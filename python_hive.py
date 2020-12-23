#!/usr/bin/env python
import pyodbc
import argparse

### Uncomment lines for AuthMech=2 and comment lines without user arg to re-use code for user authn (when hive is configured for NONE authentication)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dsn', '-d', type=str, required=True,
        help='The DSN name from $HOME/.odbc.ini to use for this connection.')
    parser.add_argument('--sql', '-s', type=str, required=True,
        help='The SQL statement to execute')
  ##parser.add_argument('--user', '-u', type=str, required=True, # For AuthMech=2
        ##help='User name')
    return parser.parse_args()

###def execute_query(sql, dsn,user):    ### for AuthMech=2
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
    ### execute_query(args.sql, args.dsn,args.user) ## For AuthMech=2
