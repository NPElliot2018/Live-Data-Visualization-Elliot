import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib as plt
import seaborn as sns

df=pd.read_csv("E:\Elliotsystems\Streamlit\MSEDCLCombine.csv")
sns.lineplot(df)
