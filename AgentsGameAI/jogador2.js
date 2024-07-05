/* aqui é o único lugar que você pode mexer! */
/* @param último tempo em que a IA executou ( formato de Date.now() ) */
jogador2.ia = function (tempo) {
    /* os métodos que você pode usar são (sem os parâmetros representados): 
     * 
     * (o que eu sei sobre minha bactéria?)
     * this.meuNome
     * this.meuX
     * this.meuY
     * this.meuAngulo
     * this.meuTamanho
     * this.minhaVelocidade
     * this.meuTurbo
     * this.meuToxico
     * 
     * (o que minha bactéria pode fazer?)
     * this.acionarTurbo
     * this.acionarToxina
     * this.direcionar
     * this.mudarNome
     * 
     * (o que eu sei sobre meu inimigo?)
     * this.distanciaDoInimigo
     * this.anguloDoInimigo
     * this.tamanhoDoInimigo
     * this.velocidadeDoInimigo
     * this.toxicoInimigo
     * 
     * (o que eu sei sobre o cenário?)
     * this.distanciaDaComidaMaisProxima
     * this.anguloDaComidaMaisProxima
     * this.distanciaAteUmaParede
     * this.anguloDaParedeMaisProxima
     * 
     * */
	//alert mostra algo na tela
    //alert(this.meuNome());
	//alert(this.distanciaDaComidaMaisProxima());
	
	if(this.meuTamanho() > this.tamanhoDoInimigo()){
		this.direcionar(this.anguloDoInimigo());
		this.acionarToxina();
		this.acionarTurbo();
	}
	else{
		if((this.distanciaDoInimigo()) < 100 && (this.tamanhoDoInimigo() > this.meuTamanho()) || (this.toxicoInimigo() == true)){
			this.direcionar(180);
			this.acionarToxina();
		}
		else{
			this.direcionar(this.anguloDaComidaMaisProxima());
		}
	}
	
    /*
     * as restrições para seu código são as seguintes:
     * 
     * 1) você não pode usar recursividade
     * 2) se você usar laços, a soma de todas as iterações de todos os laços não
     *    pode passar de 100 (o professor pode contar isso fácil com depuradores
     *    para garantir a integridade da competição)
     * 3) você não pode acessar ou alterar elementos de HTML ou CSS do jogo
     * 4) você só pode usar recursos nativos de JavaScript, e nenhuma biblioteca
     *    ou engine adicional é permitida
     * 5) você não pode criar invocações de funções ou métodos adicionais
     *    usando setInterval ou equivalentes do JavaScript, e você não pode
     *    criar esperas de tempo (equivalentes a "sleep" ou "wait")
     * 6) você só pode usar o métodos acima para criar sua lógica (acessar 
     *    qualquer outro objeto OU acessar qualquer atributo de qualquer objeto 
     *    OU usar qualquer método não permitido irá imediatamente tirá-lo da 
     *    competição)
     * 7) você pode criar variáveis globais adicionais (cuidado para não usar
     *    um nome já usado por outra variável) para controlar sua execução
     *    (para criar uma variável global em JavaScript, basta não usar o 
     *    modificador "var" no seu primeiro uso)
     * 8) antes de usar qualquer coisa mirabolante, consulte o professor!
     *    o sigilo será mantido por ele até a realização da competição
     */
}