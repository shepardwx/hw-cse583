import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# 1. READING CSV
df_bicycle=pd.read_csv('bicycle_data.csv')
df_bicycle.rename(columns={'Fremont Bridge Sidewalks, south of N 34th St Total': 'total',
                           'Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk': 'west',
                           'Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk': 'east'}, inplace=True)




# 2. COMMENT ON COLUMNS
"""
df_bicycle columns
==================
Date            :       str, current date with hourly resolution

total           :       float, total cyclists who crossed the Fremont Bridge Sidewalks, south of N 34th St in the previous hour

west            :       float, cyclists who crossed Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk in the previous hour

east            :       float, cyclists who crossed Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk in the previous hour
"""



# 3. NEW COLUMNS

# TOTAL: already have a column with total?

# HOUR
df_bicycle['hour']=df_bicycle['Date'].str[-11:]

# YEAR
df_bicycle['year']=df_bicycle['Date'].str[6:10]



# 4. DF WITH 2016 DATA
df_bicycle_2016 = df_bicycle[df_bicycle['year']=='2016']



# 5. Only NaN value is at 03/13/2016 02:00:00 AM. I will use nanmax/nanmin in data analysis to prevent trouble.
idx_nan=np.where(np.isnan(df_bicycle_2016['total'].values))
# for i in idx_nan:
    # print(df_bicycle_2016['Date'].values[i])

# 1 point of missing data



# 6. PLOTTING TOTAL RIDERS AS A FUNCTION OF HOUR
x=np.unique(df_bicycle_2016['hour'])


hourly = df_bicycle_2016.groupby("hour")["total"].sum()
order = pd.to_datetime(hourly.index, format="%I:%M:%S %p").argsort()
hourly = hourly.iloc[order]

plt.plot(x[order],hourly)

plt.xticks(rotation=45)

plt.xlabel('Hour of day')
plt.ylabel('Total cyclists')
plt.title('Total cyclists as a function of hour, 2016')

plt.savefig('counts_by_hour.png')

plt.tight_layout()

plt.close()
# plt.show()



# 7. BUSIEST HOUR

busiest_hour=x[order][np.argmax(hourly)]
print(busiest_hour)

# BUSIEST HOUR IS 5PM



# 8. EDITED README.MD