import pandas as pd

autores = pd.read_csv('autores.csv', index_col=0)
print(autores)
print("_"*50)
print(autores.info())
print("_"*50)
print(autores.columns)
print("_"*50)
print(autores.index)