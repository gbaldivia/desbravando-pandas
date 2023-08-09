# %%
import pandas as pd

# %%
df = pd.read_csv("../data/pedido.csv")
df
# %%

## Maneira 1
df = df.rename(columns={"descUF": "UF"})
df
# %%

# Alterando o próprio dataframe, não existe retorno

df.rename(columns={"UF": "descUF"}, inplace=True)