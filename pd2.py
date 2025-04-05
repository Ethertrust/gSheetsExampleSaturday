from cProfile import label

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 2000)
pd.set_option('display.max_rows', 2000)

df = pd.read_csv('Data_for_pandas/Fishing.csv')
#print(df)
# Можно ли сказать, что люди с более низким доходом и выбравшие более дешёвый тип рыбалки, в целом,
# предпочитают один тип рыбалки, а люди с более высоким доходом и более дорогой рыбалкой – другой?
print(df["income"].max())
# Null
#print(df.isnull().values.any())
# 1. Проверить данные на целостность (Проверить на наличие Null значений)
# 2. Категоризировать все записи на людей с высоким и не высоким: высокий, не высокий (средний и низкий)
# 3. Категоризировать все записи по расходам: высокие, средние и низкие расходы.
# 4. Сравнить между собой все группы людей:
#    - исходя из режима рыбалки
#    - исходя из аггрегированных характеристик: количество, сумма расходов, средние расходы, средние доходы, посмотреть на разницу между средними и медианными расходами/доходами
# 5. Сделать выводы

print(df.sort_values(["income","price"]))
# print(df)
print(df.describe().loc[:,["price", "income"]])
print(df["income"].median())
print(df["income"].mean())
print("mean-median", df["income"].mean() - df["income"].median(), ((df["income"].mean() - df["income"].median())/df["income"].max())*100)

df["class"] = pd.cut(df["income"], np.array([0, 0.1, 0.4, 1])*df["income"].max(), labels = ["low", "middle", "rich"])
df["expenses"] = pd.cut(df["price"], 3, labels = ["low", "middle", "high"])
print(df.loc[:,["mode", "price", "income", "class", "expenses"]])
rich = df["class"] == 'rich'
df_rich = df[rich].loc[:,["mode", "price", "income", "class", "expenses"]]
print(df_rich)
print(df_rich.describe())
grp_rich = df_rich.groupby("mode")
print(grp_rich.agg({"price":["count","sum","mean","median"], "income":["count","sum","mean","median"]}))
def agg_approve(x):
    return x.mean() - x.median()
def first_reserach(df, title: str):
    print("--------------------", title)
    grp_rich = df.groupby("mode")
    print(grp_rich.agg({"price": ["count", "sum", "mean", "median", agg_approve], "income": ["count", "sum", "mean", "median", agg_approve]}))
    print("Общее количество", df["price"].count())
first_reserach(df_rich, "Богатые")
rich_high_exp = (df["class"] == 'rich') & (df["expenses"] == 'high')
rich_not_high_exp = (df["class"] == 'rich') & ((df["expenses"] == 'low') | (df["expenses"] == 'middle'))
rich_not_high_exp2 = (df["class"] == 'rich') & (~(df["expenses"] == 'high'))
df_rich_high_exp = df[rich_high_exp]
df_rich_not_high_exp = df[rich_not_high_exp]
first_reserach(df_rich_high_exp, "Богатые с высокими расходами")
first_reserach(df_rich_not_high_exp, "Богатые с невысокими расходами")

df_not_rich = df[(~(df["class"] == 'rich'))]
#print(df_not_rich)
df_not_rich_high_exp = df[(~(df["class"] == 'rich')) & (df["expenses"] == 'high')]
df_not_rich_not_high_exp = df[(~(df["class"] == 'rich')) & (~(df["expenses"] == 'high'))]
first_reserach(df_not_rich, "Не Богатые")
first_reserach(df_not_rich_high_exp, "Не Богатые с высокими расходами")
first_reserach(df_not_rich_not_high_exp, "Не Богатые с не высокими расходами")
df_not_rich_low_exp = df[(~(df["class"] == 'rich')) & (df["expenses"] == 'low')]
df_not_rich_middle_exp = df[(~(df["class"] == 'rich')) & (df["expenses"] == 'middle')]
first_reserach(df_not_rich_low_exp, "Не Богатые с низкими расходами")
first_reserach(df_not_rich_middle_exp, "Не Богатые с средними расходами")
df_low_income = df[(df["class"] == 'low')]
df_low_income_not_high_exp = df[(df["class"] == 'low') & (~(df["expenses"] == 'high'))]
# df_low_income_not_high_exp2 = df[(~(df["class"] == 'rich')) & ((df["expenses"] == 'middle')|(df["expenses"] == 'low'))]
first_reserach(df_low_income,"Низкие доходы" )
first_reserach(df_low_income_not_high_exp,"Низкие доходы с не высокими расходами" )
df_rich.plot(kind="bar")
plt.show()
# first_reserach(df_low_income_not_high_exp2,"Низкие доходы с не высокими расходами" )
