import pandas as pd

lat_long = pd.read_csv('lat_long2022.csv')
price = pd.read_csv('price_2022.csv')
#select the unique names in the first colum, then copy the price column from the original 

lat_long_new = lat_long.drop_duplicates(['query'])
lat_long_new = lat_long_new.rename(columns={"query":"merged"})
out = pd.merge(lat_long_new, price, on = 'merged', how = 'inner')
out = out[out['Sale price'] != 0] 
out = out[out['Sale price'] != 1] 

out.to_csv("2022_Final.csv", index=False)
