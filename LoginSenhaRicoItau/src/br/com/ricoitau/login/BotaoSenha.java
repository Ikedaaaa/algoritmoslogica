package br.com.ricoitau.login;

public class BotaoSenha {
	private int id;
	private String descricao;
	private int[] numeros;

	public BotaoSenha(int id, String descricao, int[] numeros){
		this.id = id;
		this.descricao = descricao;
		this.numeros = numeros;
	}

	public int getId(){
		return this.id;
	}
	public void setId(int id){
		this.id = id;
	}

	public String getDescricao(){
		return this.descricao;
	}
	public void setDescricao(String descricao){
		this.descricao = descricao;
	}

	public int[] getNumeros(){
		return this.numeros;
	}
	public void setNumeros(int[] numeros){
		this.numeros = numeros;
	}
}
