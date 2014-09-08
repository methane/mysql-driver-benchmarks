# Python MySQL driver benchmarks

## Environment

MacBook AIR 2013 (Core i5 1.3GHz)

Pythons:

* CPython 3.4.1
* PyPy 2.3.1

Connectors:

* PyMySQL 0.6.2
* mysqlclient (CPython only)
* MySQL Connector/Python 1.2.3

## Prepare

```
CREATE DATABASE mysqlbench;
```

Install `world.sql` into it.

`mysql -uroot mysqlbench < world.sql`

See http://dev.mysql.com/doc/world-setup/en/index.html

## CPython 3.4.1

### 1+1

```
$ time python3 bench1_onerow.py mysqlclient

real	0m0.313s
user	0m0.191s
sys	0m0.047s

$ time python3 bench1_onerow.py pymysql

real	0m0.445s
user	0m0.318s
sys	0m0.048s

$ time python3 bench1_onerow.py connector

real	0m0.534s
user	0m0.322s
sys	0m0.081s
```

### City

```
$ time python3 bench2_world.py mysqlclient

real	0m4.230s
user	0m3.113s
sys	0m0.087s

$ time python3 bench2_world.py pymysql

real	0m35.253s
user	0m33.380s
sys	0m0.185s

$ time python3 bench2_world.py connector

real	0m36.065s
user	0m30.603s
sys	0m4.693s
```

## PyPy 2.3.1

### 1+1

```
$ time pypy bench1_oneplusone.py pymysql

real	0m1.065s
user	0m0.863s
sys	0m0.094s

$ time pypy bench1_oneplusone.py connector

real	0m0.670s
user	0m0.439s
sys	0m0.106s
```

### City

```
$ time pypy bench2_world.py pymysql

real	0m5.037s
user	0m3.962s
sys	0m0.164s

$ time pypy bench2_world.py connector

real	0m11.665s
user	0m6.182s
sys	0m4.815s
```
