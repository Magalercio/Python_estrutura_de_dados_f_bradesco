import pandas as pd

Autor = ['Sun Tzu', 'Fernando Pessoa', 'Thomas Mann', 'João Guimarães Rosa']
Livro = ['A arte da Guerra', 'Poesias Selecionadas', 'A montanha Mágica', 'Primeiras Estórias']
Ano = [2000, 2004, 2015, 2017]

dados = {
        'Autor': Autor,
        'Livro': Livro,
        'Ano': Ano
        }

autores = pd.DataFrame(dados)

print(type(autores))
df = pd.DataFrame(autores)
print(df)

#convertendo em csv
df.to_csv("autores.csv")