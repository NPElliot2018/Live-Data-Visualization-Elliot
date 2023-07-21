# Live-Data-Visualization-Elliot

## 5 ways that I explored

### a]AWS Quicksights

Step 1:Login to Amazon Quicksights enterprise edition. Create an analyses and publish your dashboard.You do not need to provision users that can access this dashboard

Step 2:Add your embedding site's domain into the domai allow list in Amazon Quicksights

Step 3:Get a embed URL for your dashboard using the getDashboardURL with IDENTITY type set to ANONYMOUS. This is a one time use URL and needs to be regenerated again. You will required session capacity pack(monthly or annual) for be able to use this functionality.

Step 4:Add this URL to your embedding application and dashboard is rendered to be accessible by anyone that can access your application

#### Youtube videos - 
1]Embed QuicKSight Dashboards on Public Portals- https://youtu.be/Lzvh0--BBFE
2]Quicksights Tutorials- https://youtube.com/playlist?list=PLaszktDZAWXYTaSm9TvdinXDKedb3q8-z

### b]AWS Grafana
#### Architecture Overview

![image](https://github.com/NPElliot2018/Live-Data-Visualization-Elliot/assets/140134093/fab9a96b-d350-410b-a204-a014e82282ae)

#### Introduction:

i]This diagram shows the end -to -end view of our system from the device that is generating the data to the data visualization in our dashboard. 

ii]We'll use our laptop as an IoT device that will generate CPU utilization telemetry.We do this because sensor send data periodically , and to test this architecture , we need to mimic it as closely as possible. 

iii]This of course could be any device capable of generating data and either sending that data directly to AWS IoT Core or forwarding the data to another device such as a local gateway or proxy that has a network connection.
 
#### Step 1 : AWS IOT Core-

i] AWS IOT Core provides SDKs in a variety of popular languages capable of running on microcontrollers such as ESP32 or STM32 and also devices capable of running Windows or Linux. In this demonstration we'll use the AWS IoT Python SDK on our laptop. 

ii]The CPU utilization telemetry will be sent as MQTT messages over a secure mutually authenticated TLS 1 .2 connection to AWS IoT Core. The connection and the transmission of the data will be accomplished with two lines of Python code, one to establish the connection and the other to publish the data. 

ii]The device's identity is defined with an X509 certificate. The device must present the certificate to establish the connection to AWS IoT Core. The AWS IoT SDK will take care of this for us. 

iii]The device's permitted actions, including where the telemetry data can be sent, are defined with policies that are associated with or attached to the X509 certificate. 

iv]The connection is managed by the AWS IoT Core device gateway. The gateway provides support for MQTT traffic based on both the MQTT 3 .1 .1 and 5 .0 specifications and also supports other protocols such as HTTP, WebSockets and LoRaWAN, but in this video we are focused on the MQTT protocol.

v]The AWS IoT Core rules engine can route our telemetry data to other AWS services and also to external destinations. The rules engine is very powerful and can inspect, transform and augment messages using over 60 AWS provided built -in functions. 

#### Step 2 : AWS Timestream-

i]In this demonstration we'll create a routing rule that subscribes to the MQTT topic the laptop is sending the data on and then routes selected items in the message payload to our time stream database. 

ii]We will persist our telemetry in a data store and this demonstration will use Amazon time stream as our data store. But popular alternative destinations we could use include AWS IoT analytics pipelines, Amazon S3, Amazon DynamoDB and Amazon Kinesis data streams. 

iii]We've selected a the message payload to our time stream database. We will persist our telemetry in a data store and this demonstration will use Amazon time stream as our data store. But popular alternative destinations we could use include AWS IoT analytics pipelines, Amazon S3, Amazon DynamoDB and Amazon Kinesis data streams. 

iv]We've selected a Amazon TimeStream because it is a fast, scalable and serverless time series database service that makes it easier to store and analyse trillions of events per day, while automatically scaling up or down to adjust capacity and performance so that we don't have to manage the underlying infrastructure. 

v]Now that we have the data in Amazon TimeStream, we can build visual representations to observe the incoming data in close to real time or retrospectively analyse data over a given time window, such as the last minute or the last hour or whatever time period is needed. 

#### Step 3: AWS Managed Grafana
i]In this demonstration we'll use Amazon Managed Grafana to build our visualisation. Amazon Managed Grafana is a fully managed service for Grafana, which is a popular open source dashboard platform. 

ii]You can find links to the Grafana open source website and the Amazon Managed Grafana service in the notes below. We're using Amazon Managed Grafana because it automatically scales compute and database infrastructure as usage demands increase, with automated version updates and security patching. 

iii]All this while enabling us to query and visualise our data. Amazon Managed Grafana also provides a built -in connector for our Amazon TimeStream time series database

#### Youtube videos for reference-
1]AWS IoT - Device data to dashboard in 10 minutes - A demonstration- https://youtu.be/z8T4hAERuOg
2]Build an IIoT Solution using AWS Services | Monitor using Grafana-https://www.youtube.com/live/Byik_DSPymA?feature=share

### c]Tableau

#### Step 1:
First, you need to publish your Tableau dashboard to Tableau Server or Tableau Online. Make sure you have the necessary permissions to publish the dashboard to the desired location.

#### Step 2:
Once the dashboard is published, you can obtain the embed code from Tableau Server or Tableau Online. This code allows you to embed the live dashboard into your webpage.

#### Step 3:
To ensure the dashboard looks and functions as desired when embedded, open the dashboard in Tableau Web Edit mode. This allows you to make any necessary adjustments to the dashboard layout and interactions.

