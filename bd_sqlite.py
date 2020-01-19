import sqlite3
from sqlite3 import Error
from numpy import array

def sql_connection():
    try:
        con = sqlite3.connect('ateam.db')
        return con
    except Error:
        print(Error)

#obj debe ser un string = 'prueba'
def insert_producto(con, obj):
    cursorObj = con.cursor()
    sql= 'insert into producto(nombre) values ' +"('"+obj+"')"
    cursorObj.execute(sql)
    con.commit()

#obj debe ser un string = 'prueba' el cual es el nombre
def delete_producto(con, obj):
    cursorObj = con.cursor()
    sql= 'delete from producto where nombre= ' +"('"+obj+"')"
    print(sql)
    # .rowcount
    n_eliminados=cursorObj.execute(sql).rowcount
    con.commit()
    return n_eliminados

# debe recibir un arreglo=> obj = array([1,'grada'])
def update_producto(con, obj):
    cursorObj = con.cursor()
    id= obj[0]
    nombre= obj[1]
    sql= "update producto set nombre='"+nombre+"' where id ="+id
    print (sql)
    cursorObj.execute(sql)
    # .rowcount
    n_modificados=cursorObj.execute(sql).rowcount
    con.commit()
    return n_modificados

def listar_productos(con):
    cursorObj = con.cursor()
    cursorObj.execute("select * from producto")
    rows = cursorObj.fetchall()
    return rows

def listar_eventos(con):
    cursorObj = con.cursor()
    cursorObj.execute("select * from evento")
    rows = cursorObj.fetchall()
    return rows

### listar usuarios
def listar_usuarios(con):
    cursorObj = con.cursor()
    cursorObj.execute("select * from usuario")
    rows = cursorObj.fetchall()
    return rows


## recibe un obj => arr = array(['user','pass'])
def verificar_usuario(con, obj):
    cursorObj = con.cursor()
    usuario = obj[0]
    print(usuario)
    contraseña = obj[1]
    print(contraseña)

    sql="select * from usuario where user='"+usuario+"' and pass='"+contraseña+"'"
    cursorObj.execute(sql)
    # acierto=cursorObj.execute(sql).rowcount
    con.commit()
    rows = cursorObj.fetchall()

    return rows

#obj debe ser un string = 'prueba'
def listar_eventos_hoy(con):
    cursorObj = con.cursor()
    sql= "select * from evento"
    cursorObj.execute(sql)
    con.commit()
    rows = cursorObj.fetchall()
    return rows

# miPack = array([placa, fecha_in, peso_neto, producto])
def insert_evento(con, obj):
    cursorObj = con.cursor()
    placa= obj[0]
    fecha_in= obj[1].strftime("%m/%d/%Y, %H:%M:%S")

    peso_neto= str(obj[2])
    producto= str(obj[3])
    #INSERT INTO table_name (column1, column2, column3, ...)
    #VALUES (value1, value2, value3, ...);
    sql= "insert into evento (placa, fecha_in, peso_neto, producto) values ('"+placa+"','"+fecha_in+"',"+peso_neto+","+producto+")"
    n_modificados=cursorObj.execute(sql).rowcount
    con.commit()
    return n_modificados



con = sql_connection()
# # asd = 'sopa'
# arr = array([1,'grada'])
# insert_producto(con,asd)
# delete_producto(con, asd)
# update_producto(con, arr)
#
# rows=listar_productos(con)
# for row in rows:
#     print(row)

# arr = array(['admin','admin'])
# print(len(verificar_usuario(con, arr)))
