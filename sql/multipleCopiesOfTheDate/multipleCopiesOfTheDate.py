import pandas as pd
import datetime

df = pd.read_table(r'C:\Users\king\Desktop\multipleCopiesOfTheDate.sql', header=None)

begin = "2022-09-01"

for i in range(5):
    next_date = (pd.to_datetime(begin) + datetime.timedelta(i)).strftime('%Y-%m-%d');
    df.loc[:, 0] = str("('") + str(pd.to_datetime(next_date).strftime('%Y-%m-%d')) + str("',")
    # print(df)
    df.to_csv(next_date + ".sql", index=None,quotechar=' ',sep=" ")
