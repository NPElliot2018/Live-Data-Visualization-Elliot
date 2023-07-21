"""import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df=pd.read_csv("E:\Elliotsystems\Quicksights\Csv files\HT Panel\9May,2023.csv")

st.set_page_config(
    page_title='Real Time Dashboard for HTPanel',
    page_icon='👌',
    layout='wide'
)

st.title("Real-TimeDahboard for HT-Panel")

parameter_filter=st.selectbox("select the parameter",pd.unique(df['Parameters']))

placeholder=st.empty()

df=df[df['Parameters']==parameter_filter]
for seconds in range(200):
    df['avgVol']=df['Avg Voltage']*np.random.choice(range(1,5))
    df['avgPF']=df['Avg PF']*np.random.choice(range(1,5))
    df['avgCur']=df['Avg Current']*np.random.choice(range(1,5))
    df['TotalActivePower']=df['Total Active power']*np.random.choice(range(1,5))
    df['TotalReactivePower']=df['Total Reactive power']*np.random.choice(range(1,5))
    df['TotalApparentPower']=df['Total Apparent power']*np.random.choice(range(1,5))
    df['THDVolL1']=df['THD Voltage L1']*np.random.choice(range(1,5))
    df['THDVolL2']=df['THD Voltage L2']*np.random.choice(range(1,5))
    df['THDVolL3']=df['THD Voltage L3']*np.random.choice(range(1,5))
    df['THDCurL1']=df['THD Current L1']*np.random.choice(range(1,5))
    df['THDCurL2']=df['THD Current L2']*np.random.choice(range(1,5))
    df['THDCurL3']=df['THD Current L3']*np.random.choice(range(1,5))
    df['ImpMWh']=df['Import MWh']*np.random.choice(range(1,5))
    df['ImpMVAh']=df['Import MVAh']*np.random.choice(range(1,5))
    df['Time']=pd.to_datetime(df['Time'])



    avgvol=np.mean(df['avgVol'])
    avgPF=np.mean(df['avgPF'])
    avgCur=np.mean(df['avgCur'])
    TotalActivePower=np.mean(df['TotalActivePower'])
    TotalReactivePower=np.mean(df['TotalReactivePower'])
    TotalApparentPower=np.mean(df['TotalApparentPower'])
    THDVolL1=np.mean(df['THDVolL1'])
    THDVolL2=np.mean(df['THDVolL2'])
    THDVolL3=np.mean(df['THDVolL3'])
    THDCurL1=np.mean(df['THDCurL1'])
    THDCurL2=np.mean(df['THDCurL2'])
    THDCurL3=np.mean(df['THDCurL3'])
    ImpMWh=np.mean(df['ImpMWh'])
    ImpMVAh=np.mean(df['ImpMVAh'])
    Time=df['Time']
    current_time=time.time()
    formatted_time = time.strftime("%H:%M:%S", time.localtime(current_time))
    value = str(Time.iloc[0])


    with placeholder.container():
        kpi1, kpi2, kpi3,kpi4,kpi5,kpi6,kpi7,kpi8,kpi9,kpi10,kpi11,kpi12,kpi13,kpi14,kpi15 = st.columns(15)

        kpi1.metric(label="Avg Voltage" , value=round(avgvol))
        kpi2.metric(label="Avg Pf" , value=round(avgPF))
        kpi3.metric(label="Avg Current" , value=round(avgCur))
        kpi4.metric(label="Total Active power" , value=round(TotalActivePower))
        kpi5.metric(label="Total Reactive power" , value=round(TotalReactivePower))
        kpi6.metric(label="Total Apparent power" , value=round(TotalApparentPower))
        kpi7.metric(label="THD Voltage L1" , value=round(THDVolL1))
        kpi8.metric(label="THD Voltage L2" , value=round(THDVolL2))
        kpi9.metric(label="THD Voltage L3" , value=round(THDVolL3))
        kpi10.metric(label="THD Current L1" , value=round(THDCurL1))
        kpi11.metric(label="THD Current L2" , value=round(THDCurL2))
        kpi12.metric(label="THD Current L3" , value=round(THDCurL3))
        kpi13.metric(label="Import MWh" , value=round(ImpMWh))
        kpi14.metric(label="ImportMVAh" , value=round(ImpMVAh))
        kpi15.metric(label="Time", value=value )


    fig1, fig2,fig3,fig4,fig5,fig6,fig7,fig8,fig9,fig10,fig11,fig12,fig13,fig14,fig15 = st.columns(15)
    with fig1:
            st.markdown("### Average Voltage Vs Time")
            fig1 = px.line(data_frame=df, y = df['Avg Voltage'], x = 'Time')
            st.write(fig1)
    with fig2:
            st.markdown("### Second Chart")
            fig2 = px.line(data_frame = df, y = 'Avg PF', x = 'Time')
            st.write(fig2)
    with fig3:
            st.markdown("### Second Chart")
            fig3 = px.line(data_frame = df, y = 'Avg Current', x = 'Time')
            st.write(fig3)
    with fig4:
            st.markdown("### Second Chart")
            fig4 = px.line(data_frame = df, y = 'Total Active power', x = 'Time')
            st.write(fig4)
    with fig5:
           st.markdown("### Second Chart")
           fig5 = px.line(data_frame = df, y = 'Total Reactive power', x = 'Time')
           st.write(fig5) 
    with fig6:
            st.markdown("### Second Chart")
            fig6 = px.line(data_frame = df, y = 'Total Apparent power', x = 'Time')
            st.write(fig6)
    with fig7:
            st.markdown("### Second Chart")
            fig7 = px.line(data_frame = df, y = 'THD Voltage L1', x = 'Time')
            st.write(fig7)
    with fig8:
            st.markdown("### Second Chart")
            fig8 = px.line(data_frame = df, y = 'THD Voltage L2', x = 'Time')
            st.write(fig8)
    with fig9:
            st.markdown("### Second Chart")
            fig9 = px.line(data_frame = df, y = 'THD Voltage L3', x = 'Time')
            st.write(fig9)
    with fig10:
            st.markdown("### Second Chart")
            fig10 = px.line(data_frame = df, y = 'THD Current L1', x = 'Time')
            st.write(fig10)
    with fig11:
            st.markdown("### Second Chart")
            fig11 = px.line(data_frame = df, y = 'THD Current L2', x = 'Time')
            st.write(fig11)
    with fig12:
            st.markdown("### Second Chart")
            fig12 = px.line(data_frame = df, y = 'THD Current L3', x = 'Time')
            st.write(fig12)
    with fig13:
            st.markdown("### Second Chart")
            fig13 = px.line(data_frame = df, y = 'Import MWh', x = 'Time')
            st.write(fig13)
    with fig14:
            st.markdown("### Second Chart")
            fig14 = px.line(data_frame = df, y = 'Import MVAh', x = 'Time')
            st.write(fig14)
    with fig15:
            st.markdown("### Second Chart")
            fig15 = px.density_heatmap(data_frame = df, y = 'THD Voltage L3', x = 'Time')
            st.write(fig15)
st.markdown("### Detailed Data View")
st.dataframe(df)

fig = make_subplots(rows=5, cols=3)

fig.add_trace(go.Scatter( y =df['Avg Voltage'], x =df[ 'Time']), row=1, col=1)
fig.add_trace(go.Scatter( y =df[ 'Avg PF'], x = df['Time']), row=1, col=2)
fig.add_trace(go.Scatter(x=df['Time'], y=df['Avg Current']), row=1, col=3)
fig.add_trace(go.Scatter(x=df['Time'], y=df['Total Active power']), row=2, col=1)
fig.add_trace(go.Scatter(x=df['Time'], y=df['Total Reactive power']), row=2, col=2)
fig.add_trace(go.Scatter(x=df['Time'], y=df['Total Apparent power']), row=2, col=3)
fig.add_trace(go.Scatter(x=df['Time'], y=df['THD Voltage L1']), row=3, col=1)
fig.add_trace(go.Scatter(x=df['Time'], y=df['THD Voltage L2']), row=3, col=2)
fig.add_trace(go.Scatter(x=df['Time'], y=df['THD Voltage L3']), row=3, col=3)
fig.add_trace(go.Scatter(x=df['Time'], y=df['THD Current L1']), row=4, col=1)
fig.add_trace(go.Scatter(x=df['Time'], y=df['THD Current L2']), row=4, col=2)
fig.add_trace(go.Scatter(x=df['Time'], y=df['THD Current L3']), row=4, col=3)
fig.add_trace(go.Scatter(x=df['Time'], y=df['Import MWh']), row=5, col=1)
fig.add_trace(go.Scatter(x=df['Time'], y=df['Import MVAh']), row=5, col=2)
#fig.add_trace(go.Densitymapbox(lat=df['THD Voltage L3'], lon=df['Time'], z=df['THD Voltage L3']), row=5, col=3)
fig.update_layout(height=10, width=20, title_text="Charts in Subplots")


fig.show()
time.sleep(1)"""
import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df=pd.read_csv("E:\Elliotsystems\Quicksights\Csv files\HT Panel\9May,2023.csv")