#### Step 4:
The embed code usually includes the dashboard URL and specific parameters to control the display and interactivity of the dashboard. Customize the embed code according to your requirements, such as adjusting the size of the embedded dashboard, specifying filters or parameter values, and setting the authentication method.

#### Step 5:
Paste the customized embed code into the HTML code of your webpage. This can be done within an HTML <iframe> tag. The <iframe> tag is used to embed an external resource, in this case, the live Tableau dashboard.

#### Step 6:
Preview and test the embedded dashboard in your webpage. Ensure that it displays correctly and that the interactions and filters work as intended.

#### Step 7:
Depending on your requirements, you might want to add additional security measures to control access to the embedded dashboard. This can include authentication and authorization mechanisms to restrict who can view the dashboard.

#### Step 8:
After you have successfully embedded the Tableau dashboard and tested it, publish your webpage to make it accessible to your users.

#### Resources-
1]Auto Refresh Embedded Tableau Dashboards-https://youtu.be/aLNwkdSO2Kw

2]https://www.youtube.com/watch?v=wJ2CHIJalNU

3]https://www.youtube.com/results?search_query=live+monitoring+dashboard+using+tableau

4]https://www.youtube.com/results?search_query=live+tableau+dashboard+on+website

5]https://www.youtube.com/results?search_query=real+time+dashboard+on+Tableau

6]https://community.tableau.com/s/question/0D54T00000C5iF1SAJ/tableau-doubt

### d]Analysis with Python

To perform data analysis using the Python pandas-profiling library, follow these steps:

#### Step 1 :
Install pandas-profiling:
Make sure you have Python and pandas installed in your environment. You can then install pandas-profiling using pip

#### Step 2 :
Import Libraries and Load Data:
Import the necessary libraries, including pandas and pandas_profiling. Load your data into a pandas DataFrame.

#### Step 3 :
Create the Profile Report:
Generate the pandas profile report by calling ProfileReport on the DataFrame.

#### Step 4 :
Display the Profile Report:
To view the profile report, you can either use the notebook interface (Jupyter Notebook or JupyterLab) or export it as an HTML report.
Using Jupyter Notebook:

#### Step 5 :
Exporting as an HTML report:
profile.to_file("data_profile_report.html")

The report will contain various sections, including an overview of the dataset, data statistics, data types, missing values, correlations, distributions, and more. It provides valuable insights into the dataset and helps in identifying patterns, issues, and potential data quality problems.Remember that for large datasets, generating the profile report may take some time. Additionally, the report is more suitable for exploratory data analysis and initial data inspection. For deeper analysis, you may need to perform additional custom data analysis using pandas or other data analysis libraries in Python.

#### Resources-

1]https://pypi.org/project/pandas-profiling/

2]https://www.analyticsvidhya.com/blog/2021/06/generate-reports-using-pandas-profiling-deploy-using-streamlit/

3]https://www.geeksforgeeks.org/pandas-profiling-in-python/

4]https://towardsdatascience.com/pandas-profiling-easy-exploratory-data-analysis-in-python-65d6d0e23650

### e]Streamlit

Streamlit is a powerful Python library that allows you to create interactive web applications for data visualization and data analysis. It is designed to be easy to use, making it accessible to data scientists and developers with minimal web development experience. Here's a step-by-step guide on how to perform data visualization using Streamlit:

#### Step 1 Install Streamlit:
Ensure you have Python installed in your environment. You can install Streamlit using pip:

#### Step 2Import Libraries and Load Data:
Start by importing the necessary libraries, including streamlit and pandas. Load your data into a pandas DataFrame.

#### Step 3 Create Interactive Visualizations:
Streamlit allows you to create various types of interactive visualizations easily. Here are a few examples:

##### Example 1 - Line Chart:

st.line_chart(data['column_name'])

 ##### Example 2 - Bar Chart:

st.bar_chart(data['column_name'])

##### Example 3 - Scatter Plot:

st.scatter_plot(data['x_column'], data['y_column'])

#### Step 4 Add Interactive Widgets:

Streamlit provides various interactive widgets that you can use to control the visualizations dynamically. Some common widgets include sliders, dropdowns, checkboxes, and buttons.

##### Example - Slider:

bins = st.slider('Select the number of bins:', min_value=10, max_value=100, value=50)

st.hist(data['column_name'], bins=bins)

##### Example - Dropdown:

selected_column = st.selectbox('Select a column:', data.columns)

st.line_chart(data[selected_column])

#### Step 5 Add Text and Explanations:

You can add text, titles, and explanations to provide context and insights alongside the visualizations.

st.title('Data Visualization with Streamlit')

st.write('Here is a line chart:')

#### Step 6 Run the Streamlit App:

To run your Streamlit app, create a Python script (e.g., app.py) and save your code there. Then, open your terminal or command prompt and navigate to the directory containing the script. Run the following command:

streamlit run app.py

Streamlit will start a local server, and you'll be able to view your data visualization web app in your web browser.

#### Step 7 Share the App (Optional):

If you want to share the app with others, you can deploy it to various platforms like Streamlit Sharing, Heroku, or AWS.

This is just a introduction to data visualization using Streamlit. Streamlit offers many more functionalities, such as customizing the layout, handling user inputs, and integrating machine learning models. For more advanced features and customization, refer to the official Streamlit documentation and gallery of examples.

#### Resources-

1]https://towardsdatascience.com/building-a-dashboard-in-under-5-minutes-with-streamlit-fd0c906ff886

2]https://www.turing.com/kb/how-to-build-an-interactive-dashboard-in-python-using-streamlit

3]https://blog.streamlit.io/how-to-build-a-real-time-live-dashboard-with-streamlit/
