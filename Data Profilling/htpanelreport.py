import pandas as pd
from ydata_profiling import ProfileReport
import numpy as np

df=pd.read_csv('9Maydata.csv')
print(df)

profile=ProfileReport(df)
profile.to_file(output_file="9Mayreport.html")
