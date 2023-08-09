# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv("../data/produto.csv")
df

# %%
df["precoAjustado"] = df["vlPreco"] * 1.09

# arredondar
df["precoAjustado"] = df["precoAjustado"].round(2)
df["precoAjustado"] = (df["vlPreco"] * 1.09).round(2)

# %%

df["txAjuste(%)"] = (100 * (df["precoAjustado"] / df["vlPreco"] - 1)).round(2)
df

# %%
df = df.drop(columns=["txAjuste"])
df

# %%
del df["txAjuste(%)"]
df

# %%

# Utilizando numpy para aplicar logarítmo em todos os valores dentro da Series
df["logTxAjuste"] = np.log(df['txAjuste(%)'])
df

# %%

# Exponencial

df["expTxAjuste"] = np.exp(df['txAjuste(%)'])
df

# %%

def fatorial(x):
    total = 1
    for i in range(2,int(x)+1):
        total *= i
    return total

# %%
df["precoAjustado"].apply(fatorial)