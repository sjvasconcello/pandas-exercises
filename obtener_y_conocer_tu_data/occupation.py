import pandas as pd

users = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep='|', index_col='user_id')

print(users.head(25))

print(" ")
print(users.tail(10))

# Numeros de datos
print(" ")
print(users.shape[0])

# Numeros de columnas 
print(" ")
print(users.shape[1])

# Imprime el numero de datos
print(" ")
print(users.columns)

# Como esta indexado el dataset
print(" ")
print(users.index)

#Que tipo de datos tiene el dataset
print(" ")
print(users.dtypes)

#Imprimir solo una columna 
print(" ")
print(users.occupation)

#Imprimir solo una columna 
print(" ")
print(users['occupation'])

#Cuantas diferentes ocupaciones hay en el dataset
print(" ")
print(users.occupation.nunique())

#Cuales son las ocupaciones mas frecuentes  
print(" ")
print(users.occupation.value_counts().head())

#Resumen del dataset 
print(" ")
print(users.describe())

#Resumen de todas las columnas 
print(" ")
print(users.describe(include="all"))

# REsumen de la columna occupation
print(" ")
print(users.occupation.describe())

# Promedio de las edades 
print(" ")
print(round(users.age.mean()))

# REsumen de la columna occupation
print(" ")
print(users.occupation.describe())

# REsumen de la columna occupation
print(" ")
print(users.age.value_counts().tail())
