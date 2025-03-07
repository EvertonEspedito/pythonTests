# copy, sorted, produtos.sort
# Exercícios

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

for produto in produtos:
      print(produto['nome'], produto['preco'])
print()      
# Aumente os preços dos produtos a seguir em 10%
produtos = [{'nome': produto['nome'], 'preco': produto['preco'] * 1.10} for produto in produtos]
for produto in produtos:
      print(produto['nome'], produto['preco'])
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = [produto.copy() for produto in produtos]
print()
# Ordene os produtos por nome decrescente (do maior para menor)
produtos.sort(key=lambda produto: produto['nome'], reverse=True)
for produto in produtos:
      print(produto['nome'], produto['preco'])
print()      
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = [produto.copy() for produto in produtos]

# Ordene os produtos por preco crescente (do menor para maior)
produtos.sort(key=lambda produto: produto['preco'])
print()
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = [produto.copy() for produto in produtos]
for produtos in produtos_ordenados_por_preco:
      print(produtos['nome'], produtos['preco'])