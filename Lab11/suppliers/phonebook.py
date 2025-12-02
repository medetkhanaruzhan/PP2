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

# создаем процедуру и функции внутри postgeSQL
def create_functions_and_procedures():

    cur.execute("DROP FUNCTION IF EXISTS find_contacts(TEXT);")
    cur.execute("DROP FUNCTION IF EXISTS get_contacts_paginated(INT, INT);")

    #poisk po patterny
    cur.execute("""
        CREATE OR REPLACE FUNCTION find_contacts(pattern TEXT)
        RETURNS TABLE(id INT, name VARCHAR, number VARCHAR)
        AS $$
        BEGIN
            RETURN QUERY
            SELECT contacts.id, contacts.name, contacts.number
            FROM contacts
            WHERE contacts.name ILIKE '%' || pattern || '%'
               OR contacts.number ILIKE '%' || pattern || '%'
            ORDER BY contacts.id;
        END;
        $$ LANGUAGE plpgsql;
    """)


    # zdes' insert or update contact
    cur.execute("""
        CREATE OR REPLACE PROCEDURE insert_or_update_contact(p_name TEXT, p_phone TEXT)
        LANGUAGE plpgsql
        AS $$
        BEGIN
            INSERT INTO contacts(name, number)
            VALUES (p_name, p_phone)
            ON CONFLICT (number)
            DO UPDATE SET name = EXCLUDED.name;
        END;
        $$;
    """)

    #insert frokm csv
    cur.execute("""
        CREATE OR REPLACE PROCEDURE insert_many_contacts(
            IN names TEXT[],
            IN phones TEXT[],
            OUT incorrect TEXT[]
        )
        LANGUAGE plpgsql
        AS $$
        DECLARE
            i INT;
            bad TEXT[] := '{}';
        BEGIN
            FOR i IN 1..array_length(names, 1) LOOP

                IF phones[i] !~ '^[0-9]+$' THEN
                    bad := array_append(bad, names[i] || ' - ' || phones[i]);
                    CONTINUE;
                END IF;

                INSERT INTO contacts(name, number)
                VALUES (names[i], phones[i])
                ON CONFLICT (number)
                DO UPDATE SET name = EXCLUDED.name;

            END LOOP;

            incorrect := bad;
        END;
        $$;
    """)

   #pagination
    cur.execute("""
        CREATE OR REPLACE FUNCTION get_contacts_paginated(limit_n INT, offset_n INT)
        RETURNS TABLE(id INT, name VARCHAR, number VARCHAR)
        AS $$
        BEGIN
            RETURN QUERY
            SELECT contacts.id, contacts.name, contacts.number
            FROM contacts
            ORDER BY contacts.id
            LIMIT limit_n
            OFFSET offset_n;
        END;
        $$ LANGUAGE plpgsql;
    """)

    #delete contact
    cur.execute("""
        CREATE OR REPLACE PROCEDURE delete_contact_proc(p_value TEXT)
        LANGUAGE plpgsql
        AS $$
        BEGIN
            DELETE FROM contacts
            WHERE name = p_value OR number = p_value;
        END;
        $$;
    """)

    conn.commit()


def insert_from_console():
    name = input("Name: ")
    number = input("Number: ")
    cur.execute("CALL insert_or_update_contact(%s, %s);", (name, number))
    conn.commit()
    print("Contact inserted/updated.\n")


def insert_from_csv():
    path = "/Users/aruzhanmedetkhan/Desktop/PP2/Lab11/suppliers/contacts.csv"

    names = []
    phones = []

    with open(path, newline='') as csv_file:
        r = csv.reader(csv_file)
        for row in r:
            if len(row) == 2:
                names.append(row[0])
                phones.append(row[1])

    cur.execute("CALL insert_many_contacts(%s, %s, %s);", (names, phones, None))
    conn.commit()
    print("CSV imported.\n")


def delete_contact():
    value = input("Enter name OR number to delete: ")
    cur.execute("CALL delete_contact_proc(%s);", (value,))
    conn.commit()
    print("Deleted.\n")


def update_contact():
    print("\nUpdate:")
    print("1. Change name by phone")
    print("2. Change phone by name")

    choice = int(input("Choose: "))

    if choice == 1:
        number = input("Current number: ")
        new_name = input("New name: ")
        cur.execute("UPDATE contacts SET name = %s WHERE number = %s;", (new_name, number))

    elif choice == 2:
        name = input("Current name: ")
        new_number = input("New phone: ")
        cur.execute("UPDATE contacts SET number = %s WHERE name = %s;", (new_number, name))

    conn.commit()
    print("Updated.\n")


def search_contacts():
    pattern = input("Enter search pattern: ")
    cur.execute("SELECT * FROM find_contacts(%s);", (pattern,))
    rows = cur.fetchall()

    print("\nID\tName\tNumber\n---------------------------")
    for r in rows:
        print(f"{r[0]}\t{r[1]}\t{r[2]}")
    print()


def pagination():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
    rows = cur.fetchall()

    print("\nID\tName\tNumber\n---------------------------")
    for r in rows:
        print(f"{r[0]}\t{r[1]}\t{r[2]}")
    print()


create_table()
create_functions_and_procedures()

run = True
while run:
    print("Options:")
    print("1. Insert Contact")
    print("2. Insert from CSV")
    print("3. Delete Contact")
    print("4. Update Contact")
    print("5. Search")
    print("6. Pagination")
    print("7. Quit")

    choose = int(input("Enter option: "))

    if choose == 1:
        insert_from_console()
    elif choose == 2:
        insert_from_csv()
    elif choose == 3:
        delete_contact()
    elif choose == 4:
        update_contact()
    elif choose == 5:
        search_contacts()
    elif choose == 6:
        pagination()
    elif choose == 7:
        print("Goodbye!")
        run = False

cur.close()
conn.close()