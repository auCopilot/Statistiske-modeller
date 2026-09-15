import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as sm
import seaborn as sns


# Read CSV Anorexia
df = pd.read_csv("anorexia.csv")
print(df.head())

for treatment in df["Treat"].unique():
    subset = df[df["Treat"] == treatment]

    plt.scatter(
        subset["Prewt"],
        subset["Postwt"],
        s=50,
        label=treatment
    )

plt.xlabel("Pre-treatment weight")
plt.ylabel("Post-treatment weight")
plt.legend(title="Treatment")
plt.show()

# Plot differences according to treatment
df["Diff"] = df["Postwt"] - df["Prewt"]

sns.boxplot(x="Treat", y="Diff", data=df)
plt.show()

model = sm.ols("Postwt ~ Prewt * C(Treat)", data=df).fit()
print(model.summary())