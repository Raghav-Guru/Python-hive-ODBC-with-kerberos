# Python-hive-ODBC-with-kerberos

This python script execute a hive sql statement using pyodbc module and Hive ODBC driver. 

This script is  verified in a kerberized environment. Before using the script it is assumed that  the client where this script execute is already configured for proper kdc in /etc/krb5.conf and also user obtained the tgt.

-->Install Hive ODBC driver : 

    #wget https://public-repo-1.hortonworks.com/HDP/hive-odbc/2.1.16.1023/Linux/EL7/hive-odbc-native-2.1.16.1023-1.el7.x86_64.rpm
    #yum install ./hive-odbc-native-2.1.16.1023-1.el7.x86_64.rpm

 -->Configure odbc driver configuration: 

    #vi /var/tmp/odbc.ini
    
    [ODBC]
    
    [ODBC Data Sources]
    HWX_KERB
    
    [HWX_KERB]
    Description=Hortonworks Hive ODBC Driver
    Driver=/usr/lib/hive/lib/native/Linux-amd64-64/libhortonworkshiveodbc64.so
    HOST=c416-node3.raghav.com:2181
    ZKNamespace=hiveserver2
    Schema=default
    ServiceDiscoveryMode=1
    HiveServerType=2
    AuthMech=1
    KrbHostFQDN=_HOST
    KrbServiceName=hive
    KrbRealm=HWX.COM

-->Install pyodbc module (this module will need gcc and gcc-c++ pkgs installed on the linux host)

    #pip install pyodbc

-->Copy the script pyhive.py
-->On Linux host get the kerberos ticket with user credentials : 

    # kinit hr1
    Password for hr1@HWX.COM:


-->Export the ODBC driver variables and execute the python script with required options: 

    #export HORTONWORKSHIVEINI=/usr/lib/hive/lib/native/Linux-amd64-64/hortonworks.hiveodbc.ini
    #export ODBCINI=/var/tmp/odbc.ini
    # python pyhive.py --dsn HWX_KERB --sql 'show tables'
    (u'test1', )
    # python testhive.py --dsn HWX_KERB --sql 'create table test2(col1 string);'
    No results.  Previous SQL was not a query.
    # python pyhive.py --dsn HWX_KERB --sql 'show tables;'
    (u'test1', )
    (u'test2', )

