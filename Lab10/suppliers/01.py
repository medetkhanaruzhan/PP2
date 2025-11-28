import psycopg2
import csv

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="aru2006",
    host="localhost",
    port="5434"
)

cur = conn.cursor()

def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts(
            id SERIAL PRIMARY KEY,
            name VARCHAR(40) NOT NULL,
            number VARCHAR(20) NOT NULL UNIQUE
        );
    """)
    conn.commit()

def insert_from_console():
    name = input("Name: ")
    number = input("Number: ")
    cur.execute("""
        INSERT INTO contacts (name, number)
        VALUES (%s, %s)
        ON CONFLICT (number) DO NOTHING;
    """, (name, number))
    conn.commit()

def insert_from_csv():
    path = "/Users/aruzhanmedetkhan/Desktop/PP2/Lab10/contacts.csv"
    with open(path, newline='') as csv_file:
        r = csv.reader(csv_file)
        for row in r:
            if len(row) != 2:
                continue
            cur.execute("""
                INSERT INTO contacts (name, number)
                VALUES (%s, %s)
                ON CONFLICT (number) DO NOTHING;
            """, (row[0], row[1]))
        conn.commit()

def delete_contact():
    print("\nIf you want to delete contact \n1. By name\n2. By number")
    n = int(input())
    if n == 1:
        name = input("Name: ")
        cur.execute("DELETE FROM contacts WHERE name = %s;", (name,))
    elif n == 2:
        number = input("Number: ")
        cur.execute("DELETE FROM contacts WHERE number = %s;", (number,))
    conn.commit()

def update_contact():
    print("\nYou want to update \n1. By contact's number\n2. By contact's name")
    n = int(input())
    if n == 1:
        number = input("Number: ")
        name = input("Name to change: ")
        cur.execute("""
            UPDATE contacts 
            SET name = %s
            WHERE number = %s;
        """, (name, number))
    elif n == 2:
        name = input("Name: ")
        number = input("Number to change: ")
        cur.execute("""
            UPDATE contacts 
            SET number = %s
            WHERE name = %s;
        """, (number, name))
    conn.commit()

def search_contacts():
    print("\nHow you want search")
    print("1. By name")
    print("2. By number")
    print("3. By part of name")
    print("4. By part of number")
    print("5. Show all")
    n = int(input())
    if n == 1:
        name = input()
        cur.execute("SELECT * FROM contacts WHERE name = %s;", (name,))
    elif n == 2:
        number = input()
        cur.execute("SELECT * FROM contacts WHERE number = %s;", (number,))
    elif n == 3:
        na = input()
        cur.execute("SELECT * FROM contacts WHERE name LIKE %s;", (f'%{na}%',))
    elif n == 4:
        num = input()
        cur.execute("SELECT * FROM contacts WHERE number LIKE %s;", (f'%{num}%',))
    elif n == 5:
        cur.execute("SELECT * FROM contacts ORDER BY id;")
    contacts = cur.fetchall()
    print("\nID\tName\tNumber\n---------------------------")
    for contact in contacts:
        print(f"{contact[0]}\t{contact[1]}\t{contact[2]}")

create_table()

run = True
while run:
    print("\nOptions:\n1. Insert\n2. Delete\n3. Update\n4. Search\n5. Quit")
    n = int(input())
    if n == 1:
        print("\n1. By console\n2. By csv")
        m = int(input())
        if m == 1:
            insert_from_console()
        elif m == 2:
            insert_from_csv()
    elif n == 2:
        delete_contact()
    elif n == 3:
        update_contact()
    elif n == 4:
        search_contacts()
    elif n == 5:
        run = False
        cur.close()
        conn.close()