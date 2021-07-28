import datetime as dt
from matplotlib import lines 
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
# Adj Close = Preço de fechamento ajustado O fechamento ajustado - é o preço de fechamento após os ajustes para todas as divisões e distribuições de dividendos aplicáveis
data = data.iloc[ma_2:]  # seleciona linhas e colunas por números 

plt.plot(data['Adj Close'], label="Distribuição de Preço", color="lightgray") # plot() cria o gráfico e o armazena em um objeto na memória
plt.plot(data[f'SMA_{ma_1}'], label=f"SMA_{ma_1}", color="orange")
plt.plot(data[f'SMA_{ma_2}'], label=f"SMA_{ma_2}", color="purple")
plt.legend(loc="upper left") #  colocam a legenda no canto correspondente dos eixos (esquerda)
plt.show()

buy_signals = []
sell_signals = []
trigger = 0 

for x in range(len(data)):
    if data[f'SMA_{ma_1}'].iloc[x] > data[f'SMA_{ma_2}'].iloc[x] and trigger != 1:
        buy_signals.append(data['Adj Close'].iloc[x]) # seleciona linhas e colunas por números
        sell_signals.append(float('nan'))
        trigger = 1
    elif data[f'SMA_{ma_1}'].iloc[x] < data[f'SMA_{ma_2}'].iloc[x] and trigger != -1:
        buy_signals.append(float('nan'))
        sell_signals.append(data['Adj Close'].iloc[x])
        trigger = -1 
    else:
        buy_signals.append(float('nan'))
        sell_signals.append(float('nan'))

data['Sinal de Compra'] = buy_signals
data['Sinal de Venda'] = sell_signals

print(data)

plt.plot(data['Adj Close'], label="Distribuição de Preço", alpha=0.5) 
plt.plot(data[f'SMA_{ma_1}'], label=f"SMA_{ma_1}", color="orange",linestyle="--")
plt.plot(data[f'SMA_{ma_2}'], label=f"SMA_{ma_2}", color="pink", linestyle="--")
plt.scatter(data.index, data['Sinal de Compra'], label='Sinal de Compra', marker="^", color="#00ff00", lw=3)
plt.scatter(data.index, data['Sinal de Venda'], label='Sinal de Venda', marker="v", color="#ff0000", lw=3)
plt.legend(loc="upper left")
plt.show()