st.set_page_config(
    page_title='Real Time Dashboard for HTPanel',
    page_icon='👌',
    layout='wide'
)

st.title("Real-TimeDahboard for HT-Panel")

parameter_filter=st.selectbox("select the parameter",pd.unique(df['Parameters']))

placeholder=st.empty()

df=df[df['Parameters']==parameter_filter]
for seconds in range(200):
    df['avgVol']=df['Avg Voltage']*np.random.choice(range(1,5))
    df['avgPF']=df['Avg PF']*np.random.choice(range(1,5))
    df['avgCur']=df['Avg Current']*np.random.choice(range(1,5))
    df['TotalActivePower']=df['Total Active power']*np.random.choice(range(1,5))
    df['TotalReactivePower']=df['Total Reactive power']*np.random.choice(range(1,5))
    df['TotalApparentPower']=df['Total Apparent power']*np.random.choice(range(1,5))
    df['THDVolL1']=df['THD Voltage L1']*np.random.choice(range(1,5))
    df['THDVolL2']=df['THD Voltage L2']*np.random.choice(range(1,5))
    df['THDVolL3']=df['THD Voltage L3']*np.random.choice(range(1,5))
    df['THDCurL1']=df['THD Current L1']*np.random.choice(range(1,5))
    df['THDCurL2']=df['THD Current L2']*np.random.choice(range(1,5))
    df['THDCurL3']=df['THD Current L3']*np.random.choice(range(1,5))
    df['ImpMWh']=df['Import MWh']*np.random.choice(range(1,5))
    df['ImpMVAh']=df['Import MVAh']*np.random.choice(range(1,5))
    df['Time']=pd.to_datetime(df['Time'])



    avgvol=np.mean(df['avgVol'])
    avgPF=np.mean(df['avgPF'])
    avgCur=np.mean(df['avgCur'])
    TotalActivePower=np.mean(df['TotalActivePower'])
    TotalReactivePower=np.mean(df['TotalReactivePower'])
    TotalApparentPower=np.mean(df['TotalApparentPower'])
    THDVolL1=np.mean(df['THDVolL1'])
    THDVolL2=np.mean(df['THDVolL2'])
    THDVolL3=np.mean(df['THDVolL3'])
    THDCurL1=np.mean(df['THDCurL1'])
    THDCurL2=np.mean(df['THDCurL2'])
    THDCurL3=np.mean(df['THDCurL3'])
    ImpMWh=np.mean(df['ImpMWh'])
    ImpMVAh=np.mean(df['ImpMVAh'])
    Time=df['Time']
    current_time=time.time()
    formatted_time = time.strftime("%H:%M:%S", time.localtime(current_time))
    value = str(Time.iloc[0])


    with placeholder.container():
        kpi1, kpi2= st.columns(2)
        """ kpi3,kpi4,kpi5,kpi6,kpi7,kpi8,kpi9,kpi10,kpi11,kpi12,kpi13,kpi14,kpi15""" 

        kpi1.metric(label="Avg Voltage" , value=round(avgvol))
        kpi2.metric(label="Avg Pf" , value=round(avgPF))
    """    kpi3.metric(label="Avg Current" , value=round(avgCur))
        kpi4.metric(label="Total Active power" , value=round(TotalActivePower))
        kpi5.metric(label="Total Reactive power" , value=round(TotalReactivePower))
        kpi6.metric(label="Total Apparent power" , value=round(TotalApparentPower))
        kpi7.metric(label="THD Voltage L1" , value=round(THDVolL1))
        kpi8.metric(label="THD Voltage L2" , value=round(THDVolL2))
        kpi9.metric(label="THD Voltage L3" , value=round(THDVolL3))
        kpi10.metric(label="THD Current L1" , value=round(THDCurL1))
        kpi11.metric(label="THD Current L2" , value=round(THDCurL2))
        kpi12.metric(label="THD Current L3" , value=round(THDCurL3))
        kpi13.metric(label="Import MWh" , value=round(ImpMWh))
        kpi14.metric(label="ImportMVAh" , value=round(ImpMVAh))
        kpi15.metric(label="Time", value=value )"""


    fig1, fig2= st.columns(2) #fig3,fig4,fig5,fig6,fig7,fig8,fig9,fig10,fig11,fig12,fig13,fig14,fig15 
    with fig1:
            st.markdown("### Average Voltage Vs Time")
            fig1 = px.line(data_frame=df, y = df['Avg Voltage'], x = 'Time')
            st.write(fig1)
    with fig2:
            st.markdown("### Second Chart")
            fig2 = px.line(data_frame = df, y = 'Avg PF', x = 'Time')
            st.write(fig2)
