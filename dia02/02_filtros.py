# %%

import pandas as pd


# %%
df = pd.read_csv("../data/pedido.csv")
df

# %%

idade = [20, 15, 17, 50, 32, 19, 92]

# Filtrar idade em Python:
idade_20 = []
for i in idade:
    if i>20:
        idade_20.append(i)  

idade_20

# Filtrar idade usando séries:
idade = pd.Series([20, 15, 17, 50, 32, 19, 92])
filtro = idade >= 20
idade[filtro]

#Criando variável de filtro:
idade[idade >= 20]

# %%

# Com base no que vimos agora: como pegar apenas estado de SP?
filtro_uf = df['descUF'] == 'São Paulo'

df[filtro_uf]

# Ou mais direto:
df[df['descUF'] == 'São Paulo']

# %%

# É de São Paulo e pediu Ketchup:
filtro_sp_ketchup = (df['descUF'] == "São Paulo") & (df['flKetchup'])
df[filtro_sp_ketchup]

# %%

# Estado de SP, RJ e PR que pediram Ketchup
filtro_ufs_ketchup = ((df['descUF'] == "São Paulo") | (df['descUF'] == "Rio de Janeiro") | (df['descUF'] == "Paraná")) & (df['flKetchup'])
df[filtro_ufs_ketchup]["descUF"].unique()
df[filtro_ufs_ketchup]

# Forma mais direta de fazer:
uf_recortes = ['São Paulo', 'Rio de Janeiro', 'Paraná']
filtro_ketchup = df['descUF'].isin(uf_recortes) & df["flKetchup"]
df[filtro_ketchup]

# %%

# Não deixou recado:
filtro_txt_na = df['txtRecado'].isna()
df[filtro_txt_na]

# %%

