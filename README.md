# Micron-s-Influence-on-Syracuse-Property-Market
Introduction

This project analyzes Micron's impact on Syracuse's real estate prices. By studying prices before and after the announcement of a $20B chip plant, we can evaluate if residential real estate prices in Syracuse can lead to higher prices and cause the possibility of homes becoming unaffordable for low income renters. 

Purpose of Repository

This repository was built to locate the addresses purchased in 2022 from 1/1/2022-12/31/22  and 1/1/2023-3/31/23  in Onondaga County.  The raw data can be retrieved from the Central New York Real Estate Transactions Database. Download as CSV. https://www.syracuse.com/realestate/transactions/ 
County: Onondaga, Municipality: All municipalities, School district: Leave Empty, Buyer's name: Leave Empty, Property type: Resident (Residential)

Structure and Use of Repository Files

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



  


