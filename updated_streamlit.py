#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[2]:


import numpy as np
import pandas as pd
import time
import altair as alt


# Sidebar options
selected_sidebar_option = st.sidebar.radio(
    "Choose a sector to investigate",
    ("Consumer Sentiment", "Finance", "Housing","Inflation","Labor","Production")
)

# In[3]:


consumer = pd.read_excel('streamlit/Consumer Sentiment.xlsx')
finance = pd.read_excel('streamlit/Financial.xlsx')
housing = pd.read_excel('streamlit/Housing.xlsx')
inflation = pd.read_excel('streamlit/Inflation.xlsx')
labor = pd.read_excel('streamlit/Labor.xlsx')
production = pd.read_excel('streamlit/Production.xlsx')


# # consumer

# In[5]:


l1 =[]
for i in range(1,6):
    list1 = consumer.iloc[1:,i].to_list()
    list1.reverse()
    l1.append(list1)


# In[6]:


l2 =[]
for i in range(1,6):
    n =0
    latest = consumer.iloc[n,i]
    while pd.isnull(latest):
        latest = consumer.iloc[n+1,i]
        n+=1
    l2.append(latest)


# In[7]:


l3 = []
for i in range(1,6):
    avg3 = 0
    count = 0
    n=0
    while count<3:
        latest = consumer.iloc[n,i]
        if pd.isnull(latest):
            while pd.isnull(latest):
                n+=1
                latest = consumer.iloc[n,i]
                n+=1
        else:
            n+=1
        avg3 += latest
        count +=1

    l3.append(avg3/3)


# In[8]:


l4 = []
for i in range(1,6):
    avg12 = 0
    count = 0
    n=0
    while count<12:
        latest = consumer.iloc[n,i]
        if pd.isnull(latest):
            while pd.isnull(latest):
                n+=1
                latest = consumer.iloc[n,i]
                n+=1
        else:
            n+=1
        avg12 += latest
        count +=1

    l4.append(avg12/12)

l5 = []
for i in range(1,6):
    avg6 = 0
    count = 0
    n=0
    while count<6:
        latest = consumer.iloc[n,i]
        if pd.isnull(latest):
            while pd.isnull(latest):
                n+=1
                latest = consumer.iloc[n,i]
                n+=1
        else:
            n+=1
        avg6 += latest
        count +=1

    l5.append(avg6/6)



