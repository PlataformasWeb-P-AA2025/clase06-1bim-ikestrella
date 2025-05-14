import csv

from sqlalchemy.orm import sessionmaker
from crear_base import Saludo
from configuracion import engine

csv_filepath = "data/saludos_mundo.csv"

Session = sessionmaker(bind=engine)
session = Session()

with open(csv_filepath, mode='r', encoding='utf-8', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter='|')
    next(csv_reader)
    
    for row in csv_reader:
        saludo = Saludo(mensaje=row[0], tipo=row[1])
        session.add(saludo)

    session.commit()
