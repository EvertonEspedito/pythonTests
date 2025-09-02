
import pandas as pd


# Dados extraídos manualmente da imagem
dados = [
    ("Pedro Lucas Souza Santos Moraes", 425),
    ("Victor Gabriel Carvalho Souza", 0),
    ("Adrian Felipe de Amorim Oliveira", 545),
    ("Raquel Santos Conceição", 475),
    ("Lucas Pereira Mota", 470),
    ("Marina Joaquina de Lima Ferreira", 450),
    ("Deillon Jhon Alves", 470),
    ("Pamela Alice Barbosa Ribeiro da Silva", 0),
    ("Marcos Vinicius Freitas Trindade", 640),
    ("Pedro Gabriel Almeira Piaia", 470),
    ("Ray Gustavo Oliveira Siqueira", 435),
    ("Ismael Leite Rodrigues Nunes", 0),
    ("Luan Gabriel Nunez Diniz", 400),
    ("Breno dos Reis Dias", 350),
    ("João Gabriel de Araújo Alves", 415),
    ("Sophia de Andrade Alves", 55),
    ("Andrey Marlon Barbosa Ribeiro Da Silva", 0),
    ("Marcelo de Castro Marques Vanzo", 490),
    ("Deivid Cassiano Quezado de Lima", 335),
    ("Diogo Coelho Amorim", 475),
    ("Luigi Gustavo Moreira Souza", 220),
    ("Ingrid Maria dos Santos Vieira", 385),
]

# Criar DataFrame
df = pd.DataFrame(dados, columns=["Nome", "Total"])

# Ordenar ranking por pontos (decrescente)
ranking = df.sort_values(by="Total", ascending=False).reset_index(drop=True)

# Adicionar coluna de posição
ranking.index += 1
ranking.insert(0, "Posição", ranking.index)
# Salvar em CSV
ranking.to_csv("ranking.csv", index=False)

print("Ranking salvo em 'ranking.csv'")

print(ranking)