# In[9]:
# Functions for Consumer section
def display_consumer_section():
    st.title("Consumer Sentiment")
    consumer
    data_df = pd.DataFrame(
        {
            "Name": ["Conference Board US Leading Index Average Consumer Expectation",'Conference Board Consumer Confidence Expectations SA 1985=100','University of Michigan Consumer Expectations Index','University of Michigan Consumer Sentiment Index','Conference Board Consumer Confidence SA 1985=100'],
            "Latest":[l2[0],l2[1],l2[2],l2[3],l2[4]],
            "Last 3m avg": [l3[0],l3[1],l3[2],l3[3],l3[4]],
            "Last 6m avg": [l5[0],l5[1],l5[2],l5[3],l5[4]],
            "Last 12m avg":[l4[0],l4[1],l4[2],l4[3],l4[4]],
            "data": [l1[0],l1[1],l1[2],l1[3],l1[4]],

        }
    )

    st.data_editor(
        data_df,
        column_config={
            "Name": st.column_config.TextColumn(),
            "Latest": st.column_config.NumberColumn(),
            "Last 3m avg":  st.column_config.NumberColumn(),
            "Last 6m avg":  st.column_config.NumberColumn(),
            "Last 12m avg":  st.column_config.NumberColumn(),
            "data": st.column_config.LineChartColumn(
                "Last 20 Years",
                width="large",
                help="Conference Board US Leading Index Average Consumer Expectation in last 20 years",
                y_min=-5,
                y_max=5
             ),
        },
        hide_index=True,
    )

    dict_inf = {
            '1': 'Conference Board US Leading Index Average Consumer Expectation',
            '2': 'Conference Board Consumer Confidence Expectations SA 1985=100',
            '3': 'University of Michigan Consumer Expectations Index',
            '4': 'University of Michigan Consumer Sentiment Index',
            '5': 'Conference Board Consumer Confidence SA 1985=100'}

    # Choose a variable using selectbox
    selected_option = st.selectbox('Choose a variable to see the graph', list(dict_inf.values()))
    st.write('You selected:', selected_option)

    # Tabs
    tabs = st.tabs(["📈 Chart", "⚙️ Data"])

    with tabs[0]:
        def graphs(name):

            chart_data = consumer.set_index('Date')[name] ##
            chart = alt.Chart(chart_data.reset_index()).mark_line().encode(
                x='Date',
                y=name,
            ).properties(
                width=600,
                height=400
            ).configure_axis(
                labelFontSize=12,
                titleFontSize=14
            )

            st.altair_chart(chart, use_container_width=True)
            st.write(f"""
            *Note: The x-axis represents the Date, and the y-axis represents the {name} values.*
            """)
            return None
        graphs(selected_option)

    with tabs[1]:
        st.write("Data with selected columns:")
        if 'Date' in consumer.columns and selected_option in consumer.columns:##
            selected_data = consumer[['Date', selected_option]]##
            st.write(selected_data)
            # Get the date range using iloc
            st.write(f"""
            *Note: The Date ranges from '{consumer['Date'].iloc[-1]}' to '{consumer['Date'].iloc[0]}'.*
            """)##
        else:
            st.write("Columns 'Date' and/or '{}' not found in the dataset.".format(selected_option))

# # Housing

# In[10]:


h_l1 =[]
for i in range(1,3):
    list1 = housing.iloc[:,i].to_list()
    list1.reverse()
    h_l1.append(list1)


# In[11]:


h_l2 =[]
for i in range(1,3):
    n =0
    latest = housing.iloc[n,i]
    while pd.isnull(latest):
        latest = housing.iloc[n+1,i]
        n+=1
    h_l2.append(latest)


# In[12]:


h_l3 = []
for i in range(1,3):
    avg3 = 0
    count = 0
    n=0
    while count<3:
        latest = housing.iloc[n,i]
        if pd.isnull(latest):
            while pd.isnull(latest):
                n+=1
                latest = housing.iloc[n,i]
                n+=1
        else:
            n+=1
        avg3 += latest
        count +=1

    h_l3.append(avg3/3)


# In[13]:


h_l4 = []
for i in range(1,3):
    avg12 = 0
    count = 0
    n=0
    while count<12:
        latest = housing.iloc[n,i]
        if pd.isnull(latest):
            while pd.isnull(latest):
                n+=1
                latest = housing.iloc[n,i]
                n+=1
        else:
            n+=1
        avg12 += latest
        count +=1

    h_l4.append(avg12/12)

h_l5 = []
for i in range(1,3):
    avg6 = 0
    count = 0
    n=0
    while count<6:
        latest = housing.iloc[n,i]
        if pd.isnull(latest):
            while pd.isnull(latest):
                n+=1
                latest = housing.iloc[n,i]
                n+=1
        else:
            n+=1
        avg12 += latest
        count +=1

    h_l5.append(avg6/6)


