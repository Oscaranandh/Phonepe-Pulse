import matplotlib.pyplot as plt
import streamlit as st
import os
import json
import sqlite3
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import git
from git.repo.base import Repo



con = sqlite3.connect("C:/Users/3arav/OneDrive/Desktop/oscar/Mydatabase.db")
cur = con.cursor()
st.set_page_config(page_title='PhonePe pulse')
st.markdown("""
    <h1 style='text-align: center;color: #800080;'>PhonePe Pulse </h1>
""", unsafe_allow_html=True)
image_url ="https://www.medianews4u.com/wp-content/uploads/2022/01/PhonePe-Pulse-unveils-digital-payment-trends-for-Q4-2021-Merchant-payments-register-a-37-QoQ-growth-hitting-3.15-Bn-transactions.jpg"
st.image(image_url,width=700)
st.markdown("""<h2 style='color:#A45EE5;'> Welcome to the PhonePe Pulse Data Visualization and Exploration Streamlit Webpage </h2>""",unsafe_allow_html=True)
st.write("""   This web application provides a powerful platform for exploring and analyzing financial transaction data made through the PhonePe app.
 You can use a range of charts, graphs, and tables to visualize transaction data in real-time and gain valuable insights into customer behavior.""")

st.markdown("""<h2 style='color:#A45EE5;'> Data Exploration</h2>""",unsafe_allow_html=True)
# Add data exploration section
st.write("""
Here you can explore transaction data made through the PhonePe app. Use the filters on the left to select date range, transaction type, and user demographics. You can visualize data using a range of charts and graphs such as bar charts, line charts, and scatter plots.
""")

st.markdown("""<h2 style='color:#A45EE5;'> Data Visualization </h2>""",unsafe_allow_html=True)
# Add data visualization section
st.write("""
Here you can visualize transaction data using a range of charts and graphs. The visualizations update in real-time based on the filters you select on the left. You can hover over the charts to see more detailed information and insights.
""")
st.markdown("""<h2 style='color:#A45EE5;'> Overall India </h2>""",unsafe_allow_html=True)
agt=cur.execute('SELECT * FROM Aggregate_Transaction').fetchall()
agt=pd.DataFrame(agt,columns=[i[0] for i in cur.description])
agu=cur.execute('SELECT * FROM Aggregate_user').fetchall()
agu=pd.DataFrame(agu,columns=[i[0] for i in cur.description])
mpt=cur.execute('SELECT * FROM Map_Transaction').fetchall()
mpt=pd.DataFrame(mpt,columns=[i[0] for i in cur.description])
mpu=cur.execute('SELECT * FROM Map_User').fetchall()
mpu=pd.DataFrame(mpu,columns=[i[0] for i in cur.description])
tpt=cur.execute('SELECT * FROM Top_Transaction').fetchall()
tpt=pd.DataFrame(tpt,columns=[i[0] for i in cur.description])
tpu=cur.execute('SELECT * FROM Top_User').fetchall()
tpu=pd.DataFrame(tpu,columns=[i[0] for i in cur.description])


font_style = {'family': 'Arial', 'size': 18, 'color': 'blue'}
title_style = {'family': 'Arial', 'size': 24, 'color': 'green'}

