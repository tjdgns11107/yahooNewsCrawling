# time_sqlite_model.py

import sqlite3
import time


def with_cursor(original_func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('time.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        rv = original_func(c, *args, **kwargs)
        conn.commit()
        conn.close()
        return rv
    return wrapper

@with_cursor
def create_time_table(c):
    c.execute("CREATE TABLE time (id integer PRIMARY KEY autoincrement, time text")

@with_cursor
def get_time_list(c):
    c.execute("SELECT * FROM time")
    return c.fetchall()


@with_cursor
def add_time(c):
    c.execute("INSERT INTO time (time) VALUES (?)",
        (time))


@with_cursor
def read_time(c, _id):
    c.execute("SELECT * FROM time WHERE id=?", (_id,))
    return c.fetchone()


@with_cursor
def modify_time(c, _id, time):
    c.execute("UPDATE time SET time=?, WHERE id=?",
        (time, _id))


@with_cursor
def remove_time(c, _id):
    c.execute("DELETE FROM time WHERE id=?", (_id,))