# In[14]:
# Functions for Housing section
def display_housing_section():
    st.title("Housing")
    housing

    data_df = pd.DataFrame(
        {
            "Name": ["Private Housing Units Started by Structure Total Monthly % Change SA",'Conference Board US Leading Index Building Permits'],
            "Latest":[h_l2[0],h_l2[1]],
            "Last 3m avg": [h_l3[0],h_l3[1]],
            "Last 6m avg": [h_l5[0],h_l5[1]],
            "Last 12m avg":[h_l4[0],h_l4[1]],
            "data": [h_l1[0],h_l1[1]],

        }
    )

    st.data_editor(
        data_df,
        column_config={
            "Name": st.column_config.TextColumn(),
            "Latest": st.column_config.NumberColumn(),
            "Last 3m avg":  st.column_config.NumberColumn(),
            "Last 6m avg":  st.column_config.NumberColumn(),
            "Last 12m avg":  st.column_config.NumberColumn(),
            "data": st.column_config.LineChartColumn(
                "Last 20 Years",
                width="large",
                help="Conference Board US Leading Index Average Consumer Expectation in last 20 years",
                y_min=-1,
                y_max=1,
             ),
        },
        hide_index=True,
    )
    dict_inf = {
        '1':'Private Housing Units Started by Structure Total Monthly % Change SA',
        '2':'Conference Board US Leading Index Building Permits'}

    # Choose a variable using selectbox
    selected_option = st.selectbox('Choose a variable to see the graph', list(dict_inf.values()))
    st.write('You selected:', selected_option)

    # Tabs
    tabs = st.tabs(["📈 Chart", "⚙️ Data"])

    with tabs[0]:
        def graphs(name):

            chart_data = housing.set_index('Date')[name] ##
            chart = alt.Chart(chart_data.reset_index()).mark_line().encode(
                x='Date',
                y=name,
            ).properties(
                width=600,
                height=400
            ).configure_axis(
                labelFontSize=12,
                titleFontSize=14
            )

            st.altair_chart(chart, use_container_width=True)
            st.write(f"""
            *Note: The x-axis represents the Date, and the y-axis represents the {name} values.*
            """)
            return None
        graphs(selected_option)

    with tabs[1]:
        st.write("Data with selected columns:")
        if 'Date' in finance.columns and selected_option in housing.columns:##
            selected_data = housing[['Date', selected_option]]##
            st.write(selected_data)
            # Get the date range using iloc
            st.write(f"""
            *Note: The Date ranges from '{housing['Date'].iloc[-1]}' to '{housing['Date'].iloc[0]}'.*
            """)
        else:
            st.write("Columns 'Date' and/or '{}' not found in the dataset.".format(selected_option))

# # Inflation

# In[15]:


i_l1 =[]
for i in range(1,4):
    list1 = inflation.iloc[:,i].to_list()
    list1.reverse()
    i_l1.append(list1)

i_l2 =[]
for i in range(1,4):
    n =0
    latest = inflation.iloc[n,i]
    while pd.isnull(latest):
        latest = inflation.iloc[n+1,i]
        n+=1
    i_l2.append(latest)

i_l3 = []
for i in range(1,4):
    avg3 = 0
    count = 0
    n=0
    while count<3:
        latest = inflation.iloc[n,i]
        if pd.isnull(latest):
            while pd.isnull(latest):
                n+=1
                latest = inflation.iloc[n,i]
                n+=1
        else:
            n+=1
        avg3 += latest
        count +=1

    i_l3.append(avg3/3)

i_l4 = []
for i in range(1,4):
    avg12 = 0
    count = 0
    n=0
    while count<12:
        latest = inflation.iloc[n,i]
        if pd.isnull(latest):
            while pd.isnull(latest):
                n+=1
                latest = inflation.iloc[n,i]
                n+=1
        else:
            n+=1
        avg12 += latest
        count +=1

    i_l4.append(avg12/12)

i_l5 = []
for i in range(1,4):
    avg6 = 0
    count = 0
    n=0
    while count<6:
        latest = inflation.iloc[n,i]
        if pd.isnull(latest):
            while pd.isnull(latest):
                n+=1
                latest = inflation.iloc[n,i]
                n+=1
        else:
            n+=1
        avg6 += latest
        count +=1

    i_l5.append(avg6/6)


