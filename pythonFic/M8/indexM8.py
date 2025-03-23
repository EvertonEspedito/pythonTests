import pandas as pd
import matplotlib.pyplot as plt

# 1. Análise Descritiva
# Foram realizadas análises descritivas para calcular a média de algumas variáveis importantes.
# Carregar os dados
arquivo_csv = 'Everton Espedito Silva Santos - dados_projeto_final.csv'  # Substitua pelo caminho do seu arquivo CSV
dados = pd.read_csv(arquivo_csv)
# Exibir as primeiras linhas dos dados para revisão
print(dados.head())
# Análise básica
print("\nEstatísticas descritivas dos dados:")
print(dados.describe())  # Exibe estatísticas como média, desvio padrão, etc.

# ● Média de Idade:
media_idade = dados['Idade'].mean()
print(f'\nMédia de Idade:  {media_idade:.0f} anos')
# ● Média de Renda Mensal:
media_renda = dados['Renda Mensal'].mean()
print(f"\nMédia da Renda Mensal: {media_renda:.2f} Reais")
# ● Média de Compras Online:
media_compras = dados['Número de Compras Online'].mean()
print(f'\nMédia de Compras Online: {media_compras:.0f} Compras')
# ● Média de Satisfação do Cliente:
media_rate = dados['Satisfação do Cliente (1-10)'].mean()
print(f'\nMédia de Satisfação do Cliente: {media_rate:.2f}')

# 2. Análise de Correlação
# Foi calculada a correlação entre a Renda Mensal e o Número de Compras Online para
# verificar se existe uma relação entre essas variáveis.
# ● Correlação entre Renda Mensal e Compras Online:
correlacao = dados[['Renda Mensal', 'Número de Compras Online']].corr()
print("\nCorrelação entre Renda Mensal e Número de Compras Online:")
print(correlacao)

# 3. Análise por Gênero
# Realizada a análise das médias por Gênero para entender as diferenças entre homens, mulheres e
# não-binários.
# ● Média por Gênero:
media_homem = dados.loc[dados['Gênero'] == 'Masculino', 'Idade'].mean()
media_mulher = dados.loc[dados['Gênero'] == 'Feminino', 'Idade'].mean()
media_nao_binario = dados.loc[dados['Gênero'] == 'Não-Binário', 'Idade'].mean()
print(f'\nMédia de Idade por Gênero:')
print(f"Homem: {media_homem:.0f} anos")
print(f"Mulher: {media_mulher:.0f} anos")
print(f"Não-Binário: {media_nao_binario:.0f} anos")

# 4. Visualizações Gráficas

# 4.1. Gráfico de Dispersão
# Foi gerado um gráfico de dispersão para mostrar a relação entre Renda Mensal e Número de
# Compras Online.
plt.scatter(dados['Renda Mensal'], dados['Número de Compras Online'])
plt.title('Renda Mensal vs Número de Compras Online')
plt.xlabel('Renda Mensal')
plt.ylabel('Número de Compras Online')
plt.show()
# 4.2. Gráfico de Barras
# Um gráfico de barras foi criado para mostrar a média de Satisfação por Gênero.
plt.bar(['Homem', 'Mulher', 'Não-Binário'], [media_homem, media_mulher, media_nao_binario])
plt.title('Média de Satisfação por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Média de Satisfação')
plt.show()

# 5. Filtragem de Dados
# Foi realizado um filtro para encontrar os clientes com mais de 30 anos e menos de 5 compras
# online. O resultado foi o seguinte:
# ● Clientes com mais de 30 anos e menos de 5 compras online:
clientes_filtrados = dados[(dados['Idade'] > 30) & (dados['Número de Compras Online'] < 5)]
print(f'\n{clientes_filtrados}\n')

# 6. Análise de Outliers
# Foi verificado se existem outliers na Renda Mensal, utilizando o intervalo interquartílico (IQR).
# Os seguintes dados foram identificados como outliers:
# ● Outliers na Renda Mensal:
# Calcular Q1 (1º quartil) e Q3 (3º quartil)

# Carregar o arquivo CSV
df = pd.read_csv("Everton Espedito Silva Santos - dados_projeto_final.csv")  # Substitua pelo caminho correto do seu arquivo

# Calcular Q1 (1º quartil) e Q3 (3º quartil)
Q1 = dados["Renda Mensal"].quantile(0.25)
Q3 = dados["Renda Mensal"].quantile(0.75)

# Calcular IQR (Intervalo Interquartílico)
IQR = Q3 - Q1

# Definir limites para detecção de outliers
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# Identificar os outliers
outliers = dados[(dados["Renda Mensal"] < limite_inferior) | (dados["Renda Mensal"] > limite_superior)]

# Exibir os outliers encontrados
print("Outliers na Renda Mensal:")
print(outliers)

# Salvar o relatório com os resultados da análise em um arquivo de texto
with open('relatorio_analise.txt', 'w') as file:
    #Dados da Media
    file.write(f"\n1 - Análise Descritiva")
    file.write(f'\nMédia de Idade:  {media_idade:.0f} anos')
    file.write(f"\nMédia da Renda Mensal: {media_renda:.2f} Reais")
    file.write(f'\nMédia de Compras Online: {media_compras:.0f} Compras')
    file.write(f'\nMédia de Satisfação do Cliente: {media_rate:.2f}')

    file.write('\n')

    file.write(f"\n2 - Análise de Correlação")
    file.write("\nCorrelação entre Renda Mensal e Número de Compras Online:\n")
    file.write(f"{correlacao}\n")

    file.write('\n')

    file.write(f"\n3. Análise por Gênero")
    file.write(f'\nMédia de Idade por Gênero:')
    file.write(f"\nHomem: {media_homem:.0f} anos")
    file.write(f"\nMulher: {media_mulher:.0f} anos")
    file.write(f"\nNão-Binário: {media_nao_binario:.0f} anos")

    file.write('\n')

    file.write(f"\n4. Visualizações Gráficas")
    file.write(f"\n 4.1 Gráfico de Dispersão: Renda Mensal vs Número de Compras Online:\n")
    file.write(f"\n 4.2 Gráfico de Barras: Média de Satisfação por Gênero:\n")

    file.write('5. Filtragem de Dados Foi realizado um filtro para encontrar os clientes com mais de 30 anos e menos de 5 compras online. O resultado foi o seguinte:')
    file.write(f'\n{clientes_filtrados}\n')
    # file.write(f"\nDados filtrados (Renda Mensal > 5000):\n{dados_filtrados}\n")

    file.write('\n')

    file.write('\n6. Análise de Outliers Foi verificado se existem outliers na Renda Mensal, utilizando o intervalo interquartílico (IQR\n')
    file.write("\nOutliers na Renda Mensal:\n")
    file.write(f'\n{outliers}')

print("\nRelatório salvo como 'relatorio_analise.txt'.")