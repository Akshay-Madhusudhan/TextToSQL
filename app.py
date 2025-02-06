from dotenv import load_dotenv

## load all the environment variable
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load google gemini model and provide sql query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the sql database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define your prompt!
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, and MARKS \n\nFor example, \nExample 1 - How many entries of records are present? The SQL command will be something like this SELECT COUNT(*) FROM STUDENT; \nExample 2 - Tell me all the students studying in Data Science? The SQL command will be something like this SELECT * FROM STUDENT WHERE CLASS = "Data Science"; also the sql code should not have ''' in the beginning or end nor should there be sql words in the output.
    """
]

# Streamlit App
st.set_page_config(page_title="AI TextToSQL")
st.header("Gemini Pro App To Retrieve Data Using SQL")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question!")

#If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, "student.db")
    st.subheader("Here is the data that meets your requirements:")
    for row in data:
        print(row)
        st.header(row)