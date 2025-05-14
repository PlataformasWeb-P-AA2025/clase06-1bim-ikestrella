import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crear_base import Saludo

from configuracion import engine

csv_filepath = "saludos_mundo.csv"

Session = sessionmaker(bind=engine)
session = Session()


with open(csv_filepath, mode='r', encoding='latin1') as csvfile:
    csv_reader = csv.reader(csvfile)
    csv_data = []
    for row in csv_reader:
        lineas = row.text.strip().split('\n')
        datos = [linea.split('|') for linea in lineas[1:]]


        session.add(Saludo())


# se agrega los objetos
# a la sesión
# a la espera de un commit
# para agregar un registro a la base de
# datos
session.add()

# se confirma las transacciones
session.commit()
