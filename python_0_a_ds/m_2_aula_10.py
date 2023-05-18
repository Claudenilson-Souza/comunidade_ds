from msilib import type_string
import numpy as np
import pandas as pd
import plotly.express as px


data=pd.read_csv("dataset/kc_house_data.csv")

print(data.dtypes)



#qual a data do imovel mais antigo do portifólio?

data['date']=pd.to_datetime(data['date'])
print(data.sort_values('date',ascending=True))
print("\na data do imovel mais antigo é: 2014-05-02 ")

#quantos imoveis possuem o numero maximo de andares?

#print(data[['floors']].sort_values('floors',ascending=False))
print("\n",data['floors'].unique())

print("\n",data[data['floors'] == 3.5].shape)

print("\n8 casas possuem o numero maximo de andares")

#criar uma classificação para imoveis, 
# separando-os em baixo padrao e alto padrao
# de acordo com preço

data['level'] = 'standard'

print(data.columns)

data.loc[data['price'] >540000,'level']='high_standard' 
data.loc[data['price'] <=540000,'level']='low_standard' 

print("\n",data['level'])

#relatorio ordenado pelo preço e contendo:
# id do imovel, data q o imovel ficou disponivel p compra, 
# o numero de quartos, o tamanho total do terreno, 
# o preço e a classificação (alto e baixo)
print(data.columns)

print(data[['id','date','bedrooms','sqft_lot','price','level']].sort_values('price',ascending=True))

#index false para nao por os index originais bagunçando arquivo
""" report=data[['id','date','bedrooms','sqft_lot','price','level']].sort_values('price',ascending=True)
report.to_csv('dataset/m_2_aula10.csv', index=False) """

#criando mapa com as casas do arquivo csv no potly

""" data_map = data[['id', 'lat','long','price']]

mapa = px.scatter_mapbox(data_map, lat= 'lat', lon='long',
                        hover_name='id',
                        hover_data= ['price'], #sempre como lista
                        color_discrete_sequence= ['darkgreen'],
                        zoom=7,
                        height = 600)

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin= {'r':0, 't':0, 'l':0, 'b': 0})
mapa.show()

mapa.write_html('datasets/mapa_house_rocket.html')  """

#Exercicios m 2 aula12
#1. Crie uma nova coluna chamada: “house_age”
#• Se o valor da coluna “date” for maior que 2014-01-01 => ‘new_house’
#• Se o valor da coluna “date” for menor que 2014-01-01 => ‘old_house’

data['house_age']= "old"
house=2014-1-1
house=pd.to_datetime(house)

data.loc[ data['date'] > house, 'house_age']='new_house'
data.loc[ data['date'] < house, 'house_age']='old_house'

#2. Crie uma nova coluna chamada: “dormitory_type”
#• Se o valor da coluna “bedrooms” for igual à 1 => ‘studio’
#• Se o valor da coluna “bedrooms” for igual a 2 => ‘apartament’
#• Se o valor da coluna “bedrooms” for maior que 2 => ‘house’

""" data['dormitory_type']=''

data.loc[data['bedrooms'] == 1,'dormitory_type'] = 'studio'
data.loc[data['bedrooms'] == 2,'dormitory_type'] ='apartament'
data.loc[data['bedrooms'] > 2,'dormitory_type'] = 'house' """

data['dormitory_type'] = 'NA'
for i in range( len( data ) ):
    if data.loc[i, 'bedrooms'] == 1:
        data.loc[i, 'dormitory_type'] = 'studio'
    elif data.loc[i, 'bedrooms'] == 2:
        data.loc[i, 'dormitory_type'] = 'apartment'
    elif data.loc[i, 'bedrooms'] > 2:
        data.loc[i, 'dormitory_type'] = 'house'

#3. Crie uma nova coluna chamada: “condition_type”
#• Se o valor da coluna “condition” for menor ou igual à 2 => ‘bad’
#• Se o valor da coluna “condition” for igual à 3 ou 4 => ‘regular’
#• Se o valor da coluna “condition” for igual à 5 => ‘good’

