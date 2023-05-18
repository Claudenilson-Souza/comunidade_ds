#aula 2

import pandas as pd
import numpy as np
data=pd.read_csv('dataset\kc_house_data.csv')

print("Resolução das Questões! \n")
print(data.columns,"\n")

#1 quantas casas estao disponiveis para compra? 
houses=len(data['id'].unique())
print("Temos {} casas disponiveis para compra! \n" .format(houses))
# ou len(data['id'].drop_duplicates())

#2 Quantos atributos as casas possuem?
print("As casas possuem 21 Atributos! \n")

#3 quais sao os atributos da casa?
print("Os Atributos sao: ", data.columns,"\n")

#4 qual a casa mais cara(maior valor de venda)
#print(data[['id','price']].sort_values('price',ascending=False).reset_index(drop=True).loc[0,'id'])

print("A Casa mais cara é: a com ID= 6762700020 com o preço: 7700000.0 \n")

#5 qual a casa com maior numero de quartos
#print(data[['id','bedrooms']].sort_values('bedrooms',ascending=False).reset_index(drop=True).loc[0,'id'])

print("a casa com maios numero de quartos é: a com ID= 2402100895 e com 33 quartos \n")

#6 qual a soma total de quartos do conjunto de dados?
#print(data['bedrooms'].sum())

print("a soma de total de quartos do conjunto de dados é de  72854 \n" )

#7 quantas casas possuem 2 banheiros ?

houses =len(data.loc[data['bathrooms'] == 2, ['id','bathrooms']])

print(" {} casas possuem dois banheiros".format(houses))

#8 qual o preço médio de todas as casas no conjunto de dados?
#print(data[['price']].mean())
print("\nO preço médio é de 540088 \n")

#9 qual o preço médio de casas com 2 banheiros?

houses=np.round(data.loc[data['bathrooms'] == 2, 'price'].mean(), 2)

print("O preço médio das casas com dois banheiros é de: {}".format(houses))

#10 qual o preço mínimo entre as casas com 3 quartos?

houses=np.round(data.loc[data['bedrooms'] == 3, 'price'].min(),2)
print("\nO preço médio das casas com dois banheiros é de: {}".format(houses))

#11 quantas casas possuem mais de 300 metros quadrados na sala de estar?
data['m2']=data['sqft_living'] *0.093
houses= len(data.loc[data['m2'] > 300, 'id'])

print("\n{} casas com mais de 300 metros quadrados na sala de estar".format(houses))

#12 quantas casas tem mais de 2 andares?

houses= len(data.loc[data['floors'] > 2, 'id'])

print("\n{} casas com mais de 2 andares".format(houses))

#13 quantas casas tem vista para o mar?

houses= len(data.loc[data['waterfront'] == True, 'id'])

print("\n{} casas com vista para o mar".format(houses))

#14 das casas com vista para o mar, quantas tem 3 quartos?

houses = len(data.loc[(data['waterfront']==True )&(data['bedrooms'] == 3), 'id'] )

print("\n{} casas com vista para o mar com 3 quartos".format(houses))

#15 das casas com mais de 300 metros quadrados de sala de estar, quantos possuem 2 banheiros 
data['m2']=data['sqft_living'] *0.093

houses = len(data.loc[(data['m2'] >300 )&(data['bedrooms'] == 2), 'id'] )

print("\n{} casas com vista para o mar com 300 metros quadrados de sala de estar que possuem 2 banheiros".format(houses))