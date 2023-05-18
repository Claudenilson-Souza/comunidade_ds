import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import gridspec
import plotly.express as px
import seaborn as sns
import time
from multiprocessing import Pool
import numpy as np

pd.set_option('display.float_format', lambda x: '%.2f' % x)

data = pd.read_csv('dataset\kc_house_data.csv')

data['date'] = pd.to_datetime(data['date'])

data['season'] = 'NA'

data['season'] = data['date'].apply(lambda x:
                                    'smr' if ((x.month >= 6) and (x.month <= 8)) else  # smr = summer
                                    'aut' if ((x.month >= 9) and (x.month <= 11)) else  # aut = autumn
                                    'win' if ((x.month == 12) or (
                                                x.month <= 2))  # win = winter
                                    else 'spr')  # spr = spring

df = data[['zipcode', 'price']].groupby('zipcode').median().reset_index()
df.columns = ['zipcode', 'median_price']

df1 = pd.merge(data, df, on='zipcode', how='inner').reset_index()

df1[['price', 'median_price']]

df1['status'] = df1.apply(lambda x:
                          'compra' if (x['price'] < x['median_price']) & (x['condition'] >= 3) & (x['waterfront'] == 1)
                          else 'não_compra', axis=1)

df2 = df1[['id', 'zipcode', 'price', 'median_price', 'condition', 'status']]

# for i in range (len(df1)):
#    if (df1.loc [i,'price'] < df1.loc [i,'median_price']) and (df1.loc [i,'condition'] >=2):
#        df1.loc[i,'status'] = 'compra'
#    else:
#        df1.loc[i,'status'] = 'nao_compra'


# - Agrupar os
# imóveis por região ( zipcode ) e por
# sazonalidade ( Summer, Inter ) -- e tamanho
# - Vou sugerir os imóveis que estão
# abaixo do preço mediano da região e que estejam e boas
# condições e vista para água.

df1['sell_price'] = df1.apply(lambda x:
                              x['price'] + (x['price'] * 0.30) if x['price'] < x['median_price']
                              else x['price'] + (x['price'] * 0.10), axis=1)

for i in range(len(df1)):
    if 1 == 1:
        df1.loc[i, 'profit'] = df1.loc[i, 'sell_price'] - df1.loc[i, 'price']

df3 = df1[['id', 'zipcode', 'season', 'median_price', 'price', 'sell_price', 'profit']]

df3.rename(columns={'price': 'buy_price'}, inplace=True)

# df3[['id','zipcode','season','median_price','buy_price','sell_price','profit']]

df3.head()

# cod | regiao | temporada | preço medio | preco compra | preco venda | lucro

data.columns

# H1: Imóveis que possuem vista para água, são 30% mais caros, na média

houses = data[['waterfront', 'price']].groupby('waterfront').mean().reset_index()
y = houses.loc[0, 'price'] * 0.30

if (houses.loc[0, 'price'] + y) < houses.loc[1, 'price']:
    x = int((houses.loc[0, 'price'] * 100) / houses.loc[1, 'price'])

    print(
        "As casas que possuem vista para agua são {} % mais caros na média do que as que não possuem vista para agua ".format(
            x))
else:
    print(
        "As casas que não possuem vista para agua são mais caros (ou iguais) na média do que as que possuem vista para agua ")

# H2: Imóveis com data de construção menor que 1955, são
# 50% mais baratos, na média.

houses = data[['yr_built', 'price']].groupby('yr_built').mean().reset_index()

cont = 0
cont1 = 0
for i in range(len(houses)):
    if houses.loc[i, 'yr_built'] < 1955:
        x = houses.loc[i, 'price']
        cont = cont + 1
    if houses.loc[i, 'yr_built'] >= 1955:
        x1 = houses.loc[i, 'price']
        cont1 = cont1 + 1

x = x / cont
x1 = x1 / cont1
print(x, " ", x1)

if x < x1 * 0.5:
    print("as casas construidas antes de 1955 são 50% (ou mais) baratas que as construidas apos 1955")
else:
    print("as casas construidas antes de 1955 são 50% (ou mais) baratas que as construidas apos 1955")

x = (int((x * 100) / (x1 - 1)))

print("elas sao {}% mais caras ".format(x))

# H3: Imóveis sem porão possuem sqrt_lot, são 50%
# maiores do que com porão.

data.columns

houses = data[['sqft_lot', 'sqft_basement']].groupby('sqft_basement').mean().reset_index()

cont1 = 0
for i in range(len(houses)):
    if houses.loc[i, 'sqft_basement'] == 0:
        x = houses.loc[i, 'sqft_lot']
    if houses.loc[i, 'sqft_basement'] > 0:
        x1 = houses.loc[i, 'sqft_lot']
        cont1 = cont1 + 1
x = x
x1 = x1 / cont1

print(x, " ", x1)

if x < x1 * 0.5:
    print("as que não possuem poram são 50%(ou mais) maiores na média do que as que possuem")
else:
    x = int((x * 100) / (x1 - 1))
    print(x)

    print("os que possuem poram são {}% maiores ".format(x))

# H4: o crescimento do preço dos imóveis yoy (year over year) é de 10%

houses = data[['price', 'date']].reset_index()

for i in range(len(houses)):
    if 1 == 1:
        houses.loc[i, 'year'] = houses.loc[i, 'date'].year
        houses.loc[i, 'month'] = houses.loc[i, 'date'].month

a = houses['year'].unique

print(a)

casa = pd.DataFrame()
casa1 = pd.DataFrame()

    for i in range(len(houses)):
        if (houses.loc[i, 'date'].year == 2015) and (houses.loc[i, 'date'].month == 5):
            casa.loc[i, 'month'] = houses.loc[i, 'date'].month
            casa.loc[i, 'year'] = houses.loc[i, 'date'].year
            casa.loc[i, 'price'] = houses.loc[i, 'price']

    if (houses.loc[i, 'date'].year == 2015 - 1) and (houses.loc[i, 'date'].month == 5):
        casa1.loc[i, 'month'] = houses.loc[i, 'date'].month
        casa1.loc[i, 'year'] = houses.loc[i, 'date'].year
        casa1.loc[i, 'price'] = houses.loc[i, 'price']

    casa = casa[['price', 'year']].groupby('year').mean().reset_index()
    casa1 = casa1[['price', 'year']].groupby('year').mean().reset_index()

    if casa.loc[0, 'price'] > casa1.loc[0, 'price']:
        x = (int((casa['price'] * 100) / (casa1['price'] - 1)))
        print("as casas mais novas são {}% mais caras ".format(x))

    if casa.loc[0, 'price'] < casa1.loc[0, 'price']:
        x = (int((casa1['price'] * 100) / (casa['price'] - 1)))
        print("as casas mais velhas são {}% mais caras ".format(x))


# H5: Imóveis com 3 banheiros tem um crescimento MoM ( Month over Month ) de 15%