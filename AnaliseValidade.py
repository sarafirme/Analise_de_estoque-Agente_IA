import google.generativeai as genai
from dotenv import load_dotenv
import os
import pandas as pd
import datetime


load_dotenv()

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

if not GOOGLE_API_KEY:
    print("A variável de ambiente GOOGLE_API_KEY não foi definida no .env.")
    exit()

genai.configure(api_key=GOOGLE_API_KEY)

MODEL_ID = "gemini-2.0-flash"

model = genai.GenerativeModel(MODEL_ID)

def analisar_validade(dados_validade):
    """
    Analisa dados de validade de produtos usando o modelo Gemini.

    Args:
        dados_validade (str): Uma string contendo informações sobre produtos, lotes, datas de validade e estoques.

    Returns:
        str: Uma análise concisa dos dados de validade, identificando padrões e insights sobre produtos próximos ao vencimento ou com grande estoque perto da data de validade.
    """
    prompt = f"""
    Analise os seguintes dados de validade de produtos e me diga se há algum padrão
    ou insight interessante sobre produtos próximos ao vencimento ou com grande quantidade
    em estoque perto da data de validade.

    Dados:
    {dados_validade}

    Tente identificar:
    - Produtos com maior risco de vencer em breve (próximos a data atual: {datetime.date.today().strftime('%Y-%m-%d')}.
    - Produtos com grande estoque e data de validade próxima.

    Responda de forma clara e concisa, incluindo os nomes dos produtos e as informações relevantes.
    """
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    import datetime
    produtos_excel = "Produtos_Teste.xlsx"

    try:
        df = pd.read_excel(produtos_excel)

        if 'PRODUTO' not in df.columns or 'VALIDADE' not in df.columns or 'ESTOQUE' not in df.columns or 'LOTE' not in df.columns:
            print("A planilha deve conter as colunas 'PRODUTO', 'LOTE', 'VALIDADE' e 'ESTOQUE'.")
        else:
            dados_analise = ""
            for index, row in df.iterrows():
                dados_analise += f"Produto: {row['PRODUTO']}, Lote: {row['LOTE']}, Validade: {row['VALIDADE'].strftime('%Y-%m-%d')}, Estoque: {int(row['ESTOQUE'])}\n"

            insights = analisar_validade(dados_analise)
            print("Análise de Validade:\n")
            print(insights)

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo_excel}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler a planilha: {e}")

#     # Exemplo de dados de validade
#     dados = """
# Produto: Lote A, Validade: 2025-06-15, Estoque: 100
# Produto: Lote B, Validade: 2025-05-25, Estoque: 50
# Produto: Lote C, Validade: 2025-07-01, Estoque: 200
# Produto: Lote D, Validade: 2025-05-20, Estoque: 150
# Produto: Lote E, Validade: 2025-08-10, Estoque: 300
# Produto: Lote F, Validade: 2025-05-10, Estoque: 20
# """
#     insights = analisar_validade(dados)
#     print("Análise de Validade:\n")
#     print(insights)