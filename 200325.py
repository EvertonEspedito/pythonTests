# import numpy as np
# import scipy.stats as st

# n = 40
# x_bar = 20
# s = 7.5
# conf = 0.95
# z = st.norm.ppf((1 + conf) / 2)
# margin = z * (s / np.sqrt(n))
# intervalo = (x_bar - margin, x_bar + margin)
# print("Intervalo de Confiança de 95%:", intervalo)

import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

def calcular_intervalo_confiança(media, desvio, tamanho_amostra, nivel_confianca, distribuicao='normal'):
    if distribuicao == 'normal':
        z = st.norm.ppf((1 + nivel_confianca) / 2)
    else:
        z = st.t.ppf((1 + nivel_confianca) / 2, df=tamanho_amostra-1)
    
    margem_erro = z * (desvio / np.sqrt(tamanho_amostra))
    intervalo = (media - margem_erro, media + margem_erro)
    return intervalo

# (a) Tempo médio de espera no consultório
print("\nItem (a) - Tempo médio de espera no consultório")
intervalo_a = calcular_intervalo_confiança(media=20, desvio=7.5, tamanho_amostra=40, nivel_confianca=0.95, distribuicao='normal')
print(f"Intervalo de confiança de 95%: {intervalo_a}")

# (b) Gorjeta média
print("\nItem (b) - Gorjeta média")
intervalo_b = calcular_intervalo_confiança(media=3.75, desvio=0.25, tamanho_amostra=20, nivel_confianca=0.99, distribuicao='t-student')
print(f"Intervalo de confiança de 99%: {intervalo_b}")

# (c) Peso das caixas de cereal
print("\nItem (c) - Peso das caixas de cereal")
intervalo_c = calcular_intervalo_confiança(media=11.89, desvio=0.05, tamanho_amostra=15, nivel_confianca=0.90, distribuicao='normal')
print(f"Intervalo de confiança de 90%: {intervalo_c}")

# Gráfico de Distribuição do Item (b)
np.random.seed(42)
amostras = np.random.normal(loc=3.75, scale=0.25/np.sqrt(20), size=1000)

plt.hist(amostras, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.axvline(intervalo_b[0], color='red', linestyle='dashed', label='Limite Inferior')
plt.axvline(intervalo_b[1], color='green', linestyle='dashed', label='Limite Superior')
plt.axvline(3.75, color='black', linestyle='dashed', label='Média')
plt.title("Distribuição das Amostras e Intervalo de Confiança")
plt.legend()
plt.show()
