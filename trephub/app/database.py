import sqlite3 as sql

def connect( dbname ):
    dbconnecton = None
    try:
        dbconnecton = sql.connect( dbname )
    except sql.Error, e:
        print "Error %s:" % e.args[0]
        return None
    finally:
        return dbconnecton

def drop_table( dbname, table ):
    dbconnecton = connect( dbname )
    if dbconnecton:
        cursor = dbconnecton.cursor()
        cursor.execute( 'DROP TABLE IF EXISTS %s' % table )
        dbconnecton.close()
        return 'Table %s DROPPED' % table
    else:
        return 'Unable to connect to DB ' + dbname

def get_sqlite_version( dbname ):
    dbconnecton = connect( dbname )
    if dbconnecton:
        cursor = dbconnecton.cursor()
        cursor.execute( 'SELECT SQLITE_VERSION()' )
        
        data = cursor.fetchone()
        dbconnecton.close()
        return 'SQLIte version: %s ' % data
    else:
        return 'Unable to connect to DB ' + dbname
        
def create_table( table, dbname ):
    dbconnecton = connect( dbname )
    if dbconnecton:
        cursor = dbconnecton.cursor()
        cursor.execute( "CREATE TABLE IF NOT EXISTS %s( Id INT, Event TEXT, Date TEXT )" % table )
        dbconnecton.close()
        return 'Table %s CREATED ' % table
    else:
        return 'Unable to connect to DB ' + dbname

def insert_table( dbname, table, data ):
    dbconnecton = connect( dbname )
    if dbconnecton:
        dbconnecton.execute( "INSERT INTO Cars( Id, Name, Price) \
            VALUES( 1, '%s', 25 )" % data )
        dbconnecton.commit()
        dbconnecton.close()
        return 'Data INSERTED into table %s ' % table
    else:
        return 'Unable to connect to DB ' + dbname        