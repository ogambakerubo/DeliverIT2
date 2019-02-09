# DeliverIT2/app/api/v2/models/users.py
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
from passlib.hash import sha256_crypt


class Users:
    '''This class creates a blueprint for the user object'''

    def __init__(self):
        # create a database connection
        try:
            self.conn = psycopg2.connect(database="deliverit2_test_db",
                                         user="postgres",
                                         password="Cake-By-The-Ocean",
                                         host="localhost",
                                         port="5432")
            self.conn.autocommit = True
            self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

            print('message: Database Connection Successful')

        except psycopg2.DatabaseError as err:

            print('message: Something went wrong {}'.format(err))

    def create_schemas(self):
        # create user schemas
        roles_table = "\
        CREATE TABLE IF NOT EXISTS roles (\
        role_id serial PRIMARY KEY,\
        role_name VARCHAR(255) NOT NULL UNIQUE)"
        # roles_table schema
        self.cur.execute(roles_table)

        roles_test_table = "CREATE TABLE IF NOT EXISTS roles_test (LIKE roles)"
        # roles_test schema
        self.cur.execute(roles_test_table)

        users_table = "\
        CREATE TABLE IF NOT EXISTS users (\
        user_id serial PRIMARY KEY,\
        role_id integer NOT NULL,\
        username VARCHAR(255) NOT NULL UNIQUE,\
        password VARCHAR(255) NOT NULL,\
        email VARCHAR(255) NOT NULL UNIQUE,\
        date_created VARCHAR(255) NOT NULL,\
        FOREIGN KEY(role_id) REFERENCES roles(role_id) ON UPDATE CASCADE ON DELETE CASCADE)"
        # users_table schema
        self.cur.execute(users_table)

        users_test_table = "CREATE TABLE IF NOT EXISTS users_test (LIKE users)"
        # users_test_table schema
        self.cur.execute(users_test_table)

        unsub_table = "\
        CREATE TABLE IF NOT EXISTS unsub (\
        user_id serial PRIMARY KEY,\
        role_id integer NOT NULL,\
        username VARCHAR(255) NOT NULL UNIQUE,\
        password VARCHAR(255) NOT NULL,\
        email VARCHAR(255) NOT NULL UNIQUE,\
        date_created VARCHAR(255) NOT NULL,\
        date_unsubbed VARCHAR(255) NOT NULL,\
        FOREIGN KEY(role_id) REFERENCES roles(role_id) ON UPDATE CASCADE ON DELETE CASCADE)"
        # unsub_table schema
        self.cur.execute(unsub_table)

        unsub_test_table = "CREATE TABLE IF NOT EXISTS unsub_test (LIKE unsub)"
        # users_test_table schema
        self.cur.execute(unsub_test_table)

        print('message: tables created successfully')

    def add_role(self, role_name):
        # creates a new role of admin or regular user
        self.role_name = role_name

        # add role query
        query = """ INSERT INTO roles(
            role_name)
            VALUES('{}')""".format(
                self.role_name
        )

        self.cur.execute(query, (role_name,))
        print('message: new role created')

    def add_user(self, username, email, password):
        # create a new regular user
        self.role_id = 1 #regular user role id
        self.username = ''.join(username.lower().split())
        self.email = ''.join(email.lower().split())
        self.password = sha256_crypt.encrypt(str(password))
        self.date_created = str(datetime.now())

        # check username query
        checkusername_query = """ SELECT * from users WHERE username = '{}'""".format(
            self.username)
        self.cur.execute(checkusername_query)
        if self.cur.rowcount > 0:
            return "message: Username already in use, please try again"

        # check email query
        checkemail_query = """ SELECT * from users WHERE email = '{}'""".format(
            self.email)
        self.cur.execute(checkemail_query)
        if self.cur.rowcount > 0:
            return "message: Email already in use, please try again"

        # add user query
        query = """ INSERT INTO users(
            role_id,
            username,
            password,
            email,
            date_created)
            VALUES('{}', '{}', '{}', '{}', '{}')""".format(
                self.role_id,
                self.username,
                self.password,
                self.email,
                self.date_created
        )

        self.cur.execute(query, (self.username, self.password, self.email))
        return "message: new user created"