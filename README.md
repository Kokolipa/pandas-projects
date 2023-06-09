# Retail Sales Analysis
This retail sales dataset was merged from a folder that contained the sales for twelve consecutive months in 2019. 
- Dataset size: 186,850
- Libraries used: Pandas, ydata_profiling, numpy, matplotlib, seaborn, os, itertools, and collections. 

### Outlining the analysis process
1. Dataset creation: Merging all CSV files (data integration).  
2. Data cleansing
3. Memory optimisation & data transformation 
4. Adding additional (necessary) columns for analysis and clarity 
5. Quick analysis - Pandas-profiling
6. Analysis

### Additional Methods Implemented
1. Formatting table output with HTML 

#### Folder structure
----
``` yml
.
├── Pandas - Project
│   ├── Sales_Data                    # This was the raw data before it was merged into one dataset
│   │   ├── Sales_April_2019.csv      # These are all the CSV documents
│   │   ├── Sales_August_2019.csv...  
│   └── ...                    
|   ├── Output                        # This folder contains the merged dataset
│   |   ├── dataset.csv                               
│   └── ...       
|   ├── SalesAnalysis                 # This folder contains the analysis and the HTML output from pandas_profiling
│   |   ├── Analysis.ipynb
│   |   ├── updated_sales_report.html                               
│   └── ...                     
|              
|___README.md
``` 




