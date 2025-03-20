from pydantic import BaseModel, Field
from datetime import date

#Los DTO son objetos d etransferencia de datos
class ProveedorDTO(BaseModel): #EL DTO DE RECEPCION
    nombres:str
    documento:str
    direccion:str
    ciudad:str
    representante:str
    telefonoContacto:str
    correo:str
    fechaEnvio:date
    costoEnvio:int
    descripcion:str

class ProveedorDTOEnvio(BaseModel): #EL DTO DE RESPUESTA
    id:int
    nombres:str
    documento:str
    direccion:str
    ciudad:str
    representante:str
    telefonoContacto:str
    correo:str
    fechaEnvio:date
    costoEnvio:int
    descripcion:str

class LogisticaDTO(BaseModel): #EL DTO DE RECEPCION
    nombre_encargado:str
    correo_encargado:str
    telefono_encargado:str
    fecha_receptor:date
    detalles:str

class LogisticaDTOEnvio(BaseModel): #EL DTO DE RESPUESTA
    id_logistica:int
    nombre_encargado:str
    correo_encargado:str
    telefono_encargado:str
    fecha_receptor:date
    detalles:str