# In[16]:
# Functions for Inflation section
def display_inflation_section():
    inflation['CPI ex-Food & Energy (mom %)'] = pd.to_numeric(inflation['CPI ex-Food & Energy (mom %)'], errors='coerce')
    st.title("Inflation")
    inflation

    data_df = pd.DataFrame(
        {
            "Name": ['CPI ex-Food & Energy (mom %)',
                     'Consumer Price Index (mom %)',
                     'US PCE Index Market-Based Motor Vehicles and Parts SA'],
            "Latest":[i_l2[0],i_l2[1],i_l2[2]],
            "Last 3m avg": [i_l3[0],i_l3[1],i_l3[2]],
            "Last 6m avg": [i_l5[0],i_l5[1],i_l5[2]],
            "Last 12m avg":[i_l4[0],i_l4[1],i_l4[2]],
            "data": [i_l1[0],i_l1[1],i_l1[2]],

        }
    )

    st.data_editor(
        data_df,
        column_config={
            "Name": st.column_config.TextColumn(),
            "Latest": st.column_config.NumberColumn(),
            "Last 3m avg":  st.column_config.NumberColumn(),
            "Last 6m avg":  st.column_config.NumberColumn(),
            "Last 12m avg":  st.column_config.NumberColumn(),
            "data": st.column_config.LineChartColumn(
                "Last 20 Years",
                width="large",
                help="Conference Board US Leading Index Average Consumer Expectation in last 20 years",
                y_min=-1,
                y_max=1,
             ),
        },
        hide_index=True,
    )
    
    
    dict_inf = {
        '1': "CPI ex-Food & Energy (mom %)",
        '2': "Consumer Price Index (mom %)",
        '3': "US PCE Index Market-Based Motor Vehicles and Parts SA"}

    # Choose a variable using selectbox
    selected_option = st.selectbox('Choose a variable to see the graph', list(dict_inf.values()))
    st.write('You selected:', selected_option)

    # Tabs
    tabs = st.tabs(["📈 Chart", "⚙️ Data"])

    with tabs[0]:
        def graphs(name):

            chart_data = inflation.set_index('Date')[name] ##
            chart = alt.Chart(chart_data.reset_index()).mark_line().encode(
                x='Date',
                y=name,
            ).properties(
                width=600,
                height=400
            ).configure_axis(
                labelFontSize=12,
                titleFontSize=14
            )

            st.altair_chart(chart, use_container_width=True)
            st.write(f"""
            *Note: The x-axis represents the Date, and the y-axis represents the {name} values.*
            """)
            return None
        graphs(selected_option)

    with tabs[1]:
        st.write("Data with selected columns:")
        if 'Date' in inflation.columns and selected_option in inflation.columns:##
            selected_data = inflation[['Date', selected_option]]##
            st.write(selected_data)
            # Get the date range using iloc
            st.write(f"""
            *Note: The Date ranges from '{inflation['Date'].iloc[-1]}' to '{inflation['Date'].iloc[0]}'.*
            """)
        else:
            st.write("Columns 'Date' and/or '{}' not found in the dataset.".format(selected_option))
# # labor

# In[8]:


l_l1 =[]
for i in range(1,6):
    list1 = labor.iloc[:,i].to_list()
    list2 = []
    for i in list1:
        if pd.isnull(i):
            continue
        else:
            list2.append(i)
    list2.reverse()
    l_l1.append(list2)

l_l2 =[]
for i in range(1,6):
    n =0
    latest = labor.iloc[n,i]
    while pd.isnull(latest):
        latest = labor.iloc[n+1,i]
        n+=1
    l_l2.append(latest)

l_l3 = []
for i in range(1,6):
    avg3 = 0
    count = 0
    n=0
    while count<3:
        latest = labor.iloc[n,i]
        if pd.isnull(latest):
            while pd.isnull(latest):
                n+=1
                latest = labor.iloc[n,i]
                n+=1
        else:
            n+=1
        avg3 += latest
        count +=1

    l_l3.append(avg3/3)

