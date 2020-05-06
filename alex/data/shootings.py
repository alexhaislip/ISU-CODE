import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv('pah_wikp_combo.csv')
clean = df.filter(["Date", "City", "School", "Fatalities","Wounded"])

largest_deaths = clean.nlargest(1, ['Fatalities'])
# print(largest_deaths)

# Date format: a certain way of writing a date
current_date_format = '%m/%d/%y'

# Example date: just a test
str_date = "4/16/07"

# Creating a datetime object using the test and our format
date = datetime.strptime(str_date, current_date_format)

# printing the date
print(date.year)

clean['Year'] = df["Date"].apply(lambda x: datetime.strptime(x,current_date_format).year)

year_group = clean.groupby(["Year"])

yearly_stats = year_group.sum()

#x axis will be the years,y amout of fatatalities ranked highest to lowest
yearly_stats.plot()
plt.savefig('fig.pdf')



# ts = row[1]
# ts = datetime.strptime(ts, '%Y-%m-%dT%H:%MZ').strftime("%m/%d/%Y")
# if ts != "":
#     row[17] = ts # this is what you miss
#     writer.writerow(row)