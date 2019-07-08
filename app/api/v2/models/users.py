# DeliverIT2/app/api/v2/models/users.py
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
from passlib.hash import sha256_crypt

DATABASE = os.environ.get("DATABASE", '')
USER = os.environ.get("USER", '')
PASSWORD = os.environ.get("PASSWORD", '')
HOST = os.environ.get("HOST", '')
PORT = os.environ.get("PORT", '')

class Users:
    '''This class creates a blueprint for the user object'''

    def __init__(self):
        # create a database connection
        try:
            self.conn = psycopg2.connect(database=DATABASE,
                                         user=USER,
                                         password=PASSWORD,
                                         host=HOST,
                                         port=PORT)
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
        date_changed VARCHAR(255),\
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

    def add_role(self):
        # creates a new role of admin or regular user
        self.regular = "regular"
        self.admin = "admin"

        # add role query
        query = """ INSERT INTO roles(role_id, role_name)
            VALUES(1, '{}'),(2, '{}') ON CONFLICT (role_id) DO NOTHING""".format(
                self.regular,
                self.admin
        )

        self.cur.execute(query, (self.regular, self.admin))
        print('message: new role created')

    def add_user(self, username, email, password):
        # create a new regular user
        self.role_id = 1  # regular user role id
        self.username = ''.join(username.lower().split())
        self.email = ''.join(email.lower().split())
        self.password = sha256_crypt.encrypt(str(password))#hash the password
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

    def get_user_by_email(self, email, password):
        # retrieve a single user by their email address
        self.password_candidate = password
        query = """ SELECT * from users WHERE email = '{}'""".format(email)
        self.cur.execute(query)
        if self.cur.rowcount > 0:
            # get stored hash
            user_data = self.cur.fetchone()
            self.actual_password = user_data['password']

            # compare passwords
            if sha256_crypt.verify(self.password_candidate, self.actual_password):
                # passed
                return user_data
            else:
                # failed
                return None
        else:
            return None

    def add_admin(self, username, email, password):
        # create an admin
        self.role_id = 2  # admin role id
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

        # add admin query
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
        return "message: new admin created"

    def get_admin_by_email(self, email, password):
        # retrieve a single user by their email address
        self.password_candidate = password
        query = """ SELECT * from users WHERE email = '{}'""".format(email)
        self.cur.execute(query)
        if self.cur.rowcount > 0:
            # get stored hash
            user_data = self.cur.fetchone()
            self.actual_password = user_data['password']

            # compare passwords
            if sha256_crypt.verify(self.password_candidate, self.actual_password):
                # passed
                return user_data
            else:
                # failed
                return None
        else:
            return None

    def user_access(self, email):
        #retrieve user by email
        query = """ SELECT * from users WHERE email = '{}'""".format(email)
        self.cur.execute(query)
        if self.cur.rowcount > 0:
            user_data = self.cur.fetchone()
            return user_data
        return None

    def update_user(self, username, email, password):
        #update user information
        self.username = ''.join(username.lower().split())
        self.email = email
        self.password = sha256_crypt.encrypt(str(password))
        self.date_changed = str(datetime.now())

        # check username query
        checkusername_query = """ SELECT * from users WHERE username = '{}'""".format(
            self.username)
        self.cur.execute(checkusername_query)
        user_data = self.cur.fetchone()

        if self.cur.rowcount > 0:
            if self.username == user_data['username']:
                return None
            else:
                return "message: Username already in use, please try again"

        # add admin query
        query = """ UPDATE users SET(
            username,
            password,
            date_changed)=
            ('{}', '{}', '{}') WHERE email = '{}'""".format(
                self.username,
                self.password,
                self.date_changed,
                self.email
        )

        self.cur.execute(query, (self.username, self.password, self.email))
        return "message: user updated"

    def get_all_users(self):
        #get all users and their details
        get_all_users_query = """ SELECT user_id, username, email, date_created, date_changed 
        FROM users WHERE role_id = '1'"""

        self.cur.execute(get_all_users_query)
        if self.cur.rowcount > 0:
            all_users = self.cur.fetchall()

            return all_users
