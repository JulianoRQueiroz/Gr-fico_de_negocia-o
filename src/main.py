import datetime as dt 
import matplotlib.pyplot as plt 
import pandas_datareader as web 

plt.style.use("dark_background")

ma_1 = 30 
ma_2 = 100 

start = dt.datetime.now() - dt.timedelta(days=365 * 3) # Uma duração expressando a diferença entre dois
end = dt.datetime.now()

''' pacote que nos permite criar um objeto DataFrame pandas usando várias fontes de dados da internet'''
data = web.DataReader('FB', 'yahoo', start, end) 
# SMA = Média Móvel Simples - Uma média móvel simples é formada pelo cálculo do preço médio de um ativo num número específico de períodos
data[f'SMA_{ma_1}'] = data['Adj Close'].rolling(window=ma_1).mean() # rolling() fornece uma janela contínua para operações matemáticas
data[f'SMA_{ma_2}'] = data['Adj Close'].rolling(window=ma_2).mean() # mean() media de uma lista 

data = data.iloc[ma_2:]  # seleciona linhas e colunas por números 

plt.plot(data['Adj Close'], label="Distribuição de Preço", color="lightgray") # plot() cria o gráfico e o armazena em um objeto na memória
plt.plot(data[f'SMA_{ma_1}'], label=f"SMA_{ma_1}", color="orange")
plt.plot(data[f'SMA_{ma_2}'], label=f"SMA_{ma_2}", color="purple")
plt.legend(loc="upper left") #  colocam a legenda no canto correspondente dos eixos (esquerda)
plt.show()

buy_signals = []
sell_signals = []