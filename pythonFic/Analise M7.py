import pandas as pd

# Criando o DataFrame
dados_vendas = {
    'Pedido_ID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    'Cliente': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Elisa', 'Felipe', 'Gabriela', 'Hugo', 'Isabel', 'João'],
    'Categoria': ['Eletrônicos', 'Roupas', 'Eletrônicos', 'Livros', 'Roupas', 'Eletrônicos', 'Livros', 'Roupas', 'Eletrônicos', 'Livros'],
    'Valor_Venda': [1200, 250, 3500, 90, 180, 2500, 120, 300, 4500, 80],
    'Data': pd.to_datetime(['2024-01-15', '2024-01-18', '2024-01-21', '2024-01-22', '2024-01-25', 
                            '2024-02-02', '2024-02-10', '2024-02-14', '2024-02-20', '2024-02-25']),
    'Quantidade': [1, 3, 2, 1, 2, 1, 2, 4, 1, 1],
    'Avaliacao': [4.5, 3.8, 4.9, 4.2, 3.5, 4.7, 4.1, 3.9, 5.0, 4.0]
}

df = pd.DataFrame(dados_vendas)

# Exibir as todas linhas do DataFrame
print(df)

#Qual foi o valor médio das vendas?

print("Valor médio das vendas:", df['Valor_Venda'].mean())

#Qual foi a categoria mais vendida em quantidade de produtos?

print(df.groupby('Categoria')['Quantidade'].sum())

#Qual foi o maior valor de venda registrado? E quem comprou?

max_venda = df[df['Valor_Venda'] == df['Valor_Venda'].max()]
print(max_venda[['Cliente', 'Valor_Venda']])

#Vendas de Produtos de Fevereiro
vendas_fevereiro = df[df['Data'].dt.month == 2]
print("Total de vendas em fevereiro:", len(vendas_fevereiro))

#Qual a média de avaliação dos clientes?
print("Média de avaliação dos clientes:", df['Avaliacao'].mean())

#Filtre apenas os pedidos de Eletrônicos e ordene-os pelo maior valor de venda. Liste os resultados.
df_eletronico = df[df['Categoria'] == 'Eletrônicos'].sort_values(by ='Valor_Venda', ascending=False)
print(df_eletronico)