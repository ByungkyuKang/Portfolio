import oracledb
from datetime import date
from db_connection import connect_db


def get_customer_by_id(cursor, customer_id):
    cursor.execute(
        """
        SELECT customer_id,
               customer_name
          FROM customers
         WHERE customer_id = :customer_id
        """,
        customer_id=customer_id
    )

    return cursor.fetchone()


def main():
    connection = connect_db()
    cursor = connection.cursor()

    print("Connected to Oracle Database")

    # =========================================================
    # Rollback Demo
    # =========================================================

    cus_id = 9999
    cus_name = "Test Customer"
    email = "test.customer@example.com"
    state = "FL"
    sign_up_date = date(2026, 8, 24)

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

    print("Before rollback:")
    print(f"\t{get_customer_by_id(cursor, cus_id)}")

    connection.rollback()

    print("After rollback:")
    print(f"\t{get_customer_by_id(cursor, cus_id)}\n")

    # =========================================================
    # Commit Demo
    # =========================================================

    cus_id = 9998
    cus_name = "Commit Test Customer"
    email = "commit.test@example.com"
    state = "TX"
    sign_up_date = date(2026, 8, 25)

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

    print("Before commit:")
    print(f"\t{get_customer_by_id(cursor, cus_id)}")

    connection.commit()

    cursor.close()
    connection.close()

    # Reconnect to verify that committed data persists
    connection = connect_db()
    cursor = connection.cursor()

    print("Reconnected to Oracle Database")

    print("After commit:")
    print(f"\t{get_customer_by_id(cursor, cus_id)}\n")

    # Cleanup test data
    print(f"Deleting the added row: customer_id={cus_id}")

    cursor.execute(
        """
        DELETE FROM customers
         WHERE customer_id = :customer_id
        """,
        customer_id=cus_id
    )

    connection.commit()

    print("Looking for the added row to check if it has been deleted:")
    print(f"\t{get_customer_by_id(cursor, cus_id)}")

    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()