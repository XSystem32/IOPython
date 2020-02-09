from sqlite3 import connect

with connect('C:\\users\\thanatos\\PycharmProjects\\FileIO\\Filehandling\\example.db') as conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE cars(id int PRIMARY KEY, name text, model text, age INTEGER)')
    cur.execute('INSERT INTO cars(id, name, model, age) VALUES (1, "Skoda", "Octavia", 2013)')
    cur.execute('INSERT INTO cars(id, name, model, age) VALUES (2, "VW", "Arteon", 2019)')
    cur.execute('INSERT INTO cars(id, name, model, age) VALUES (3, "BMW", "M3", 2010)')
    cur.execute('INSERT INTO cars(id, name, model, age) VALUES (4, "Seat", "Mii", 2015)')
    cur.execute('INSERT INTO cars(id, name, model, age) VALUES (5, "Toyota", "Camry", 2009)')

    for i in cur.execute('SELECT * FROM cars'):
        print(i)