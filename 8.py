import psycopg2

conn = psycopg2.connect(
    database="phonebook_db",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
)

cur = conn.cursor()


def search_user():
    pattern = input("Search name/phone: ")

    cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    rows = cur.fetchall()

    for r in rows:
        print(r)


def add_or_update():
    name = input("Name: ")
    phone = input("Phone: ")

    cur.execute("CALL add_or_update_user(%s, %s)", (name, phone))
    conn.commit()

    print("Saved!")


def delete_user():
    value = input("Name or phone: ")

    cur.execute("CALL delete_user(%s)", (value,))
    conn.commit()

    print("Deleted!")


def pagination():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    cur.execute("SELECT * FROM get_phonebook_page(%s, %s)", (limit, offset))
    rows = cur.fetchall()

    for r in rows:
        print(r)


def menu():
    while True:
        print("\n1.Search 2.Add 3.Delete 4.Page 0.Exit")
        c = input("> ")

        if c == "1":
            search_user()
        elif c == "2":
            add_or_update()
        elif c == "3":
            delete_user()
        elif c == "4":
            pagination()
        elif c == "0":
            break


menu()

cur.close()
conn.close()