# %%
import pandas as pd

# %%

df = pd.read_csv("../data/pedido.csv")
df

# %%

# select idPedido, flKetchup from pedido
colunas = ['idPedido', 'flKetchup']

df[colunas]

# %%

# df vai aparecer na ordem que eu definir:

colunas = [
    'idPedido'
    , 'descUF'
    , 'flKetchup'
    , 'txtRecado'
    , 'dtPedido'
]

df[colunas].head()

# %%
# ordenar colunas em ordem alfabética:

colunas = df.columns.tolist()
colunas.sort()

df[colunas]

# %%

# Criar um dataframe novo com 100 dados aleatórios do dataframe antigo

df_sample = df.sample(100)
df_sample

# %%
# Não é no índice, é na posição0
df_sample.iloc[0:5]
df_sample.iloc[[0,2,5]]

# %%
# No loc a gente acessa o índice

df_sample.loc[[234,148]]
