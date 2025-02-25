#Gráficos
import matplotlib.pyplot as plt
import seaborn as sns

#dados tabulares
import pandas as pd

#avisos
import warnings 
warnings.filterwarnings(action='ignore')

#DataSets
data = sns.load_dataset('tips')
data.head()

#copia de trabalho
df = data.copy(deep=True)
df.head()

#Renomear Colunas
#Renomear valores dentro das colunas categoricas(Variaveis numericas Categóricas)
df.columns
aux = {'total_bill':'conta', 'tip':'gorjeta', 'sex':'genero',
           'smoker':'fumante', 'day':'dia', 'time':'hora', 'size':'mesa'}

#map, filter, reduce
df.rename(mapper=aux,axis=1,inplace=True)
df.head()

df['hora'].unique()

# alterar valores categóricos das colunas
df['genero'].replace(to_replace={'Female':'F', 'Male':'M'}, inplace=True)
df['fumante'].replace(to_replace={'No':'N', 'Yes':'S'}, inplace=True)
df['dia'].replace(to_replace={'Sun':'Dom', 'Sat':'Sab', 'Thur':'Qui', 'Fri':'Sex'}, inplace=True)
df['hora'].replace(to_replace={'Dinner':'Jantar', 'Lunch':'Almoco'}, inplace=True)

df.sample(10)

df.info()

# # categorical describe
df.describe(include='category').T

# nuumerical describe
df[['conta', 'gorjeta']].describe().round(2).T

# built-in do pandas
df[['conta', 'gorjeta']].plot(kind='hist', subplots=True, layout=(1,2), bins=30, 
                              sharex=False, sharey=False, figsize=(12,5),
                              title='Relação entre Conta e Gorjeta');
plt.show()


plt.figure(figsize=(12, 5))
plt.subplot(121)
sns.histplot(data=df, x='conta', kde=True, label='Conta')
plt.title('Distribuição dos valores das Contas')
plt.legend()

plt.subplot(122)
sns.histplot(data=df, x='gorjeta', kde=True, label='Gorjeta')
plt.title('Distribuição dos valores das Gorjetas')
plt.legend();

plt.show()

