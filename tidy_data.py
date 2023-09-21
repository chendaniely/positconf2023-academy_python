import pandas as pd

## billboard: values in columns -----

billboard = pd.read_csv("data/tidy/billboard.csv")
billboard

# get a vector of just the column names based on a pattern
# we talked about the .str. accessor later in the workshop
billboard.columns[billboard.columns.str.contains("wk")]

# using filter will return a full dataframe first, before you just get the column names
billboard.filter(like="wk").columns

billboard_long = billboard.melt(
  id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
  var_name="week",
  value_name="rating"
)
billboard_long

## ebola multiple bits of info per cell -----

ebola = pd.read_csv("data/tidy/country_timeseries.csv")
ebola

ebola_long = ebola.melt(
  id_vars=["Date", "Day"]
)
ebola_long

# string methods

"Deaths_Mali".split("_")
ebola_long.info()
ebola_long.dtypes

# documentation on accessors are under pandas Series objects
# .dt.
# .cat.
ebola_long["variable"].str.split("_")

ebola_long["case_death"] = ebola_long["variable"].str.split("_").str.get(0)
ebola_long["country"] = ebola_long["variable"].str.split("_").str.get(1)
ebola_long

## ebola values in rows and columns

ebola_long.pivot_table(
  index=["Date", "Day", "country"],
  columns="case_death",
  values="value"
).reset_index()
