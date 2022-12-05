import streamlit as st
import os
import snowflake.connector
import warnings 
warnings.filterwarnings("ignore")

st.header("Create Database/Schema/Table", anchor=None)

db_conf = st.radio("Do you want to create Database",('Yes', 'No'))

if db_conf == 'Yes':
    db_name = st.text_input('Enter Database Name')
    if st.button('submit'):
        sql_cmd = 'CREATE OR REPLACE DATABASE' + str(db_name)
        with snowflake.connector.connect(
    user='RAJREDDY',
    password='Raju1997@$',
    account='VK83964.ap-southeast-1',
    warehouse='DNAHACK') as con:
            
            try:
                cur = con.cursor()
                cur.execute(sql_cmd)
            except Exception as e:
                print(e)
            finally:
                cur.close()
        con.close()
        st.write('Database has been created')
        db_conf = st.radio("Do you want to create Schema",('Yes', 'No'))
        
    

    