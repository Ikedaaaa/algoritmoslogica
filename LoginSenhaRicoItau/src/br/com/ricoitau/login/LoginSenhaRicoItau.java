package br.com.ricoitau.login;

import java.util.Scanner;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.InputMismatchException;

public class LoginSenhaRicoItau {

	public static void main(String[] args) throws NoSuchAlgorithmException {
		
		MessageDigest digest = MessageDigest.getInstance("SHA-256");

		Scanner scanner = new Scanner(System.in);

		BotaoSenha bt1 = new BotaoSenha(0, "8 ou 5", new int[]{8,5});
		BotaoSenha bt2 = new BotaoSenha(1, "7 ou 0", new int[]{7,0});
		BotaoSenha bt3 = new BotaoSenha(2, "3 ou 2", new int[]{3,2});
		BotaoSenha bt4 = new BotaoSenha(3, "1 ou 6", new int[]{1,6});
		BotaoSenha bt5 = new BotaoSenha(4, "9 ou 4", new int[]{9,4});

		ArrayList<BotaoSenha> botoesSenha = new ArrayList<BotaoSenha>();
		botoesSenha.add(bt1); botoesSenha.add(bt2); botoesSenha.add(bt3);
		botoesSenha.add(bt4); botoesSenha.add(bt5);
		
		ArrayList<BotaoSenha> botoesDigitados = new ArrayList<BotaoSenha>();

		System.out.println("Digite uma senha de 6 dígitos numéricos para testes:");
		String senha = scanner.next();
		if (senha.length() != 6) {
			scanner.close();
			throw new IllegalArgumentException("A senha precisa ter 6 dígitos!");
		}
		if (!passwordIsInteger(senha)) {
			scanner.close();
			throw new NumberFormatException("A senha precisa conter apenas números!");
		}
		
		byte[] encodedHash = digest.digest(senha.getBytes(StandardCharsets.UTF_8));
		String hashedPassword = bytesToHex(encodedHash);
		
		int[] idBtnsSenha = new int[6];
		
		System.out.println("\n***************** SIMULADOR DE LOGIN EM CONTA RICO/XP OU ITAÚ *****************\n");

		System.out.println("Conta: 1234567");
		System.out.println("Senha de testes: " + senha);
		System.out.println("Hash da senha: " + hashedPassword);
		
		System.out.println("\nSenha:");

		System.out.println(bt1.getId() + " - " + bt1.getDescricao());
		System.out.println(bt2.getId() + " - " + bt2.getDescricao());
		System.out.println(bt3.getId() + " - " + bt3.getDescricao());
		System.out.println(bt4.getId() + " - " + bt4.getDescricao());
		System.out.println(bt5.getId() + " - " + bt5.getDescricao());

		System.out.println("\nDigite os números correspondentes as opções para cada dígito da sua Senha:");

		for (int i = 0; i < idBtnsSenha.length; i++) {
			try {
				idBtnsSenha[i] = scanner.nextInt();
				if ((idBtnsSenha[i] < 0) || (idBtnsSenha[i] > 4)) {
					scanner.close();
					throw new IllegalArgumentException("Opção inválida!");
				}
			} catch (InputMismatchException e) {
				throw new InputMismatchException("Opção Inválida!");
			}
		}

		scanner.close();
		
		long start = System.nanoTime();
		
		for (int i = 0; i < idBtnsSenha.length; i++) {
			botoesDigitados.add(findBotaoById(botoesSenha, idBtnsSenha[i]));
		}
		/*
		System.out.println("\nOs botões digitados foram:");
		for(BotaoSenha btn: botoesDigitados) {
			System.out.println(btn.getId() + " - " + btn.getDescricao());
		}
		*/
		System.out.println();
		System.out.println(findSenha(hashedPassword, botoesDigitados));
		
		long finish = System.nanoTime();
		long elapsedTime = finish - start;
		System.out.println("Tempo decorrido:\n" + elapsedTime + " nanosegundos\n" + elapsedTime / 1000000 + " milisegundos");
	}

	public static BotaoSenha findBotaoById(ArrayList<BotaoSenha> botoesList, Integer botaoId) {
		return botoesList.stream().filter(botao -> botaoId.equals(botao.getId())).findFirst().orElse(null);
	}
	
	public static String findSenha(String senhaEmHash, ArrayList<BotaoSenha> botoesDigitados) throws NoSuchAlgorithmException {
		MessageDigest digest = MessageDigest.getInstance("SHA-256");
		
		int[] digito1 = botoesDigitados.get(0).getNumeros();
		int[] digito2 = botoesDigitados.get(1).getNumeros();
		int[] digito3 = botoesDigitados.get(2).getNumeros();
		int[] digito4 = botoesDigitados.get(3).getNumeros();
		int[] digito5 = botoesDigitados.get(4).getNumeros();
		int[] digito6 = botoesDigitados.get(5).getNumeros();
		
		String tentativaSenha;
		int tentativas = 0;
		
		for (int a = 0; a < digito1.length; a++) {
			for (int b = 0; b < digito2.length; b++) {
				for (int c = 0; c < digito3.length; c++) {
					for (int d = 0; d < digito4.length; d++) {
						for (int e = 0; e < digito5.length; e++) {
							for (int f = 0; f < digito6.length; f++) {
								tentativas++;
								tentativaSenha = String.valueOf(digito1[a]) +
												 String.valueOf(digito2[b]) +
												 String.valueOf(digito3[c]) +
												 String.valueOf(digito4[d]) +
												 String.valueOf(digito5[e]) +
												 String.valueOf(digito6[f]);
								
								byte[] encodedHash = digest.digest(tentativaSenha.getBytes(StandardCharsets.UTF_8));
								String hashedPassword = bytesToHex(encodedHash);
								
								if (senhaEmHash.equals(hashedPassword))
									return  "Senha Encontrada: " + tentativaSenha +
											"\nHash da Senha encontrada: " + hashedPassword +
											"\nNúmero de Tentativas: " + tentativas;
							}
						}
					}
				}
			}
		}
		
		return "Senha Incorreta";
	}
	
	private static String bytesToHex(byte[] hash) {
		StringBuilder hexString = new StringBuilder(2 * hash.length);
		for (int i = 0; i < hash.length; i++) {
			String hex = Integer.toHexString(0xff & hash[i]);
			
			if (hex.length() == 1)
				hexString.append('0');
			
			hexString.append(hex);
		}
		return hexString.toString();
	}
	
	public static boolean passwordIsInteger(String password) {
		try {
			int numericPassword = Integer.parseInt(password);
			justToRemoveWarnings(numericPassword);
		} catch (NumberFormatException e) {
			return false;
		}
		return true;
	}
	
	public static void justToRemoveWarnings(int a) {
		
	}
}
