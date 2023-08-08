# %%
import pandas as pd

# %%
data = {
    "name":['Téo', 'Nah', 'Maria', 'José', 'Marina', 'Jess', 'InfoSlack'],
    "idade":[30, 33, 2, 45, 65, 43, 40],
    "cor":["Preto", "Verde", "Azul", "Vermelho", "Amarelo", "Verde", "Azul"],
    "renda":[3500, 1350, 0, 6780, 4150, 5500, 10750]
}

data["idade"]

# %%

df = pd.DataFrame(data)

df["idade"]

# %%

type(df["idade"])

# %%

df[['idade', 'renda']].mean()