category=st.selectbox('Select ',("Aggregate","Map","Top"))
if category=='Aggregate':
    ts=st.selectbox('Select type',('Transaction','User'))
    if ts=='Transaction':
        cur.execute("SELECT * FROM Aggregate_Transaction")
        cols = list(map(lambda x: x[0], cur.description))
        target=st.selectbox('Select column',cols)
        col2=cols.copy()
        col2.remove(target)
        x_var=st.selectbox('Choose x',col2)
        y_var=st.selectbox('Choose y',col2)
        plots=st.selectbox("Select plot type",('Line','Scatter','Bar'))
        if plots=='Scatter':
            fig=px.scatter(agt,x=x_var,y=y_var,color=target,labels={'x':x_var,'y':y_var})
            fig.update_layout(
                title={
                'text': 'Aggregate Transaction',
                'font': {'family': 'Arial', 'size': 24, 'color': 'blue'}
                },
                xaxis={'title': x_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}},
                yaxis={'title': y_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}}
                )
            cb = st.button("Submit")
            if cb == True:
                st.plotly_chart(fig)
        elif plots=='Line':
            fig = px.line(agt,x=x_var,y=y_var,color=target,labels={'x':x_var,'y':y_var})
            fig.update_layout(
                title={
                    'text': 'Aggregate Transaction',
                    'font': {'family': 'Arial', 'size': 24, 'color': 'blue'}
                },
                xaxis={'title': x_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}},
                yaxis={'title': y_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}}
            )
            cb = st.button("Submit")
            if cb == True:
                st.plotly_chart(fig)
        else:
            fig = px.bar(agt, x=x_var, y=y_var, color=target, labels={'x': x_var, 'y': y_var})
            fig.update_layout(
                title={
                    'text': 'Aggregate Transaction',
                    'font': {'family': 'Arial', 'size': 24, 'color': 'blue'}
                },
                xaxis={'title': x_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}},
                yaxis={'title': y_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}}
            )
            cb = st.button("Submit")
            if cb == True:
                st.plotly_chart(fig)

    else:
        cur.execute("SELECT * FROM Aggregate_User")
        cols = list(map(lambda x: x[0], cur.description))
        target = st.selectbox('Select column',cols)
        col2 = cols.copy()
        col2.remove(target)
        x_var = st.selectbox('Choose x', col2)
        y_var = st.selectbox('Choose y', col2)
        plots = st.selectbox("Select plot type", ('Line', 'Scatter', 'Bar'))
        if plots == 'Scatter':
            fig = px.scatter(agu, x=x_var, y=y_var, color=target, labels={'x': x_var, 'y': y_var})
            fig.update_layout(
                title={
                    'text': 'Aggregate User',
                    'font': {'family': 'Arial', 'size': 24, 'color': 'blue'}
                },
                xaxis={'title': x_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}},
                yaxis={'title': y_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}}
            )
            cb = st.button("Submit")
            if cb == True:
                st.plotly_chart(fig)
        elif plots == 'Line':
            fig = px.line(agu, x=x_var, y=y_var, color=target, labels={'x': x_var, 'y': y_var})
            fig.update_layout(
                title={
                    'text': 'Aggregate User',
                    'font': {'family': 'Arial', 'size': 24, 'color': 'blue'}
                },
                xaxis={'title': x_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}},
                yaxis={'title': y_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}}
            )
            cb = st.button("Submit")
            if cb == True:
                st.plotly_chart(fig)
        else:
            fig = px.bar(agu, x=x_var, y=y_var, color=target, labels={'x': x_var, 'y': y_var})
            fig.update_layout(
                title={
                    'text': 'Aggregate User',
                    'font': {'family': 'Arial', 'size': 24, 'color': 'blue'}
                },
                xaxis={'title': x_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}},
                yaxis={'title': y_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}}
            )
            cb = st.button("Submit")
            if cb == True:
                st.plotly_chart(fig)
elif category=="Map":
    ts = st.selectbox('Select type',('Transaction', 'User'))
    if ts == 'Transaction':
        cur.execute("SELECT * FROM Map_Transaction")
        cols = list(map(lambda x: x[0], cur.description))
        target = st.selectbox('Select column',cols)
        col2 = cols.copy()
        col2.remove(target)
        x_var = st.selectbox('Choose x', col2)
        y_var = st.selectbox('Choose y', col2)
        plots = st.selectbox("Select plot type", ('Line', 'Scatter', 'Bar'))
        if plots == 'Scatter':
            fig = px.scatter(mpt, x=x_var, y=y_var, color=target, labels={'x': x_var, 'y': y_var})
            fig.update_layout(
                title={
                    'text': 'Map Transaction',
                    'font': {'family': 'Arial', 'size': 24, 'color': 'blue'}
                },
                xaxis={'title': x_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}},
                yaxis={'title': y_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}}
            )
            cb = st.button("Submit")
            if cb == True:
                st.plotly_chart(fig)
        elif plots == 'Line':
            fig = px.line(mpt, x=x_var, y=y_var, color=target, labels={'x': x_var, 'y': y_var})
            fig.update_layout(
                title={
                    'text': 'Map Transaction',
                    'font': {'family': 'Arial', 'size': 24, 'color': 'blue'}
                },
                xaxis={'title': x_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}},
                yaxis={'title': y_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}}
            )
            cb = st.button("Submit")
            if cb == True:
                st.plotly_chart(fig)
        else:
            fig = px.bar(mpt, x=x_var, y=y_var, color=target, labels={'x': x_var, 'y': y_var})
            fig.update_layout(
                title={
                    'text': 'Map Transaction',
                    'font': {'family': 'Arial', 'size': 24, 'color': 'blue'}
                },
                xaxis={'title': x_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}},
                yaxis={'title': y_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}}
            )
            cb = st.button("Submit")
            if cb == True:
                st.plotly_chart(fig)
    else:
        cur.execute("SELECT * FROM Map_User")
        cols = list(map(lambda x: x[0], cur.description))
        target = st.selectbox('Select column',cols)
        col2 = cols.copy()
        col2.remove(target)
        x_var = st.selectbox('Choose x', col2)
        y_var = st.selectbox('Choose y', col2)
        plots = st.selectbox("Select plot type", ('Line', 'Scatter', 'Bar'))
        if plots == 'Scatter':
            fig = px.scatter(mpu, x=x_var, y=y_var, color=target, labels={'x': x_var, 'y': y_var})
            fig.update_layout(
                title={
                    'text': 'Map User',
                    'font': {'family': 'Arial', 'size': 24, 'color': 'blue'}
                },
                xaxis={'title': x_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}},
                yaxis={'title': y_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}}
            )
            cb = st.button("Submit")
            if cb == True:
                st.plotly_chart(fig)
        elif plots == 'Line':
            fig = px.line(mpu, x=x_var, y=y_var, color=target, labels={'x': x_var, 'y': y_var})
            fig.update_layout(
                title={
                    'text': 'Map User',
                    'font': {'family': 'Arial', 'size': 24, 'color': 'blue'}
                },
                xaxis={'title': x_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}},
                yaxis={'title': y_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}}
            )
            cb = st.button("Submit")
            if cb == True:
                st.plotly_chart(fig)
        else:
            fig = px.bar(mpu, x=x_var, y=y_var, color=target, labels={'x': x_var, 'y': y_var})
            fig.update_layout(
                title={
                    'text': 'Map User',
                    'font': {'family': 'Arial', 'size': 24, 'color': 'blue'}
                },
                xaxis={'title': x_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}},
                yaxis={'title': y_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}}
            )
            cb = st.button("Submit")
            if cb == True:
                st.plotly_chart(fig)
