#!/usr/bin/env python
import pyodbc
import argparse

CONNECTION_STRING_EXAMPLE = ';'.join('''
Description=Hortonworks Hive ODBC Driver
Driver=/usr/lib/hive/lib/native/Linux-amd64-64/libhortonworkshiveodbc64.so
HOST=c416-node3.raghav.com:2181
ZKNamespace=hiveserver2
Schema=default
ServiceDiscoveryMode=1
HiveServerType=2
AuthMech=1
UID=
KrbHostFQDN=_HOST
KrbServiceName=hive
KrbRealm=HWX.COM
SSL=0
TwoWaySSL=0
ClientCert=
ClientPrivateKey=
ClientPrivateKeyPassword=
'''.splitlines())


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dsn', '-d', type=str, required=True,
        help='The DSN name from $HOME/.odbc.ini to use for this connection.')
    parser.add_argument('--sql', '-s', type=str, required=True,
        help='The SQL statement to execute')
    return parser.parse_args()


def execute_query(sql, dsn):
    try:
        connect_string = 'DSN=%(dsn)s' % locals()
        conn = pyodbc.connect(connect_string, autocommit=True)
        cursor = conn.cursor()
        cursor.execute(sql)
        for row in cursor:
            print row
    except Exception as e:
        print e
    finally:
        cursor.close()
        conn.close()

###########################################################
# MAIN
###########################################################
if __name__ == '__main__':
    args = parse_args()
    execute_query(args.sql, args.dsn)
