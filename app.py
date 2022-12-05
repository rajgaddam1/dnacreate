import streamlit as st
import os
import snowflake.connector
import warnings 
warnings.filterwarnings("ignore")

user = os.environ.get('user')
password = os.environ.get('password')

st.header("Create Database/Schema/Table", anchor=None)

db_conf = st.radio("Do you want to create Database",('No','Yes'))

if db_conf == 'Yes':
    db_name = st.text_input('Enter Database Name')
    if st.button('submit'):
        sql_cmd = 'CREATE OR REPLACE DATABASE ' + str(db_name) + ';'
        with snowflake.connector.connect(
    user = user,
    password = password,
    account='VK83964.ap-southeast-1',
    warehouse='DNAHACK') as con:
            
            try:
                cur = con.cursor()
                cur.execute(sql_cmd)
                st.write('Database has been created')
            except Exception as e:
                print(e)
                st.write('An error has occured please check logs')
            finally:
                cur.close()
        con.close()
        sc_conf = st.radio("Do you want to create Schema",('No', 'Yes'))
        if sc_conf == 'Yes':
            sc_name = st.text_input('Enter Schema Name')
            if st.button('submit'):
                sql_cmd1 = 'CREATE OR REPLACE SCHEMA ' + str(sc_name) + ';'
                with snowflake.connector.connect(
                        user = user,
                        password = password,
                        account='VK83964.ap-southeast-1',
                        warehouse='DNAHACK', 
                        database = db_name) as con:
                    
                    try:
                        cur = con.cursor()
                        cur.execute(sql_cmd)
                        st.write('Database has been created')
                    except Exception as e:
                        print(e)
                        st.write('An error has occured please check logs')
                    finally:
                        cur.close()
                con.close()
                
                
            

        
    

    
