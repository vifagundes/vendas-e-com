import pandas as pd

def load_data(file_path):
    """Carrega os dados de um arquivo CSV."""
    return pd.read_csv(file_path)

def summarize_data(df):
    """Gera um resumo estatístico dos dados."""
    return df.describe()