else:
    ts = st.selectbox('Select type',('Transaction', 'User'))
    if ts == 'Transaction':
        cur.execute("SELECT * FROM Top_Transaction")
        cols = list(map(lambda x: x[0], cur.description))
        target = st.selectbox('Select column',cols)
        col2 = cols.copy()
        col2.remove(target)
        x_var = st.selectbox('Choose x', col2)
        y_var = st.selectbox('Choose y', col2)
        plots = st.selectbox("Select plot type", ('Line', 'Scatter', 'Bar'))
        if plots == 'Scatter':
            fig = px.scatter(tpt, x=x_var, y=y_var, color=target, labels={'x': x_var, 'y': y_var})
            fig.update_layout(
                title={
                    'text': 'Top Transaction',
                    'font': {'family': 'Arial', 'size': 24, 'color': 'blue'}
                },
                xaxis={'title': x_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}},
                yaxis={'title': y_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}}
            )
            cb = st.button("Submit")
            if cb == True:
                st.plotly_chart(fig)
        elif plots == 'Line':
            fig = px.line(tpt, x=x_var, y=y_var, color=target, labels={'x': x_var, 'y': y_var})
            fig.update_layout(
                title={
                    'text': 'Top Transaction',
                    'font': {'family': 'Arial', 'size': 24, 'color': 'blue'}
                },
                xaxis={'title': x_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}},
                yaxis={'title': y_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}}
            )
            cb = st.button("Submit")
            if cb == True:
                st.plotly_chart(fig)
        else:
            fig = px.bar(tpt, x=x_var, y=y_var, color=target, labels={'x': x_var, 'y': y_var})
            fig.update_layout(
                title={
                    'text': 'Top Transaction',
                    'font': {'family': 'Arial', 'size': 24, 'color': 'blue'}
                },
                xaxis={'title': x_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}},
                yaxis={'title': y_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}}
            )
            cb = st.button("Submit")
            if cb == True:
                st.plotly_chart(fig)
    else:
        ccur.execute("SELECT * FROM Top_User")
        cols = list(map(lambda x: x[0], cur.description))
        target = st.selectbox('Select column',cols)
        col2 = cols.copy()
        col2.remove(target)
        x_var = st.selectbox('Choose x', col2)
        y_var = st.selectbox('Choose y', col2)
        plots = st.selectbox("Select plot type", ('Line', 'Scatter', 'Bar'))
        if plots == 'Scatter':
            fig = px.scatter(tpu, x=x_var, y=y_var, color=target, labels={'x': x_var, 'y': y_var})
            fig.update_layout(
                title={
                    'text': 'Top User',
                    'font': {'family': 'Arial', 'size': 24, 'color': 'blue'}
                },
                xaxis={'title': x_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}},
                yaxis={'title': y_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}}
            )
            cb = st.button("Submit")
            if cb == True:
                st.plotly_chart(fig)
        elif plots == 'Line':
            fig = px.line(tpu, x=x_var, y=y_var, color=target, labels={'x': x_var, 'y': y_var})
            fig.update_layout(
                title={
                    'text': 'Top User',
                    'font': {'family': 'Arial', 'size': 24, 'color': 'blue'}
                },
                xaxis={'title': x_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}},
                yaxis={'title': y_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}}
            )
            cb = st.button("Submit")
            if cb == True:
                st.plotly_chart(fig)
        else:
            fig = px.bar(tpu, x=x_var, y=y_var, color=target, labels={'x': x_var, 'y': y_var})
            fig.update_layout(
                title={
                    'text': 'Top User',
                    'font': {'family': 'Arial', 'size': 24, 'color': 'blue'}
                },
                xaxis={'title': x_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}},
                yaxis={'title': y_var, 'title_font': {'family': 'Arial', 'size': 18, 'color': 'green'}}
            )
            cb = st.button("Submit")
            if cb == True:
                st.plotly_chart(fig)

