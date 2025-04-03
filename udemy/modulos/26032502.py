# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta

valorImprestimo = 1_000_000
dataEmprestimo = datetime(2020, 12, 20)
deltaAnos = relativedelta(years=5)

dataFinal = dataEmprestimo + deltaAnos

data_parcelas = []
dataParcela = dataEmprestimo
while dataParcela <= dataFinal:
    data_parcelas.append(dataParcela)
    dataParcela += relativedelta(months=1)

totalParcelas = len(data_parcelas)
valorMensal = valorImprestimo / totalParcelas

for data in data_parcelas:
    numeroParcela = data_parcelas.index(data) + 1
    print(f'{numeroParcela}° - {data.strftime("%d/%m/%Y")}: Valor a Pagar R$ {valorMensal:,.2f}')  
print()
print(f'Valor do empréstimo: R$ {valorImprestimo:,.2f}')