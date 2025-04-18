import pandas as pd 
from sklearn.linear_model import LinearRegression

#Exemplos dos meses
dados = pd.DataFrame({
    'mes': [1, 2, 3, 4, 5, 6],
    'gasto': ['2150', '2050', '2350', '2300', '2000', '1750']
})

x = dados [['mes']]
y = dados['gasto']

modelo = LinearRegression()
modelo.fit(x, y)

#Previsão para o mês 7
previsao = modelo.predict([[7]])
print(f"Previsão de gasto para mês 7: R${previsao[0]:.2f}")
