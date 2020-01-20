import sqlite3
from sqlite3 import Error
from numpy import array
from datetime import date
from datetime import datetime

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

# entrada: id, peso_carga, peso_out
def insert_evento_salida(con, obj):
    cursorObj = con.cursor()
    id=  str(obj[0])
    peso_carga=  str(obj[1])
    peso_out=  str(obj[2])
    fecha_aux=datetime.now()
    fecha_out= fecha_aux.strftime("%m/%d/%Y, %H:%M:%S")

    #INSERT INTO table_name (column1, column2, column3, ...)
    #VALUES (value1, value2, value3, ...);
    sql= "update evento set "+"fecha_out='"+fecha_out+"', peso_in="+peso_carga+", peso_out="+peso_out+" where id="+id
    print(sql)
    cursorObj.execute(sql)
    con.commit()
    return True

#entrada array con placa, salida es id y pesoneto del evento mas reciente segun la placa
def buscar_evento(con, obj):
    cursorObj = con.cursor()
    placa= obj[0]
    # fecha_in= obj[1].strftime("%m/%d/%Y, %H:%M:%S")
    fecha_salida=datetime.now()
    sql= "select id, peso_neto from evento where placa='"+placa+"'  ORDER BY fecha_in DESC"
    # peso_neto= str(obj[2])
    # producto= str(obj[3])
    #INSERT INTO table_name (column1, column2, column3, ...)
    #VALUES (value1, value2, value3, ...);
    cursorObj.execute(sql)
    con.commit()
    rows = cursorObj.fetchone()

    return rows

def crear_producto(con,obj):
    cursorObj = con.cursor()
    nombre=obj[1]
    id=str(obj[0])
    sql= "insert into producto (id,nombre) values "+"("+id+",'"+nombre+"')"
    cursorObj.execute(sql)
    con.commit()
    return True

def update_producto(con,obj):
    cursorObj = con.cursor()
    nombre=obj[1]
    id=str(obj[0])
    sql= "update producto set id ="+id+", nombre='"+nombre+"' where id="+id
    cursorObj.execute(sql)
    con.commit()
    return True

def eliminar_producto(con,obj):
    cursorObj = con.cursor()
    id= str(obj[0])
    #DELETE FROM table_name WHERE condition;
    sql= "delete from producto where id= "+id
    cursorObj.execute(sql)
    con.commit()
    return True

def crear_usuario(con,obj):
    cursorObj = con.cursor()
    us=obj[0]
    pw=obj[1]
    sql= "insert into usuario (user, pass) values "+"('"+obj[0]+"','"+obj[1]+"')"
    cursorObj.execute(sql)
    con.commit()
    return True

def eliminar_usuario(con,obj):
    cursorObj = con.cursor()
    id= str(obj[0])
    print (id)
    print (obj)
    #DELETE FROM table_name WHERE condition;
    sql= "delete from usuario where user= '"+id+"'"
    cursorObj.execute(sql)
    con.commit()
    return True

def eliminar_evento(con,obj):
    cursorObj = con.cursor()
    # id= str(obj[0])
    id = str(obj)
    # print (obj)
    #DELETE FROM table_name WHERE condition;
    sql= "delete from evento where id= "+id
    cursorObj.execute(sql)
    con.commit()
    return True

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
