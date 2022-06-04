import csv
import pandas as pd
import seaborn as sns

# Convertendo para dataframe
data = pd.read_csv('./gasolina.csv', sep=',')

# criando gráfico
with sns.axes_style('whitegrid'): 
  grafico= sns.relplot(x="dia", y="venda",  kind="line", data=data)
  grafico.set(title='Relação dia e venda de Gasolina')
  
# salvando o grafico em png
grafico.fig
grafico.fig.savefig(fname='gasolina.png', bbox_inches='tight')

print('Sucesso!')