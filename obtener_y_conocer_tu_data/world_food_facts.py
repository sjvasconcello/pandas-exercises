import numpy as np

import pandas as pd

food = pd.read_csv('/home/sjvasconcello/Code/pandas_exercises/obtener_y_conocer_tu_data/data/en.openfoodfacts.org.products.tsv', sep='\t')

print(food.head())

#Cantidad de filas en el dataset

print(food.shape)


print(food.shape[0])

print(food.info())

print(food.columns)

# Mostrar columna 104
print(food.columns[104])

# Tipo de dato en la columna 104
print(food.dtypes['-glucose_100g'])

# Como esta indexada 
print(food.index)

# Cual es el nombre del producto 19 
print(food.values[18][7])
