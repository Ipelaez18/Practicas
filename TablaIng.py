import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('BaseRelacional.db')

conn.execute("DROP TABLE EJEMPLO")

# Creación de la tabla
conn.execute('''CREATE TABLE EJEMPLO
       (ID INT PRIMARY KEY     NOT NULL,
       NOMBRE           TEXT    NOT NULL,
       EDAD            INT     NOT NULL);''')

# Inserción de datos en la tabla
conn.execute("INSERT INTO EJEMPLO (ID, NOMBRE, EDAD) \
      VALUES (01, 'Iván Pérez', 22)")

conn.execute("INSERT INTO EJEMPLO (ID, NOMBRE, EDAD) \
      VALUES (02, 'Erick Lilly', 21)")

conn.execute("INSERT INTO EJEMPLO (ID, NOMBRE, EDAD) \
      VALUES (03, 'Ximena Coria', 22)")

conn.execute("INSERT INTO EJEMPLO (ID, NOMBRE, EDAD) \
      VALUES (04, 'María Castillo', 21)")

# Guardar los cambios en la base de datos
conn.commit()

# Cierre de la conexión
conn.close()