l_l4 = []
for i in range(1,6):
    avg12 = 0
    count = 0
    n=0
    while count<12:
        latest = labor.iloc[n,i]
        if pd.isnull(latest):
            while pd.isnull(latest):
                n+=1
                latest = labor.iloc[n,i]
                n+=1
        else:
            n+=1
        avg12 += latest
        count +=1

    l_l4.append(avg12/12)

l_l5 = []
for i in range(1,6):
    avg6 = 0
    count = 0
    n=0
    while count<6:
        latest = labor.iloc[n,i]
        if pd.isnull(latest):
            while pd.isnull(latest):
                n+=1
                latest = labor.iloc[n,i]
                n+=1
        else:
            n+=1
        avg6 += latest
        count +=1

    l_l5.append(avg6/6)


# In[28]:
# Functions for Labor section
def display_labor_section():
    st.title("Labor")
    labor

    data_df = pd.DataFrame(
        {
            "Name": ["US Employees on Nonfarm Payrolls Total SA",
                     'US Personal Income MoM SA',
                     'Nonagricultural Industries Usually Part Time Economic Reasons',
                     'Conference Board Employment Trends Index',
                     'U-3 US Unemployment Rate Total in Labor Force Seasonally Adjusted'],
            "Latest":[l_l2[0],l_l2[1],l_l2[2],l_l2[3],l_l2[4]],
            "Last 3m avg": [l_l3[0],l_l3[1],l_l3[2],l_l3[3],l_l3[4]],
            "Last 5m avg": [l_l3[0],l_l5[1],l_l5[2],l_l5[3],l_l5[4]],
            "Last 12m avg":[l_l4[0],l_l4[1],l_l4[2],l_l4[3],l_l4[4]],
            "data": [l_l1[0],l_l1[1],l_l1[2],l_l1[3],l_l1[4]],

        }
    )

    st.data_editor(
        data_df,
        column_config={
            "Name": st.column_config.TextColumn(),
            "Latest": st.column_config.NumberColumn(),
            "Last 3m avg":  st.column_config.NumberColumn(),
            "Last 6m avg":  st.column_config.NumberColumn(),
            "Last 12m avg":  st.column_config.NumberColumn(),
            "data": st.column_config.LineChartColumn(
                "Last 20 Years",
                width="large",
                help="Conference Board US Leading Index Average Consumer Expectation in last 20 years",
                y_min=-5,
                y_max=5,
             ),
        },
        hide_index=True,
    )
    dict_inf = {
        '1': 'US Employees on Nonfarm Payrolls Total SA',
        '2':'US Personal Income MoM SA',
        '3':'Nonagricultural Industries Usually Part Time Economic Reasons',
        '4':'Conference Board Employment Trends Index',
        '5':'U-3 US Unemployment Rate Total in Labor Force Seasonally Adjusted'}

    # Choose a variable using selectbox
    selected_option = st.selectbox('Choose a variable to see the graph', list(dict_inf.values()))
    st.write('You selected:', selected_option)

    # Tabs
    tabs = st.tabs(["📈 Chart", "⚙️ Data"])

    with tabs[0]:
        def graphs(name):

            chart_data = labor.set_index('Date')[name] ##
            chart = alt.Chart(chart_data.reset_index()).mark_line().encode(
                x='Date',
                y=name,
            ).properties(
                width=600,
                height=400
            ).configure_axis(
                labelFontSize=12,
                titleFontSize=14
            )

            st.altair_chart(chart, use_container_width=True)
            st.write(f"""
            *Note: The x-axis represents the Date, and the y-axis represents the {name} values.*
            """)
            return None
        graphs(selected_option)

    with tabs[1]:
        st.write("Data with selected columns:")
        if 'Date' in labor.columns and selected_option in labor.columns:##
            selected_data = labor[['Date', selected_option]]##
            st.write(selected_data)
            # Get the date range using iloc
            st.write(f"""
            *Note: The Date ranges from '{labor['Date'].iloc[-1]}' to '{labor['Date'].iloc[0]}'.*
            """)
        else:
            st.write("Columns 'Date' and/or '{}' not found in the dataset.".format(selected_option))

