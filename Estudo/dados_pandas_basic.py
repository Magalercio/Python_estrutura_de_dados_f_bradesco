import pandas as pd

series_objeto = pd.Series([1,7,9,13,17,99])

#print(series_objeto)

series_objeto2= pd.Series([4, 7, 8, -2], index = ['alfa', 'beta', 'teta', 'gama'])

#print(series_objeto2)

#Dataframe

disciplinas = {'cursos': ['Estatística', 'Economia', 'Cálculo', 'Geometria'],
               'créditos': [90,60,90,40],
               'requisito': [True, False, True, False]}

data = pd.DataFrame(disciplinas)

#print(data)

# Conversão de lista em DataFrame

nome_cidade = pd.Series(['Maringá', 'Itabira','Uberlândia'])
populacao = pd.Series([403.062,120.904,699.097])

df_city = pd.DataFrame({"Cidade": nome_cidade, "População": populacao})

#print(df_city)

#transformando listas em dicionarios

populacao_cidades_dic = dict(zip(nome_cidade,populacao))

print(type(populacao_cidades_dic))
print(populacao_cidades_dic['Itabira'])
print("Maringá" in populacao_cidades_dic)

#add novo elemento ao dicionario
populacao_cidades_dic['Vitória'] = 365.855

print(populacao_cidades_dic)

# removendo elemento do dicionário
del populacao_cidades_dic["Uberlândia"]
print(populacao_cidades_dic)