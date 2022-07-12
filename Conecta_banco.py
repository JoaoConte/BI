import pyodbc  # Biblioteca MSSQL
import cx_Oracle # Blblioteca Oracle

def conecta_sql(servidor,banco): # Conecta Database SQL Server
    try:
        cbd_sql = pyodbc.connect("Driver=SQL Server; Server=" + servidor + "; Database=" + banco + "; TrustedConnection=yes")
        conn_db = cbd_sql.cursor()
    except:
        sg.popup('Não consegui conectar o banco de dados ' + banco)
    return conn_db

def conecta_ora(banco, ora_conn): # Conecta Database Oracle
    try:
        cbd_ora = cx_Oracle.connect(ora_conn)
        conn_db = cbd_ora.cursor()
    except:
        sg.popup('Não consegui conectar o banco de dados ' + banco)    
    return conn_db
    