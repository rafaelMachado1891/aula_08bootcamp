import pandas as pd
import os   # biblioteca que usa os comandos do terminal no python
import glob

# funcao que faz a leitura e consolida os arquivos json


def extrair_dados_json(pasta: str) -> pd.DataFrame: 
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


# função de transformação do dataframe

def calcular_kpi_valor_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df['Total'] = df['Quantidade'] * df["Venda"]
    return df

# Load do meu dataframe
def carregar_arquivo(df: pd.DataFrame) -> json


#arquivo de teste das minhas funções
if __name__ =="__main__":
    pasta_argumentos = "data"
    DataFrame_consolidado=extrair_dados_json(pasta=pasta_argumentos)
    print(calcular_kpi_valor_total_de_vendas(df=DataFrame_consolidado))