""" data['condition_type']=''
data.loc[data['condition'] >= 2, 'condition_type']= 'bad'
data[lambda x: ((x['condition'] > 2) & (x['condition'] < 5)), 'condition_type']= 'regular'
data.loc[data['condition'] == 5, 'condition_type']= 'good'

print(data['condition_type']) """
 

data['condition'] = data['condition'].astype( int )
data['conditional_type'] = data['condition'].apply( lambda x: 'bad' if x <= 2 
else 'regular' if (x == 3) | (x == 4) else 'good' )

#4. Modifique o TIPO a Coluna “condition” para STRING

data['condition']=data['condition'].astype( str )

#5. Delete as colunas: “sqft_living15” e “sqft_lot15”

data = data.drop(['sqft_living15','sqft_lot15'], axis=1)

#6. Modifique o TIPO a Coluna “yr_build” para DATE

data['yr_built']=pd.to_datetime(data['yr_built'], format="%Y")

#7. Modifique o TIPO a Coluna “yr_renovated” para DATE

data['yr_renovated'] = data['yr_renovated'].apply( lambda x: pd.to_datetime( x,format='%Y') if x > 0 else x )

#8. Qual a data mais antiga de construção de um imóvel?
house=data['yr_built'].min()
print("\n the oldest house {}".format(house))

#9. Qual a data mais antiga de renovação de um imóvel?

#min_date = data.where(data['yr_renovated'] > pd.to_datetime('1900-01-01',format='%Y-%m-%d')).min()
df = data[data['yr_renovated'] != 0]['yr_renovated']
print( '\nThe oldest house renovated is {} years old'.format( df.min() ) )

#10. Quantos imóveis tem 2 andares?

print("\n properties with two floors",len( data[data['floors'] == 2]))

#11. Quantos imóveis estão com a condição igual a “regular” ?

print("\n properties with condicion like regular ", len(data[data['conditional_type']=='regular']))

#12. Quantos imóveis estão com a condição igual a “bad”e possuem “vista para água” ?

houses = data[(data['conditional_type'] == 'bad') & (data['waterfront'] == 1)].shape[0]
print( "\nNumber of Houses with water view and bad condition: {}".format( houses))

#13. Quantos imóveis estão com a condição igual a “good” e são “new_house”?

house=data[(data['conditional_type']=='good')&(data['house_age']=='new_house')].shape[0]
print("\n {} houses are good and new houses".format(house))

#14. Qual o valor do imóvel mais caro do tipo “studio” ?

house= data[data['dormitory_type']=='studio']['price'].max()
print("\nThe biggest price is: {}".format(house))

#15. Quantos imóveis do tipo “apartment” foram reformados em 2015 ?

house= data[(data['dormitory_type']=='apartment') & (data['yr_renovated']==2015)].shape[0]
print("\n {} was renovate in 2015".format(house))

#16. Qual o maior número de quartos que um imóveis do tipo “house” possui ?
house=data[data['dormitory_type']=='house']['bedrooms'].max()
print("\nThe biggest numbers of bedrooms in a house is: {}".format(house)  )

#17. Quantos imóveis “new_house” foram reformados no ano de 2014?

house = data.loc[(data['house_age']=='new_house') & (data['yr_renovated'] == pd.to_datetime(2014, format="%Y") ),'id'].size
print("\n {} houses if type new_house was renovated in 2014".format(house))

#18. Selecione as colunas: “id”, “date”, “price”, “floors”, “zipcode” pelo método:
#• Direto pelo nome das colunas.
#• Pelos Índices.
#• Pelos Índices das linhas e o nome das colunas
#• Índices Booleanos
print("\n for columns",data[['id','date','price','floors','zipcode']])
print("\n for index",data.iloc[[ 0, 1, 2, 7, 15]])
print("\n for index of lines and name of columns",data.loc[0:5 ,['id','date','price','floors','zipcode']])
print("\n for booleans index",data.iloc[[1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0]])

house = data.columns

#house.to_csv('dataset/house_columns.csv', index=False)
data[['house_age', 'dormitory_type', 'conditional_type']].to_csv( 'exercicio18.csv' )

#20. Modifique a cor dos pontos no mapa de “pink” para “verde-escuro” 
#    color_discrete_sequence= ['darkgreen'],