"""  with fig3:
            st.markdown("### Second Chart")
            fig3 = px.line(data_frame = df, y = 'Avg Current', x = 'Time')
            st.write(fig3)
    with fig4:
            st.markdown("### Second Chart")
            fig4 = px.line(data_frame = df, y = 'Total Active power', x = 'Time')
            st.write(fig4)
    with fig5:
           st.markdown("### Second Chart")
           fig5 = px.line(data_frame = df, y = 'Total Reactive power', x = 'Time')
           st.write(fig5) 
    with fig6:
            st.markdown("### Second Chart")
            fig6 = px.line(data_frame = df, y = 'Total Apparent power', x = 'Time')
            st.write(fig6)
    with fig7:
            st.markdown("### Second Chart")
            fig7 = px.line(data_frame = df, y = 'THD Voltage L1', x = 'Time')
            st.write(fig7)
    with fig8:
            st.markdown("### Second Chart")
            fig8 = px.line(data_frame = df, y = 'THD Voltage L2', x = 'Time')
            st.write(fig8)
    with fig9:
            st.markdown("### Second Chart")
            fig9 = px.line(data_frame = df, y = 'THD Voltage L3', x = 'Time')
            st.write(fig9)
    with fig10:
            st.markdown("### Second Chart")
            fig10 = px.line(data_frame = df, y = 'THD Current L1', x = 'Time')
            st.write(fig10)
    with fig11:
            st.markdown("### Second Chart")
            fig11 = px.line(data_frame = df, y = 'THD Current L2', x = 'Time')
            st.write(fig11)
    with fig12:
            st.markdown("### Second Chart")
            fig12 = px.line(data_frame = df, y = 'THD Current L3', x = 'Time')
            st.write(fig12)
    with fig13:
            st.markdown("### Second Chart")
            fig13 = px.line(data_frame = df, y = 'Import MWh', x = 'Time')
            st.write(fig13)
    with fig14:
            st.markdown("### Second Chart")
            fig14 = px.line(data_frame = df, y = 'Import MVAh', x = 'Time')
            st.write(fig14)
    with fig15:
            st.markdown("### Second Chart")
            fig15 = px.density_heatmap(data_frame = df, y = 'THD Voltage L3', x = 'Time')
            st.write(fig15)"""
