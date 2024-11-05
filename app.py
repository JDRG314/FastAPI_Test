from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import get_db_connection, create_table

# Crear la tabla al iniciar la aplicación
create_table()

app = FastAPI()

# Definir el esquema de datos para la solicitud
class Candidato(BaseModel):
    dni: str
    nombre: str
    apellido: str

@app.post("/candidato")
async def crear_candidato(candidato: Candidato):
    # Obtener la conexión a la base de datos
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Verificar si el DNI ya existe
    cursor.execute("SELECT * FROM candidatos WHERE dni = ?", (candidato.dni,))
    existing_candidato = cursor.fetchone()
    if existing_candidato:
        conn.close()
        raise HTTPException(status_code=400, detail="El DNI ya está registrado.")
    
    # Insertar los datos del candidato
    cursor.execute(
        "INSERT INTO candidatos (dni, nombre, apellido) VALUES (?, ?, ?)",
        (candidato.dni, candidato.nombre, candidato.apellido)
    )
    conn.commit()
    conn.close()

    return {"message": "Candidato registrado correctamente", "candidato": candidato}
