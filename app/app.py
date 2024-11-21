import streamlit as st
from data_processing import load_data, summarize_data

# Carregar os dados
st.title("Dashboard de E-commerce")
file_path = './datasets/online_sales_dataset.csv'
df = load_data(file_path)

# Limpar os dados
df_clean = df

# Exibir os dados no Streamlit
st.subheader("Dados Limpos")
st.write(df_clean)

# Exibir resumo estatístico
st.subheader("Resumo Estatístico")
summary = summarize_data(df_clean)
st.write(summary)
