package br.com.piramidebasequadrada;
import java.util.Scanner;

public class DesafioPiramide {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String linha;
		int nivel;
		
		System.out.print("*** Pirâmide de Base Quadrada ***");
		System.out.println("\nDigite o lado N da pirâmide: ");
		int N = scanner.nextInt();
		double meioPiramide = N / 2;
		scanner.close();
		
		System.out.println("\nPirâmide de lado " + N + " * " + N + ":");
		for (int i = 0; i < N; i++) {
			linha = "1";
			nivel = 1;
			for (int j = 0; j < N - 1; j++) {
				
				if (i < meioPiramide) {
					if ((j < meioPiramide) && (nivel < i +1))
						nivel++;
					else if ((nivel > 1) && (j >= (N - (i + 1))))
						nivel--;
					
					linha += " " + Integer.toString(nivel);
				} else {
					if ((j < meioPiramide) && (nivel < N - i))
						nivel++;
					else if ((nivel > 1) && (j >= N - (N - i)))
						nivel--;
					
					linha += " " + Integer.toString(nivel);
				}
				
			}
			System.out.println(linha);
		}
	}

}
