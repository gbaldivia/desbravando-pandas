# %%
import pandas as pd

# %%

df = pd.read_csv("../data/pedido.csv")

df

# %%

df.columns

# %%

df.shape

# %%
df.index

# %%
df.info(memory_usage='deep')

# %%

tipos_colunas = df.dtypes
tipos_colunas

# %%

df.head()
df.head(10)

# %%
df.tail()

# %%

df.sample(5)