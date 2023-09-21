import pandas as pd

# functions groupby apply
j2sr = pd.read_csv("data/j2sr/j2sr.csv")

health_change = (
  j2sr
  .loc[j2sr["year"].isin([2014, 2020])]
  .groupby("country")
  ["child_health"]
  .apply(lambda g: g.iloc[-1] - g.iloc[0])
  .reset_index()
  .rename(columns={"child_health": "child_health_change"})
)
