import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('BaseRelacional.db')

# Consulta a la base de datos
cursor = conn.execute("SELECT * from EJEMPLO")
print("ID\tNOMBRE\t\tEDAD")
for row in cursor:
   print(row[0], end="\t")
   print(row[1], end="\t")
   print(row[2])
print("\n\n\n\n")
# Cierre de la conexión
conn.close()