# 🤖 Análise de Estoque com Agente IA 🕵️‍♀️

E aí? 👋

**Em resumo, essa belezinha faz o seguinte:**

* **Mastiga seus dados de validade:** Você joga as informações de lote, validade e estoque, e ele processa tudo rapidinho.
* **Liga o alerta de "perigo":** Identifica os produtos que estão quase dando o "tchau" (vencendo em breve).
* **Faz as contas:** Cruza os dados de validade com a quantidade em estoque para você não ter um caminhão de produtos prestes a vencer.
* **Te entrega o ouro:** Apresenta uma análise clara e concisa, mostrando os produtos críticos e os insights mais importantes.

**Como botar essa mágica pra funcionar? É mais fácil que receita de miojo! 🍜**

1.  **Clone esse repositório camarada:**

    ```bash
    git clone https://github.com/sarafirme/Analise_de_estoque-Agente_IA.git
    cd Analise_de_estoque-Agente_IA
    ```

2.  **Crie o arquivo secreto `.env`:**

    * Na raiz do projeto, crie um arquivo chamado `.env`.
    * Dentro dele, coloque a sua chave da API do Google Gemini, assim:

        ```
        GOOGLE_API_KEY=SUA_CHAVE_SECRETA_AQUI
        ```

    * **Importante:** Essa chave é como a senha do cofre, guarde com carinho e não compartilhe com estranhos, beleza? 😉

3.  **Instale o necessário:**

    *Por enquanto o script só precisa das bibliotecas `google-generativeai` e `python-dotenv`. Se não tiver instalado, rode um `pip install google-generativeai python-dotenv`)*

4.  **Rode o projeto**

    ```bash
    python AnaliseValidade.py
    ```

    Ele vai pegar os dados de exemplo que já estão no código e te mostrar a análise.

5.  **Adapte para os SEUS dados:**

    * Abra o arquivo `AnaliseValidade.py`.
    * Na seção `if __name__ == "__main__":`, você vai encontrar um exemplo de como os dados precisam ser formatados na variável `dados`.
    * **Mande bala e coloque os SEUS dados de validade ali!** Pode ser de um arquivo, de uma planilha, do jeito que você preferir. Garanta que a estrutura seja parecida (Produto, Lote, Validade, Estoque).

**Pronto! Agora você tem um agente IA trabalhando duro para manter seu estoque nos trinques!** 😎