st.markdown("### Detailed Data View")
st.dataframe(df)

fig = make_subplots(rows=5, cols=3)

fig.add_trace(go.Scatter( y =df['Avg Voltage'], x =df[ 'Time']), row=1, col=1)
fig.add_trace(go.Scatter( y =df[ 'Avg PF'], x = df['Time']), row=1, col=2)
fig.add_trace(go.Scatter(x=df['Time'], y=df['Avg Current']), row=1, col=3)
fig.add_trace(go.Scatter(x=df['Time'], y=df['Total Active power']), row=2, col=1)
fig.add_trace(go.Scatter(x=df['Time'], y=df['Total Reactive power']), row=2, col=2)
fig.add_trace(go.Scatter(x=df['Time'], y=df['Total Apparent power']), row=2, col=3)
fig.add_trace(go.Scatter(x=df['Time'], y=df['THD Voltage L1']), row=3, col=1)
fig.add_trace(go.Scatter(x=df['Time'], y=df['THD Voltage L2']), row=3, col=2)
fig.add_trace(go.Scatter(x=df['Time'], y=df['THD Voltage L3']), row=3, col=3)
fig.add_trace(go.Scatter(x=df['Time'], y=df['THD Current L1']), row=4, col=1)
fig.add_trace(go.Scatter(x=df['Time'], y=df['THD Current L2']), row=4, col=2)
fig.add_trace(go.Scatter(x=df['Time'], y=df['THD Current L3']), row=4, col=3)
fig.add_trace(go.Scatter(x=df['Time'], y=df['Import MWh']), row=5, col=1)
fig.add_trace(go.Scatter(x=df['Time'], y=df['Import MVAh']), row=5, col=2)
#fig.add_trace(go.Densitymapbox(lat=df['THD Voltage L3'], lon=df['Time'], z=df['THD Voltage L3']), row=5, col=3)
fig.update_layout(height=10, width=20, title_text="Charts in Subplots")


fig.show()
time.sleep(1)
        
        