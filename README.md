# 🤖 Análise Inteligente de Validade de Estoque ⏳

Este projeto utiliza inteligência artificial (Google Gemini) para simplificar a análise de datas de validade de produtos. Ele permite identificar rapidamente itens **próximos ao vencimento** ⚠️ ou com **grande quantidade em estoque prestes a vencer** 📦, auxiliando na tomada de decisões para evitar perdas 📉.

## ✨ Como Funciona ✨

O script `AnaliseValidade.py` pode analisar dados de duas maneiras:

1.  **Arquivo Excel (`Produtos_Teste.xlsx`):** Lendo diretamente os dados de uma planilha com colunas "PRODUTO", "LOTE", "VALIDADE" (formato AAAA-MM-DD) e "ESTOQUE". 📊
2.  **Dados no Código:** (Opção comentada no script) Permite inserir dados de produtos diretamente na forma de texto. 📝

O modelo Gemini processa esses dados e retorna insights sobre os produtos com **maior risco de perda por validade** 💡.

## 🚀 Utilização 🚀

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/sarafirme/Analise_de_estoque-Agente_IA.git](https://github.com/sarafirme/Analise_de_estoque-Agente_IA.git)
    cd Analise_de_estoque-Agente_IA
    ```

2.  **⚙️ Configure a Chave de API 🔑:**
    * Crie um arquivo `.env` e adicione sua chave do Google AI:
        ```
        GOOGLE_API_KEY=SUA_CHAVE_DE_API
        ```
    * *(Você pode criar um arquivo `.env` com base no `.env.sample` fornecido).*

3.  **⬇️ Instale as Dependências ⬇️:**
    no terminal digite o comando:
   `pip install google-generativeai python-dotenv pandas openpyxl`

4.  **📊 Execute a Análise (com arquivo Excel) 📈:**
    * Certifique-se de que o arquivo `Produtos_Teste.xlsx` esteja na mesma pasta.
    * Execute o script:
        ```bash
        python AnaliseValidade.py
        ```

5.  **🔍 Visualize os Resultados 👀:** A análise será exibida no terminal.

## 📂 Arquivos Principais 📂

* `.env.sample`: Exemplo de como configurar as variáveis de ambiente.
* `.gitignore`: Especifica arquivos que o Git deve ignorar.
* `AnaliseValidade.py`: O script Python principal para realizar a análise.
* `Produtos_Teste.xlsx`: Arquivo de exemplo com os dados dos produtos.
* `README.md`: Este arquivo com a descrição do projeto. 📄

Este projeto simplifica a gestão de estoque ao fornecer uma visão clara dos produtos que requerem atenção imediata devido à proximidade da data de validade. ✅

    * Abra o arquivo `AnaliseValidade.py`.
    * Na seção `if __name__ == "__main__":`, você vai encontrar um exemplo de como os dados precisam ser formatados na variável `dados`.
    * **Mande bala e coloque os SEUS dados de validade ali!** Pode ser de um arquivo, de uma planilha, do jeito que você preferir. Garanta que a estrutura seja parecida (Produto, Lote, Validade, Estoque).

**Pronto! Agora você tem um agente IA trabalhando duro para manter seu estoque nos trinques!** 😎