# # Production

# In[20]:


p_l1 =[]
for i in range(1,6):
    list1 = production.iloc[:,i].to_list()
    list2 = []
    for i in list1:
        if pd.isnull(i):
            continue
        else:
            list2.append(i)
    list2.reverse()
    p_l1.append(list2)

p_l2 =[]
for i in range(1,6):
    n =0
    latest = production.iloc[n,i]
    while pd.isnull(latest):
        latest = production.iloc[n+1,i]
        n+=1
    p_l2.append(latest)

p_l3 = []
for i in range(1,6):
    avg3 = 0
    count = 0
    n=0
    while count<3:
        latest = production.iloc[n,i]
        if pd.isnull(latest):
            while pd.isnull(latest):
                n+=1
                latest = production.iloc[n,i]
                n+=1
        else:
            n+=1
        avg3 += latest
        count +=1

    p_l3.append(avg3/3)

p_l4 = []
for i in range(1,6):
    avg12 = 0
    count = 0
    n=0
    while count<12:
        latest = production.iloc[n,i]
        if pd.isnull(latest):
            while pd.isnull(latest):
                n+=1
                latest = production.iloc[n,i]
                n+=1
        else:
            n+=1
        avg12 += latest
        count +=1

    p_l4.append(avg12/12)

p_l5 = []
for i in range(1,6):
    avg6 = 0
    count = 0
    n=0
    while count<6:
        latest = production.iloc[n,i]
        if pd.isnull(latest):
            while pd.isnull(latest):
                n+=1
                latest = production.iloc[n,i]
                n+=1
        else:
            n+=1
        avg6 += latest
        count +=1

    p_l5.append(avg6/6)


# In[21]:
# Functions for Production section
def display_production_section():
    st.title("Production")
    production

    data_df = pd.DataFrame(
        {
            "Name": ["Real GDP (qoq %, saar)",'US Manufacturing & Trade Sales in Nominal Dollars SA','US Industrial Production MOM SA','ISM Manufacturing Report on Business New Orders SA','ISM Manufacturing PMI SA'],
            "Latest":[p_l2[0],p_l2[1],p_l2[2],p_l2[3],p_l2[4]],
            "Last 3m avg": [p_l3[0],p_l3[1],p_l3[2],p_l3[3],p_l3[4]],
            "Last 6m avg": [p_l5[0],p_l5[1],p_l5[2],p_l5[3],p_l5[4]],
            "Last 12m avg":[p_l4[0],p_l4[1],p_l4[2],p_l4[3],p_l4[4]],
            "data": [p_l1[0],p_l1[1],p_l1[2],p_l1[3],p_l1[4]],

        }
    )

    st.data_editor(
        data_df,
        column_config={
            "Name": st.column_config.TextColumn(),
            "Latest": st.column_config.NumberColumn(),
            "Last 3m avg":  st.column_config.NumberColumn(),
            "Last 6m avg":  st.column_config.NumberColumn(),
            "Last 12m avg":  st.column_config.NumberColumn(),
            "data": st.column_config.LineChartColumn(
                "Last 20 Years",
                width="large",
                help="Conference Board US Leading Index Average Consumer Expectation in last 20 years",
                y_min=-5,
                y_max=5,
             ),
        },
        hide_index=True,
    )
    dict_inf = {
        '1': 'Real GDP (qoq %, saar)',
        '2':'US Manufacturing & Trade Sales in Nominal Dollars SA',
        '3':'US Industrial Production MOM SA',
        '4':'ISM Manufacturing Report on Business New Orders SA',
        '5':'ISM Manufacturing PMI SA'}

    # Choose a variable using selectbox
    selected_option = st.selectbox('Choose a variable to see the graph', list(dict_inf.values()))
    st.write('You selected:', selected_option)

    # Tabs
    tabs = st.tabs(["📈 Chart", "⚙️ Data"])

    with tabs[0]:
        def graphs(name):

            chart_data = production.set_index('Date')[name] ##
            chart = alt.Chart(chart_data.reset_index()).mark_line().encode(
                x='Date',
                y=name,
            ).properties(
                width=600,
                height=400
            ).configure_axis(
                labelFontSize=12,
                titleFontSize=14
            )

            st.altair_chart(chart, use_container_width=True)
            st.write(f"""
            *Note: The x-axis represents the Date, and the y-axis represents the {name} values.*
            """)
            return None
        graphs(selected_option)

    with tabs[1]:
        st.write("Data with selected columns:")
        if 'Date' in production.columns and selected_option in production.columns:##
            selected_data = production[['Date', selected_option]]##
            st.write(selected_data)
            # Get the date range using iloc
            st.write(f"""
            *Note: The Date ranges from '{production['Date'].iloc[-1]}' to '{production['Date'].iloc[0]}'.*
            """)
        else:
            st.write("Columns 'Date' and/or '{}' not found in the dataset.".format(selected_option))
