import mysql.connector  # 👈 Yeh line sabse upar hona zaroori hai!

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",     # 'localhost' ki jagah IP
            user="root",
            password="root123",   # Aapka set kiya hua password
            database="hospital_db",
            port=3306
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None