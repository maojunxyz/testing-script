import pandas as pd
import datetime

data = pd.read_csv(r'C:\Users\king\Desktop\multipleCopiesOfTheDate.csv')
data['settle_date'] = pd.to_datetime(data['settle_date'])

for i in range(5):
    next_date = data['settle_date'][0] + datetime.timedelta(1)
    data['settle_date'] = next_date
    data.to_csv(next_date.strftime('%Y-%m-%d') + ".csv", index=None)
