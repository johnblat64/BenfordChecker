# Benford Checker


## INFO
Checks a csv file and calculates percentages of leading digits (1-9) within a specified column. Can be used to check against benford's law to determine if the dataset aligns with it.
https://en.wikipedia.org/wiki/Benford%27s_law

## Instructions

- Install Python3
- Run python3 ./benford.py <name-of-file.csv> <column-name>
- The program will print out a bar chart and command line output
- For now, analyze the results yourself to see if it matches benford's law 
- If the program throws an error during reading the csv file, it might be a different encoding than the default iso-8859-1. Supply an extra command line argument specifying the encoding of your file if it's different than the default
## Example
- An example csv file is included in this repo for populations based on US counties
- python3 ./bf-checker.py co-est2019-alldata.csv CENSUS2010POP
- The above command will print a chart based on the leading digits in census 2010 populations for each county
