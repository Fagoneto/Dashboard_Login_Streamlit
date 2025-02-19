import streamlit as st
import psycopg2

# Function to connect to the Neon database
def connect_to_neon():
    conn = psycopg2.connect(
        host="ep-blue-leaf-a83owbne-pooler.eastus2.azure.neon.tech",  # Replace with your Neon host
        dbname="REGISTROS",  # Replace with your database name
        user="REGISTROS_owner",  # Replace with your username
        password="npg_VCo8vO3ydpZY",  # Replace with your password
        port="5432"  # Default PostgreSQL port
    )
    return conn

# Streamlit app
def main():
    st.title("Streamlit + Neon DB Example")

    # Connect to the database
    conn = connect_to_neon()
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM REGISTROS")  # Replace with your table name
    rows = cursor.fetchall()

    # Display the results in Streamlit
    st.write("Data from Neon DB:")
    st.table(rows)

    # Close the connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()