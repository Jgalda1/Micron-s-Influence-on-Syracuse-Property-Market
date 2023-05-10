import requests
import json
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

wgs84 = 4326
read = pd.read_csv("Real_Estate_Transactions_2022")
#
#  List of addresses to geocode
#

addresses = read[['Address','Municipality']]

addresses['merged'] = addresses['Address'] + ", " + addresses['Municipality'] + "," + " New York"
address = addresses['merged'].tolist()
#add merge municiplaity, NY
print(addresses)

#%%


output = []
api = "https://nominatim.openstreetmap.org/search"

#address = pd.read_csv("Real_Estate_Transactions2023-04-22.csv")



#fh = open('Copy of Real_Estate_Transactions_2023_edited.csv')

for a in address:

    #  Build the payload and make the query

    payload = { 'q':f'<{a}>', 'format':'json' }

    response = requests.get(api,payload)
    assert response.status_code == 200

    #  Parse the result

    result = response.json()

    #  Print it for reference

    print( json.dumps(result, indent=4) )

    #  Pull out the key information and append it to the list

    for r in result:
        newaddr = {
            'query':a,
            'name':r['display_name'],
            'lat':r['lat'],
            'lon':r['lon']
            }
        output.append(newaddr)

#%%
#
#  Build a dataframe and write it out
#

adds = pd.DataFrame(output)
adds.to_csv('lat_long2022.csv',index=False)