# # Finance

# In[23]:


f_l1 =[]
for i in range(1,8):
    list1 = finance.iloc[:,i].to_list()
    list2 = []
    for i in list1:
        if pd.isnull(i):
            continue
        else:
            list2.append(i)
    list2.reverse()
    f_l1.append(list2)

f_l2 =[]
for i in range(1,8):
    n =0
    latest = finance.iloc[n,i]
    while pd.isnull(latest):
        latest = finance.iloc[n+1,i]
        n+=1
    f_l2.append(latest)


f_l3 = []
for i in range(1,8):
    avg3 = 0
    count = 0
    n=0
    while count<3:
        latest = finance.iloc[n,i]
        if pd.isnull(latest):
            while pd.isnull(latest):
                n+=1
                latest = finance.iloc[n,i]
                n+=1
        else:
            n+=1
        avg3 += latest
        count +=1

    f_l3.append(avg3/3)


f_l4 = []
for i in range(1,8):
    avg12 = 0
    count = 0
    n=0
    while count<12:
        latest = finance.iloc[n,i]
        if pd.isnull(latest):
            while pd.isnull(latest):
                n+=1
                latest = finance.iloc[n,i]
                n+=1
        else:
            n+=1
        avg12 += latest
        count +=1

    f_l4.append(avg12/12)

f_l5 = []
for i in range(1,8):
    avg6 = 0
    count = 0
    n=0
    while count<6:
        latest = finance.iloc[n,i]
        if pd.isnull(latest):
            while pd.isnull(latest):
                n+=1
                latest = finance.iloc[n,i]
                n+=1
        else:
            n+=1
        avg6 += latest
        count +=1

    f_l5.append(avg6/6)


