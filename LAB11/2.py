import psycopg2
from configparser import ConfigParser
import csv

def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return config

def connect(config):
    try:
        conn = psycopg2.connect(**config)
        print('Connected to the PostgreSQL server.')
        return conn
    except psycopg2.Error as e:
        print("Unable to connect to the database:", e)
        return None

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                contact_id SERIAL PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255),
                phone_number VARCHAR(20) NOT NULL
            )
        """)
        conn.commit()
        print("Table 'contacts' created successfully!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error creating table:", e)

def insert_or_update_contact(conn):
    try:
        cursor = conn.cursor()
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("Enter phone number: ")

        # Call the stored procedure to insert or update contact
        cursor.callproc('insert_or_update_contact', (first_name, last_name, phone_number))
        conn.commit()
        print("Contact inserted or updated successfully!")

    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting or updating contact:", e)

def insert_from_csv(conn, filename):
    try:
        cursor = conn.cursor()
        with open(filename, "r") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            next(csvreader)  # Skip header row
            for row in csvreader:
                first_name, last_name, phone_number = row
                # Call the stored procedure to insert or update contact
                cursor.callproc('insert_or_update_contact', (first_name, last_name, phone_number))
        conn.commit()
        print("Data inserted from CSV successfully!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting data from CSV:", e)

def update_contact(conn):
    try:
        cursor = conn.cursor()
        contact_id = input("Enter contact ID to update: ")
        first_name = input("Enter new first name (leave blank to keep current): ")
        last_name = input("Enter new last name (leave blank to keep current): ")
        phone_number = input("Enter new phone number (leave blank to keep current): ")

        update_query = "UPDATE contacts SET"
        update_fields = []

        if first_name:
            update_fields.append(f"first_name = '{first_name}'")
        if last_name:
            update_fields.append(f"last_name = '{last_name}'")
        if phone_number:
            update_fields.append(f"phone_number = '{phone_number}'")

        if update_fields:
            update_query += " " + ", ".join(update_fields)
            update_query += f" WHERE contact_id = {contact_id}"
            cursor.execute(update_query)
            conn.commit()
            print("Contact updated successfully!")
        else:
            print("No fields to update specified.")

    except psycopg2.Error as e:
        conn.rollback()
        print("Error updating contact:", e)

def query_contacts(conn):
    try:
        cursor = conn.cursor()
        print("Query contacts:")
        first_name = input("Enter first name (leave blank if not needed): ").strip()
        last_name = input("Enter last name (leave blank if not needed): ").strip()

        query = "SELECT * FROM contacts WHERE TRUE"

        if first_name:
            query += f" AND first_name = '{first_name}'"
        if last_name:
            query += f" AND last_name = '{last_name}'"

        cursor.execute(query)
        rows = cursor.fetchall()

        if rows:
            print("Matching contacts:")
            for row in rows:
                print(row)
        else:
            print("No matching contacts found.")

    except psycopg2.Error as e:
        print("Error querying contacts:", e)

def delete_contact(conn):
    try:
        cursor = conn.cursor()
        print("Delete contacts:")
        print("1. Delete a specific contact by phone number")
        print("2. Delete all contacts")

        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == '1':
            phone_number = input("Enter phone number of the contact to delete: ").strip()
            cursor.execute("DELETE FROM contacts WHERE phone_number = %s", (phone_number,))
            conn.commit()
            print("Contact deleted successfully!")

        elif choice == '2':
            confirm = input("Are you sure you want to delete all contacts? (yes/no): ").strip().lower()
            if confirm == 'yes':
                cursor.execute("DELETE FROM contacts")
                conn.commit()
                print("All contacts deleted successfully!")
            else:
                print("Deletion canceled.")

        else:
            print("Invalid choice. Please enter either 1 or 2.")

    except psycopg2.Error as e:
        conn.rollback()
        print("Error deleting contacts:", e)

def query_by_pattern(conn, pattern):
    try:
        cursor = conn.cursor()
        query = """
            SELECT * FROM contacts 
            WHERE first_name LIKE %s 
            OR last_name LIKE %s 
            OR phone_number LIKE %s
        """
        cursor.execute(query, (f'%{pattern}%', f'%{pattern}%', f'%{pattern}%'))
        rows = cursor.fetchall()

        if rows:
            print("Matching contacts:")
            for row in rows:
                print(row)
        else:
            print("No matching contacts found.")

    except psycopg2.Error as e:
        print("Error querying by pattern:", e)

def query_with_pagination(conn, limit, offset):
    try:
        cursor = conn.cursor()
        query = """
            SELECT * FROM contacts 
            LIMIT %s OFFSET %s
        """
        cursor.execute(query, (limit, offset))
        rows = cursor.fetchall()

        if rows:
            print("Contacts (Limited by Pagination):")
            for row in rows:
                print(row)
        else:
            print("No contacts found with the specified pagination.")

    except psycopg2.Error as e:
        print("Error querying with pagination:", e)

if __name__ == '__main__':
    try:
        config = load_config()
        conn = connect(config)

        if conn is not None:
            create_table(conn)

            try:
                while True:
                    print("\nChoose an option:")
                    print("1. Insert data (from console or CSV)")
                    print("2. Update contact information")
                    print("3. Query contacts")
                    print("4. Delete contacts")
                    print("5. Query by pattern (name, surname, or phone number)")
                    print("6. Query with pagination")
                    print("7. Exit")

                    choice = input("Enter your choice (1-7): ").strip()

                    if choice == '1':
                        insert_option = input("Add from terminal (T) or CSV file (C)? ").strip().lower()
                        if insert_option == 't':
                            insert_or_update_contact(conn)
                        elif insert_option == 'c':
                            csv_file = input("Enter CSV filename: ").strip()
                            insert_from_csv(conn, csv_file)
                        else:
                            print("Invalid option. Please try again.")

                    elif choice == '2':
                        update_contact(conn)

                    elif choice == '3':
                        query_contacts(conn)

                    elif choice == '4':
                        delete_contact(conn)

                    elif choice == '5':
                        pattern = input("Enter a pattern (name, surname, or phone number): ").strip()
                        query_by_pattern(conn, pattern)

                    elif choice == '6':
                        limit = int(input("Enter limit (number of records per page): "))
                        offset = int(input("Enter offset (starting record position): "))
                        query_with_pagination(conn, limit, offset)

                    elif choice == '7':
                        print("Exiting...")
                        break

                    else:
                        print("Invalid choice. Please enter a valid option (1-7).")

            finally:
                cursor = conn.cursor()
                cursor.execute("ALTER SEQUENCE contacts_contact_id_seq RESTART WITH 1")
                conn.commit()
                print("Contact_id sequence reset successfully.")

                conn.close()
                print("Connection closed.")

    except Exception as e:
        print("An error occurred:", e)
