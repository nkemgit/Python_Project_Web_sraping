### STEP_ONE
# import the libraries 

from bs4 import BeautifulSoup
import requests 
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_Nigeria"
# it means the request was successful and the server responded with the requested data.

requests.get(url) 
<Response [200]>
page = requests.get(url)
BeautifulSoup(page.text, "html") # return the text of the page
soup = BeautifulSoup(page.text, "html")
print(soup) 
soup.prettify # beautify the website for easy visualisation
soup.find_all("table", class_ = "wikitable sortable" )[0] # used index zero to select the targeted table out tables on the web


### STEP_TWO 
# use index of zero to pull the first table data on the page 
table = soup.find_all("table")[0] 
print(table)
table.find_all("th")
[<th>Rank
 </th>,
 <th>Company
 </th>,
 <th>Industry
 </th>,
 <th>Revenue<br/>(US$ millions)
 </th>,
 <th>Profits<br/>(US$ millions)
 </th>] ### Output


### STEP_THREE
# rename the table
Nigeria_titles = table.find_all("th")
print(Nigeria_titles)
[<th>Rank
</th>, <th>Company
</th>, <th>Industry
</th>, <th>Revenue<br/>(US$ millions)
</th>, <th>Profits<br/>(US$ millions)
</th>] #### output


### STEP_FOUR
# loop the titles data to obatain the individual data

Nigeria_table_tile = [title.text.strip() for title in Nigeria_titles]
print(Nigeria_table_tile)
['Rank', 'Company', 'Industry', 'Revenue(US$ millions)', 'Profits(US$ millions)']


# import pandas libary to pull the table tittle to data frame, pull  the extracted data to dataframe 'df'
import pandas as pd
df = pd.DataFrame(columns  = Nigeria_table_tile)
df
Rank	Company	Industry	Revenue(US$ millions)	Profits(US$ millions)
column_data = table.find_all("tr")
print(column_data)


### STEP_FIVE
# we loop through row data to obtain the individual data

for row in column_data[1:]:
    row_data = row.find_all("td")
    individual_row_data = [data.text.strip() for data in row_data]
    print( individual_row_data)
['1', 'Nigeria National Petroleum', 'Oil and gas', '9,706', '1,877']
['2', 'Nigeria Liquefied Natural Gas', 'Oil and gas', '6,315', '...']
['3', 'MTN Nigeria', 'Telecommunications', '3,514', '536']
['4', 'Dangote Cement', 'Cement', '2,699', '721']
['5', 'Nigerian Petroleum Development', 'Oil and gas', '2,686', '219']
['6', 'Flour Mills of Nigeria', 'Agroindustry', '2,014', '67']
['7', 'Airtel Nigeria', 'Telecommunications', '1,503', '343']
['8', 'Nigerian Breweries', 'Agroindustry', '890', '19']
['9', 'Jumia', 'Retail', '837', '...']
['10', 'Nestle Nigeria', 'Agroindustry', '749', '102']
['11', 'Krystal Digital Network Solutions', 'Infotech', '678', '21']
['12', 'Julius Berger', 'Construction', '631', '3']
['13', 'Nigerian Bottling Company', 'Agroindustry', '627', '...']
['14', 'Lafarge Africa', 'Cement', '602', '97']
['15', 'Dangote Sugar Refinery', 'Agroindustry', '559', '78']
['16', 'BUA Cement', 'Cement', '547', '184']
['17', 'TotalEnergies Nigeria', 'Oil and gas', '534', '5']
['18', 'Seplat Petroleum Development', 'Oil and gas', '498', '−80']
['19', 'Ardova Plc', 'Oil and gas', '474', '5']
['20', '11PLC', 'Oil and gas', '428', '16']
['21', 'International Breweries plc', 'Agroindustry', '357', '−32']
['22', 'Conoil', 'Oil and gas', '307', '...']
['23', 'Honeywell Flour Mill', 'Agroindustry', '286', '3']
['24', 'PZ Cussons Nigeria', 'Consumer goods', '216', '4']
['25', 'UAC of Nigeria', 'Conglomerate', '213', '11'] ##### output


