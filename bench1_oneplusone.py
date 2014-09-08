import sys
try:
    import MySQLdb
except ImportError:
    pass
import pymysql
import mysql.connector


def bench(conn):
    cur = conn.cursor()
    for _ in range(1000):
        cur.execute("SELECT 1+1")
        x = cur.fetchall()[0][0]
        assert x == 2


if __name__ == '__main__':
    connector = sys.argv[1]
    cfg = {'user': 'root', 'host': '127.0.0.1', 'database': 'mysqlbench'}
    if connector == 'connector':
        con = mysql.connector.connect(**cfg)
    elif connector == 'pymysql':
        con = pymysql.connect(**cfg)
    elif connector == 'mysqlclient':
        cfg['db'] = cfg.pop('database')
        con = MySQLdb.connect(**cfg)
    else:
        sys.exit("connector, pymysql or mysqlclient")

    bench(con)
