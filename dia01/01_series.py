# %%
import pandas as pd

# %%
## Lista
idade = [31, 35, 40, 17, 15, 8, 60, 65, 23]
idade

# %%

# Isso é uma lista!
idade = [31, 33, 2, 15, 17, 98, 65, 43]

media = sum(idade)/len(idade)
media

# %%
s_idade = pd.Series(idade)
s_idade

# %%

# Métodos das Séries
media = s_idade.mean()
media

variancia = s_idade.var()
variancia

des_pad = s_idade.std()
des_pad

s_idade.describe()

# %%
# Idade maior do que 30 anos com Python

nova_idade = []
for i in idade:
    if i >= 30:
        nova_idade.append(i)

nova_idade = [i for i in idade if i >= 30]7

nova_idade

# %%

filtro = s_idade >= 30
s_idade[filtro] 