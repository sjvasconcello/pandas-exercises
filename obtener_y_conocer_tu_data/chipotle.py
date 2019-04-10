import numpy as np

import pandas as pd

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

chipo = pd.read_csv(url, sep='\t')

# Te muestra las primeras 5 filas
print(chipo.head(5))

# Te dice cuantas entradas hay en la tabla
print(chipo.shape[0])

# Te muestra los datos que tiene la tabla
print(chipo.info())

# Te muestra cuantas columnas hay en el dataset
print(chipo.shape[1])

# Imprime el nombre de las columnas
print(chipo.columns)

# Como es el index en el dataset
print(chipo.index)

print("")
print("")
print("------------------------------------------")
print("Para el articulo más pedido, ¿Cuántos artículos se ordenaron?")
print("")
print("")

c1 = chipo.groupby('item_name').sum()
c1 = c1.sort_values(['quantity'], ascending=False)
print(c1.head())

print("")
print("")
print("------------------------------------------")
print("¿Cuál fue el artículo más ordenado en la columna choice_description?")
print("")
print("")

c2 = chipo.groupby('choice_description').sum()
c2 = c2.sort_values(['quantity'], ascending=False)
print(c2.head())


print("")
print("")
print("------------------------------------------")
print("Cuantos item hay en total?")
print("")

total_items_orders = chipo.quantity.sum()
print(total_items_orders)


print("")
print("")

print(chipo.item_price.dtype)


def dollarizer(x): return float(x[1:-1])


chipo.item_price = chipo.item_price.apply(dollarizer)

print(chipo.item_price.dtype)


print("")
print("")
print("------------------------------------------")
print("¿Cupanto fue el ingreso para el período en el conjunto de datos?")
print("")
print("")

revenue = (chipo['quantity']*chipo['item_price']).sum()
print(revenue)

print('Revenue was: $' + str(np.round(revenue, 2)))


print("")
print("")
print("------------------------------------------")
print("¿Cual es el promedio por orden?")
print("")
print("")

chipo['revenue'] = chipo['quantity']*chipo['item_price']
order_grouped = chipo.groupby(by=['order_id']).sum()
print(order_grouped.mean()['revenue'])
print(chipo.head())


print("------------------------------------------")

print(chipo.groupby(by='order_id').sum().mean()['revenue'])

print("")
print("")
print("------------------------------------------")
print("¿Cuantos diferentes item vendio?")
print("")
print("")

print(chipo.item_name.value_counts().count())
