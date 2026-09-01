import oracledb
from datetime import date
from db_connection import connect_db


connection = None
cursor = None

cus_id = 1001
cus_name = "Emma Johnson"
email = "emma.johnson@example.com"
state = "FL"
sign_up_date = date(2024, 1, 15)

try:
    connection = connect_db()
    cursor = connection.cursor()

    print("Connected to Oracle Database")

    cursor.execute(
        """
        INSERT INTO customers (
            customer_id,
            customer_name,
            email,
            state,
            signup_date
        )
        VALUES (
            :customer_id,
            :customer_name,
            :email,
            :state,
            :signup_date
        )
        """,
        customer_id=cus_id,
        customer_name=cus_name,
        email=email,
        state=state,
        signup_date=sign_up_date
    )

except oracledb.Error as error:
    print("Oracle Database Error:")
    print(f"\t{error}")

    if connection:
        connection.rollback()
        print("Transaction rolled back.")

else:
    connection.commit()
    print("Transaction committed.")

finally:
    if cursor:
        cursor.close()

    if connection:
        connection.close()
        print("Connection closed.")