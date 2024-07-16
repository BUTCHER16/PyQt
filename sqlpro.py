import mysql.connector

# Replace these with your actual database credentials
host = "localhost"
user = "root"
password = "User@3214"
database = "mist_vfx"

try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connected to MySQL database")

        # Perform database operations here

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
