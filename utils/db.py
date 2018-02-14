import psycopg2
from urllib import parse

from settings import DATABASE_URL


def execute():
    parse.uses_netloc.append("postgres")
    url = parse.urlparse(DATABASE_URL)

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
    print cur.execute("SELECT * FROM test;")

    conn.commit()

    cur.close()
    conn.close()