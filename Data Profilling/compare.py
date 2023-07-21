import pandas as pd
from ydata_profiling import ProfileReport
import numpy as np

df1=pd.read_csv('23Jundata.csv')
df2=pd.read_csv('24Jundata.csv')

profile1=ProfileReport(df1,title="23rd June")
profile2=ProfileReport(df2,title="24th June")
comparison_report=profile1.compare(profile2)
comparison_report.to_file("compare23vs24.html")

