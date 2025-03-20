#Conexión con la base de datos

#Importación de las librerías

from sqlalchemy import create_engine, event #Llamar la librería para la comunicación con la base de datos
from sqlalchemy.orm import sessionmaker #abrir un canal hacia la base de datos
from sqlalchemy.engine import Engine

#Datos para la conexión a base de datos

dataBaseName = "logisticauribebd"
userName = "root"
userPassword = ""
connectionPort = 3306
server = "localhost"

#Creando la conexión

dataBaseConnection = f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{connectionPort}/{dataBaseName}"

#Creo el motor de conexión

engine = create_engine(dataBaseConnection)

#Abrir la sesión con la base de datos

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)