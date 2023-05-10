# Micron-s-Influence-on-Syracuse-Property-Market
Introduction

This project analyzes Micron's impact on Syracuse's real estate prices. By studying prices before and after the announcement of a $20B chip plant, we can evaluate if residential real estate prices in Syracuse can lead to higher prices and cause the possibility of homes becoming unaffordable for low income renters. 

Purpose of Repository

This repository was built to locate the addresses purchased in 2022 from 1/1/2022-12/31/22  and 1/1/2023-3/31/23  in Onondaga County.  The raw data can be retrieved from the Central New York Real Estate Transactions Database. Download as CSV. https://www.syracuse.com/realestate/transactions/ 
County: Onondaga, Municipality: All municipalities, School district: Leave Empty, Buyer's name: Leave Empty, Property type: Resident (Residential)


Input_Data File 
The files used to geocode 2023 and 2022  addresses. 

Script 

There are two scripts  built to geocode 2022 and 2023 separately using the files in Input_Data File. The column in merged is made to list and match the addresses found can be matched into a list and it would not be difficult to later drop addresses that are counted more than once in the new data frame.  
The 2023_Join and 2022_Join scripts are  made to drop any repeated addresses that are geolocated around a property and are counted as more than once because it is locating different locations within that property. 
Sales_Prices_2022_2023 finds the mean of each data frame for 2022 and 2023 and compares them through a boxplot figure.  

Output_Data File

Lat_long files are the output for the geocoded addresses. They are then joined with price files to create 2022_Final and 2023_Final files to include variables merges, lat, long, Address, Municipality and Sale price.

2022_Final and 2023_Final CSVs are then inputted in Arc Pro to create two maps.
ArcGIS Pro
15 mile Buffer (UTM 18N)
Digitized Micron Site (UTM 18N)
Census Tract Clipping for Onondaga County (UTM 18N)
Spatial Join (UTM 18N)
Symbology: Graduated Colors- Natural Breaks Method

Main Findings 

2022 has a ratio of 346/439 = 79%
2023 has a ratio of 406/443 = 91%
According to my findings, there are more residential houses being sold in Onondaga County and it is likely due to Micron.  
![prices](https://github.com/Jgalda1/Micron-s-Influence-on-Syracuse-Property-Market/assets/123008395/f1f9ccc2-e42f-435e-8759-575bd75c717f) 
<img width="384" alt="Map_2023" src="https://github.com/Jgalda1/Micron-s-Influence-on-Syracuse-Property-Market/assets/123008395/44aa7c73-6f35-4b1f-84ff-11ba32cb3b41">
<img width="376" alt="Map_2022" src="https://github.com/Jgalda1/Micron-s-Influence-on-Syracuse-Property-Market/assets/123008395/29b6523a-5ab0-414a-8a8a-b64f5628c250">
<img width="778" alt="Distribution of Sale Prices 2022" src="https://github.com/Jgalda1/Micron-s-Influence-on-Syracuse-Property-Market/assets/123008395/764cae21-3070-40f3-98e1-a8ca1144aae2">

In ArcGIS, I located the precise area where Micron is planned to be situated and digitized a polygon for that region. I chose to use a polygon instead of a point to provide a better understanding of the size and boundaries of the area in question.
Next, I decided to use census tracts rather than zip codes to analyze the data because they are larger in size and provide a more detailed overview of the population. I obtained the census data and then clipped it to fit the Onondaga County region. Since the original data contained census tracts from across the states, I further clipped the census tract data to view only the census tracts within Onondaga County. To ensure consistency in the data, I set the projected coordinate system for all data to NAD 1983 UTM Zone 18N because I am working with data in New York.
After setting up the data, I conducted a spatial join for the buffer on the census tract and added my data containing Sale Price for each residential address made in 2022 and 2023. Upon analyzing the sale prices, I discovered that many of the address points for 2022 were located outside the 15-mile buffer I created from the Micron site. In contrast, the prices for 2023 were concentrated within Onondaga County. 
Fig. 4


Fig. 4 is the first map I conducted after the spatial analysis, buffer, and polygon digitization. The selected points in the buffer are addresses that are within the 15 mile radius for 2023. Upon examining the map,  it became evident that there were more data points outside of Onondaga County in 2022 than in 2023. This observation supports my hypothesis that there may be more houses being sold inside the buffer due to the proximity to Micron. Initially, I attempted to conduct a spatial join on the census tract with home sellers as the join feature for both 2022 and 2023 data. However, I encountered several issues with numerous variables showing up. To fix this issue I deleted the variables I did not need to get. I learned that I would get a polygon from conducting this operation, and not point data and this is because the spatial join will count each point within each census block. This was what I was looking for but my first error occurred when I tried to use homesales and the join features as the census tract. This would produce point data and would not be useful in comparing the amount of homesales between 2022 and 2023. 
I then began to think about what I could do to represent the difference spatial distribution from 2022 to 2022 residential home sales to see if home sales are getting closer to the Micron site. Another tactic I could have done and did not is to show the price change on a map. I instead use box plots because I was unsure how I could do it on the map. Now, looking back it may have been a good idea to do the sale prices as raster data on a map because I could use the prices as interval data. After the spatial joins I used the categorized  option for symbology for the darker colors to highlight the more addresses within that census tract. 


The analysis shows that the 2023 map has more red shaded areas within the buffer compared to the 2022 map. Specifically, there are 4 census tracts that are red in the buffer in 2023, while there were 6 in 2022. The darker colors, such as red, signify that there were more residential property sales in that census tract. Additionally, it is worth noting that the 2023 map has more yellow at the bottom of Onondaga County, while the 2022 map has more orange and dark orange. This suggests that there are more properties being sold in the southern part of Onondaga County, likely because it is further from the Micron site.
However, the census tracts next to the Micron site are lighter yellow in 2023 than in 2022, which contradicts the hypothesis that the Micron site is driving property sales. In fact, the results suggest that there are more housing sales happening near the Micron site in 2023 than in 2022, with a ratio of 91% compared to 79% within the 15-mile buffer. Moreover, Syracuse appears yellow in 2022, with surrounding areas also yellow, while in 2023, most of Syracuse is still yellow, but there is red on the outskirts.
It is important to note that the analysis included all of Onondaga County to allow for comparisons between cities and Syracuse. However, to better understand the effects of Micron on a deeper level in Syracuse, further analysis of non-residential property prices would be necessary to determine if there is an increase and if it is attributable to Micron.
In conclusion, while the results provide some insights into the changes in residential property sales in Onondaga County between 2022 and 2023, further analysis is necessary to gain a more comprehensive understanding of the underlying trends and their potential causes. By conducting additional research on non-residential property prices and other relevant factors, policymakers and researchers can gain a better understanding of how the Micron site may impact the housing market in Syracuse and the surrounding areas.



  


