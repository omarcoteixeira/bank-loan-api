import os
import urlparse
import psycopg2

from settings import DATABASE_URL

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(DATABASE_URL)


def execute():
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )

    cur = conn.cursor()

    cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

    cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
    cur.execute("SELECT * FROM test;")

    conn.commit()

    cur.close()
    conn.close()