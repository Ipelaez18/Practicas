import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('BaseRelacional.db')

# Creación de la tabla
conn.execute('''CREATE TABLE EJEMPLO
       (ID INT PRIMARY KEY     NOT NULL,
       NOMBRE           TEXT    NOT NULL,
       EDAD            INT     NOT NULL);''')

# Inserción de datos en la tabla
conn.execute("INSERT INTO EJEMPLO (ID, NOMBRE, EDAD) \
      VALUES (01, 'Iván Pérez', 22)")

conn.execute("INSERT INTO EJEMPLO (ID, NOMBRE, EDAD) \
      VALUES (02, 'Erick Lilly', 22)")

# Guardar los cambios en la base de datos
conn.commit()

# Cierre de la conexión
conn.close()