###STEP_SIX
# we loop through the column data and attach each row of the individual data to the table 

for row in column_data[1:]:
    row_data = row.find_all("td")
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] =  individual_row_data
df 
Rank	Company	Industry	Revenue(US$ millions)	Profits(US$ millions)
0	1	Nigeria National Petroleum	Oil and gas	9,706	1,877
1	2	Nigeria Liquefied Natural Gas	Oil and gas	6,315	...
2	3	MTN Nigeria	Telecommunications	3,514	536
3	4	Dangote Cement	Cement	2,699	721
4	5	Nigerian Petroleum Development	Oil and gas	2,686	219
5	6	Flour Mills of Nigeria	Agroindustry	2,014	67
6	7	Airtel Nigeria	Telecommunications	1,503	343
7	8	Nigerian Breweries	Agroindustry	890	19
8	9	Jumia	Retail	837	...
9	10	Nestle Nigeria	Agroindustry	749	102
10	11	Krystal Digital Network Solutions	Infotech	678	21
11	12	Julius Berger	Construction	631	3
12	13	Nigerian Bottling Company	Agroindustry	627	...
13	14	Lafarge Africa	Cement	602	97
14	15	Dangote Sugar Refinery	Agroindustry	559	78
15	16	BUA Cement	Cement	547	184
16	17	TotalEnergies Nigeria	Oil and gas	534	5
17	18	Seplat Petroleum Development	Oil and gas	498	−80
18	19	Ardova Plc	Oil and gas	474	5
19	20	11PLC	Oil and gas	428	16
20	21	International Breweries plc	Agroindustry	357	−32
21	22	Conoil	Oil and gas	307	...
22	23	Honeywell Flour Mill	Agroindustry	286	3
23	24	PZ Cussons Nigeria	Consumer goods	216	4
24	25	UAC of Nigeria	Conglomerate	213	11
25	1	Nigeria National Petroleum	Oil and gas	9,706	1,877
26	2	Nigeria Liquefied Natural Gas	Oil and gas	6,315	...
27	3	MTN Nigeria	Telecommunications	3,514	536
28	4	Dangote Cement	Cement	2,699	721
29	5	Nigerian Petroleum Development	Oil and gas	2,686	219
30	6	Flour Mills of Nigeria	Agroindustry	2,014	67
31	7	Airtel Nigeria	Telecommunications	1,503	343
32	8	Nigerian Breweries	Agroindustry	890	19
33	9	Jumia	Retail	837	...
34	10	Nestle Nigeria	Agroindustry	749	102
35	11	Krystal Digital Network Solutions	Infotech	678	21
36	12	Julius Berger	Construction	631	3
37	13	Nigerian Bottling Company	Agroindustry	627	...
38	14	Lafarge Africa	Cement	602	97
39	15	Dangote Sugar Refinery	Agroindustry	559	78
40	16	BUA Cement	Cement	547	184
41	17	TotalEnergies Nigeria	Oil and gas	534	5
42	18	Seplat Petroleum Development	Oil and gas	498	−80
43	19	Ardova Plc	Oil and gas	474	5
44	20	11PLC	Oil and gas	428	16
45	21	International Breweries plc	Agroindustry	357	−32
46	22	Conoil	Oil and gas	307	...
47	23	Honeywell Flour Mill	Agroindustry	286	3
48	24	PZ Cussons Nigeria	Consumer goods	216	4
49	25	UAC of Nigeria	Conglomerate	213	11
# export the data frame to csv file for analysis

df.to_csv(r"C:\Users\HP\Desktop\My working directory\nkem companies.csv", index = Fals


## The final result is availavle for download  [https://tinyurl.com/2jb5tujr]
## The second stage of the project is to perform data cleaning/manipulation in python for data analysis