# In[24]:
# Functions for Finance section
def display_finance_section():
    st.title("Finance")
    finance
    data_df = pd.DataFrame(
        {
            "Name": ["United States Financial Stress Index",
                     'St Louis Federal Reserve Bank Financial Stress Index 4.0',
                     'NY Fed Prob of Recession in US Twelve Months Ahead Predicted by Treasury Spread',
                     'Chicago Fed Adjusted National Financial Conditions Index',
                     'Conference Board US Leading Index Leading Credit Index',
                     'Tighter Standards for C&I Loans for Large Firms (%)',
                     'Tighter Standards for C&I Loans for Small Firms (%)'],
            "Latest":[f_l2[0],f_l2[1],f_l2[2],f_l2[3],f_l2[4],f_l2[5],f_l2[6]],
            "Last 3m avg": [f_l3[0],f_l3[1],f_l3[2],f_l3[3],f_l3[4],f_l3[5],f_l3[6]],
            "Last 6m avg": [f_l5[0],f_l5[1],f_l5[2],f_l5[3],f_l5[4],f_l5[5],f_l5[6]],
            "Last 12m avg":[f_l4[0],f_l4[1],f_l4[2],f_l4[3],f_l4[4],f_l4[5],f_l4[6]],
            "data": [f_l1[0],f_l1[1],f_l1[2],f_l1[3],f_l1[4],f_l1[5],f_l1[6]],

        }
    )

    st.data_editor(
        data_df,
        column_config={
            "Name": st.column_config.TextColumn(),
            "Latest": st.column_config.NumberColumn(),
            "Last 3m avg":  st.column_config.NumberColumn(),
            "Last 6m avg":  st.column_config.NumberColumn(),
            "Last 12m avg":  st.column_config.NumberColumn(),
            "data": st.column_config.LineChartColumn(
                "Last 20 Years",
                width="large",
                help="Conference Board US Leading Index Average Consumer Expectation in last 20 years",
                y_min=-5,
                y_max=5,
             ),
        },
        hide_index=True,
    )
    dict_inf = {
        '1': 'United States Financial Stress Index',
        '2':'St Louis Federal Reserve Bank Financial Stress Index 4.0',
        '3':'NY Fed Prob of Recession in US Twelve Months Ahead Predicted by Treasury Spread',
        '4':'Chicago Fed Adjusted National Financial Conditions Index',
        '5':'Conference Board US Leading Index Leading Credit Index',
        '6':'Tighter Standards for C&I Loans for Large Firms (%)',
        '7':'Tighter Standards for C&I Loans for Small Firms (%)'}

    # Choose a variable using selectbox
    selected_option = st.selectbox('Choose a variable to see the graph', list(dict_inf.values()))
    st.write('You selected:', selected_option)

    # Tabs
    tabs = st.tabs(["📈 Chart", "⚙️ Data"])

    with tabs[0]:
        def graphs(name):

            chart_data = finance.set_index('Date')[name] ##
            if chart_data.isnull().any():
                chart = alt.Chart(chart_data.reset_index()).mark_line(point=True).encode(
                    x='Date',
                    y=name,
                ).properties(
                    width=600,
                    height=400
                ).configure_axis(
                    labelFontSize=12,
                    titleFontSize=14
                )
            else:
                # If there are no None values, display a simple line chart
                chart = alt.Chart(chart_data.reset_index()).mark_line(point=False).encode(
                    x='Date',
                    y=name,
                ).properties(
                    width=600,
                    height=400
                ).configure_axis(
                    labelFontSize=12,
                    titleFontSize=14
                )

            st.altair_chart(chart, use_container_width=True)
            st.write(f"""
            *Note: The x-axis represents the Date, and the y-axis represents the {name} values.*
            """)
            return None
        graphs(selected_option)

    with tabs[1]:
        st.write("Data with selected columns:")
        if 'Date' in finance.columns and selected_option in finance.columns:##
            selected_data = finance[['Date', selected_option]]##
            st.write(selected_data)
            # Get the date range using iloc
            st.write(f"""
            *Note: The Date ranges from '{finance['Date'].iloc[-1]}' to '{finance['Date'].iloc[0]}'.*
            """)
        else:
            st.write("Columns 'Date' and/or '{}' not found in the dataset.".format(selected_option))

# Display content based on selected sidebar option
#"Consumer", "Finance", "Housing","Inflation","Labor","Production"
if selected_sidebar_option == "Consumer Sentiment":
    display_consumer_section()
elif selected_sidebar_option == "Finance":
    display_finance_section()
elif selected_sidebar_option == "Housing":
    display_housing_section()
elif selected_sidebar_option == "Inflation":
    display_inflation_section()
elif selected_sidebar_option == "Labor":
    display_labor_section()
elif selected_sidebar_option == "Production":
    display_production_section()
