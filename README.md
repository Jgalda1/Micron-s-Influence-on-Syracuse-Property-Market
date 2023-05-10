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
<img width="758" alt="Distribution of Sale Price for 2023 by Municipality" src="https://github.com/Jgalda1/Micron-s-Influence-on-Syracuse-Property-Market/assets/123008395/3fce1d8f-9e33-4c5b-a0f1-4dcf5fad868f">


In ArcGIS, I located the precise area where Micron is planned to be situated and digitized a polygon for that region. I chose to use a polygon instead of a point to provide a better understanding of the size and boundaries of the area in question.
Next, I decided to use census tracts rather than zip codes to analyze the data because they are larger in size and provide a more detailed overview of the population. I obtained the census data and then clipped it to fit the Onondaga County region. Since the original data contained census tracts from across the states, I further clipped the census tract data to view only the census tracts within Onondaga County. To ensure consistency in the data, I set the projected coordinate system for all data to NAD 1983 UTM Zone 18N because I am working with data in New York.
After setting up the data, I conducted a spatial join for the buffer on the census tract and added my data containing Sale Price for each residential address made in 2022 and 2023. Upon analyzing the sale prices, I discovered that many of the address points for 2022 were located outside the 15-mile buffer I created from the Micron site. In contrast, the prices for 2023 were concentrated within Onondaga County. The boxplots were made using ArcGIS using Sale Price and Municipality as the X and Y axis. 



Summary

The analysis shows that the 2023 map has more red shaded areas within the buffer compared to the 2022 map. Specifically, there are 4 census tracts that are red in the buffer in 2023, while there were 6 in 2022. The darker colors, such as red, signify that there were more residential property sales in that census tract. Additionally, it is worth noting that the 2023 map has more yellow at the bottom of Onondaga County, while the 2022 map has more orange and dark orange. This suggests that there are more properties being sold in the southern part of Onondaga County, likely because it is further from the Micron site.
However, the census tracts next to the Micron site are lighter yellow in 2023 than in 2022, which contradicts the hypothesis that the Micron site is driving property sales. In fact, the results suggest that there are more housing sales happening near the Micron site in 2023 than in 2022, with a ratio of 91% compared to 79% within the 15-mile buffer. Moreover, Syracuse appears yellow in 2022, with surrounding areas also yellow, while in 2023, most of Syracuse is still yellow, but there is red on the outskirts.
It is important to note that the analysis included all of Onondaga County to allow for comparisons between cities and Syracuse. However, to better understand the effects of Micron on a deeper level in Syracuse, further analysis of non-residential property prices would be necessary to determine if there is an increase and if it is attributable to Micron.
In conclusion, while the results provide some insights into the changes in residential property sales in Onondaga County between 2022 and 2023, further analysis is necessary to gain a more comprehensive understanding of the underlying trends and their potential causes. By conducting additional research on non-residential property prices and other relevant factors, policymakers and researchers can gain a better understanding of how the Micron site may impact the housing market in Syracuse and the surrounding areas.



  


