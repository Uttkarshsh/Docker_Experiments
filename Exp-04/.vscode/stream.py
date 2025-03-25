import streamlit as st
import psycopg2

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        dbname="mydb",
        user="admin",
        password="adminpassword",
        host="my_postgres",  # PostgreSQL container name as hostname
        port="5432"
    )
    return conn

st.title("Streamlit App with PostgreSQL")

try:
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Fetch data from PostgreSQL
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()

    st.write("### User Data from PostgreSQL")
    for row in rows:
        st.write(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

    cur.close()
    conn.close()
except Exception as e:
    st.error(f"Error connecting to database: {e}")
