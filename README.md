## Microns Influence on Syracuse Property Market
##Introduction

This project analyzes Micron's impact on Syracuse's real estate prices. By studying prices before and after the announcement of a $20B chip plant, we can evaluate if residential real estate prices in Syracuse can lead to higher prices and cause the possibility of homes becoming unaffordable for low income renters. My hypothesis also implies that there will be workers such as engineers living outside of Syracuse area that will move in to work at Micron. 

Purpose of Repository

This repository was built to locate the addresses purchased in 2022 from 1/1/2022-12/31/22  and 1/1/2023-3/31/23  in Onondaga County.  The raw data can be retrieved from the Central New York Real Estate Transactions Database. Download as CSV. https://www.syracuse.com/realestate/transactions/ 
County: Onondaga, Municipality: All municipalities, School district: Leave Empty, Buyer's name: Leave Empty, Property type: Resident (Residential)



##A.	Input_Data File 

The files used to geocode 2023 and 2022 addresses. 


##B. Python Scripts 

There are two scripts built to geocode 2022 and 2023 addresses separately using the files in Input_Data File. Each address represents a sale made. The addresses listed as sold for $0 or $1 were dropped. The column in merged is made to list and match the addresses found in the new data frame.  
The 2023_Join and 2022_Join scripts are made to drop any repeated addresses that are geolocated around a property and are counted as more than once because it is locating different locations within that property. 
Sales_Prices_2022_2023 finds the mean of each data frame for 2022 and 2023 and compares them through a boxplot figure.  

 Output_Data File

Lat_long files are the output for the geocoded addresses. They are then joined with price files to create 2022_Final and 2023_Final files to include variables merges, latitude, longitude, Address, Municipality and Sale price.

2022_Final and 2023_Final CSVs are then inputted in Arc Pro to create two maps.

##C. ArcGIS Pro

Both 2022 and 2023 maps include:
•	15-mile Buffer (UTM 18N)

•	Digitized Micron Site (UTM 18N)

•	Census Tract Clipping for Onondaga County (UTM 18N) https://www.census.gov/geographies/mapping-files/time-series/geo/cartographic-boundary.html

•	Spatial Join (UTM 18N)

•	Symbology: Graduated Colors- Natural Breaks Method

In ArcGIS, I located the precise area where Micron is planned to be situated and digitized a polygon for that region. I chose to use a polygon instead of a point to provide a better understanding of the size and boundaries of the area.
Next, I decided to use census tracts rather than zip codes to analyze the data because they are larger in size and provide a more detailed overview of the population. I obtained the census data and then clipped it to fit the Onondaga County region. Since the original data contained census tracts from across the states, I further clipped the census tract data to view only the census tracts within Onondaga County. To ensure consistency in the data, I set the projected coordinate system for all data to NAD 1983 UTM Zone 18N because I am working with data in New York. The 15 mile buffer is made as a preidction that employees for Micron will not want to commute more than 15 miles to work.
After setting up the data, I conducted a spatial join for the buffer on the census tract and added my data containing Sale Price for each residential address made in 2022 and 2023.The boxplots were made using ArcGIS using Sale Price and Municipality as the X and Y axis. 


Main Findings 

2022 has a ratio of 346/439 = 79%
2023 has a ratio of 406/443 = 91%
According to my findings, there are more residential houses being sold in Onondaga County and it is likely due to Micron.  
![prices](https://github.com/Jgalda1/Micron-s-Influence-on-Syracuse-Property-Market/assets/123008395/f1f9ccc2-e42f-435e-8759-575bd75c717f) 
Here is a boxplot representing 2023 and 2022 mean sale prices in Onondaga County. 
#Map 2023
<img width="384" alt="Map_2023" src="https://github.com/Jgalda1/Micron-s-Influence-on-Syracuse-Property-Market/assets/123008395/44aa7c73-6f35-4b1f-84ff-11ba32cb3b41">

#Map 2022
<img width="376" alt="Map_2022" src="https://github.com/Jgalda1/Micron-s-Influence-on-Syracuse-Property-Market/assets/123008395/29b6523a-5ab0-414a-8a8a-b64f5628c250">
This map shows more sales took place outside the 15 mile buffer than in the 2023 map. 

Each point on both maps represent a sale of a residential property within that specific year in Onondaga County. The darker the color, the more property sales were made within that census tract.   


#Sale Prices by Municipality
<img width="778" alt="Distribution of Sale Prices 2022" src="https://github.com/Jgalda1/Micron-s-Influence-on-Syracuse-Property-Market/assets/123008395/764cae21-3070-40f3-98e1-a8ca1144aae2">
<img width="758" alt="Distribution of Sale Price for 2023 by Municipality" src="https://github.com/Jgalda1/Micron-s-Influence-on-Syracuse-Property-Market/assets/123008395/3fce1d8f-9e33-4c5b-a0f1-4dcf5fad868f">



Results

It is important to note that the analysis included all of Onondaga County to allow for comparisons between cities and Syracuse. 
In conclusion, while the results provide some insights into the changes in residential property sales in Onondaga County between 2022 and 2023, further analysis is necessary to gain a more comprehensive understanding of the underlying trends and their potential causes. By conducting additional research on non-residential property prices and other relevant factors such as the COVID-19, policymakers and researchers can gain a better understanding of how the Micron site may impact the housing market in and chance of homeownership for renters in Syracuse. 




  


