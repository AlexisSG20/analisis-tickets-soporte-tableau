import os
import random
from datetime import datetime, timedelta

import pandas as pd


# =========================
# CONFIGURACIÓN GENERAL
# =========================

random.seed(42)

TOTAL_TICKETS = 2500

FECHA_INICIO = datetime(2025, 1, 1)
FECHA_FIN = datetime(2025, 12, 31)

RUTA_RAW = "data/raw/tickets_soporte_raw.csv"
RUTA_PROCESSED = "data/processed/tickets_soporte.csv"


# =========================
# CATÁLOGOS SIMULADOS
# =========================

canales = ["Correo", "Web", "Teléfono", "Chat"]

prioridades = ["Crítica", "Alta", "Media", "Baja"]

estados = ["Abierto", "En progreso", "Resuelto", "Cerrado", "Cancelado"]

ciudades = ["Lima", "Huancayo", "Arequipa", "Trujillo", "Cusco"]

tipos_cliente = ["Interno", "Externo"]

equipos = [
    "Mesa de ayuda",
    "Infraestructura",
    "Aplicaciones",
    "Seguridad",
    "Soporte ERP",
]

agentes_por_equipo = {
    "Mesa de ayuda": ["Ana Torres", "Luis Ramos", "María Paredes"],
    "Infraestructura": ["Carlos Medina", "Jorge Salazar", "Elena Chávez"],
    "Aplicaciones": ["Patricia León", "Diego Vargas", "Lucía Herrera"],
    "Seguridad": ["Ricardo Flores", "Valeria Rojas"],
    "Soporte ERP": ["Fernando Díaz", "Camila Núñez"],
}

categorias = {
    "Hardware": ["Equipo lento", "Falla de impresora", "Cambio de periférico"],
    "Software": ["Error de aplicación", "Instalación de programa", "Actualización fallida"],
    "Redes": ["Sin conexión", "VPN", "Lentitud de red"],
    "Accesos": ["Restablecimiento de contraseña", "Permisos de usuario", "Cuenta bloqueada"],
    "Correo": ["No recibe correos", "Error de envío", "Configuración de Outlook"],
    "ERP": ["Error en módulo", "Consulta de proceso", "Problema de permisos"],
    "CRM": ["Error de registro", "Problema de sincronización", "Consulta de cliente"],
}

clientes_empresa = [
    "Comercial Andina",
    "Retail Norte",
    "Grupo Pacífico",
    "Servicios Lima",
    "Logística Central",
    "Inversiones Sur",
    "Corporación Sierra",
    "Distribuidora Horizonte",
]


# =========================
# FUNCIONES AUXILIARES
# =========================

def generar_fecha_aleatoria(fecha_inicio, fecha_fin):
    dias_rango = (fecha_fin - fecha_inicio).days
    dias_aleatorios = random.randint(0, dias_rango)
    return fecha_inicio + timedelta(days=dias_aleatorios)


def obtener_sla_horas(prioridad):
    if prioridad == "Crítica":
        return 4
    if prioridad == "Alta":
        return 8
    if prioridad == "Media":
        return 24
    return 48


def generar_tiempo_resolucion(prioridad, estado):
    if estado in ["Abierto", "En progreso", "Cancelado"]:
        return None

    if prioridad == "Crítica":
        return random.randint(1, 12)
    if prioridad == "Alta":
        return random.randint(2, 24)
    if prioridad == "Media":
        return random.randint(4, 72)
    return random.randint(8, 120)


def calcular_fecha_cierre(fecha_creacion, tiempo_resolucion_horas, estado):
    if estado in ["Abierto", "En progreso"]:
        return None

    if estado == "Cancelado":
        return fecha_creacion + timedelta(hours=random.randint(1, 24))

    return fecha_creacion + timedelta(hours=tiempo_resolucion_horas)


def calcular_satisfaccion(estado, cumple_sla):
    if estado not in ["Resuelto", "Cerrado"]:
        return None

    if cumple_sla == "Sí":
        return random.randint(4, 5)

    return random.randint(1, 3)


# =========================
# GENERACIÓN DEL DATASET
# =========================

tickets = []

for i in range(1, TOTAL_TICKETS + 1):
    ticket_id = f"TCK-{i:05d}"

    fecha_creacion = generar_fecha_aleatoria(FECHA_INICIO, FECHA_FIN)

    canal = random.choices(
        canales,
        weights=[35, 30, 20, 15],
        k=1
    )[0]

    prioridad = random.choices(
        prioridades,
        weights=[8, 22, 45, 25],
        k=1
    )[0]

    estado = random.choices(
        estados,
        weights=[12, 15, 45, 23, 5],
        k=1
    )[0]

    categoria = random.choice(list(categorias.keys()))
    subcategoria = random.choice(categorias[categoria])

    equipo_asignado = random.choice(equipos)
    agente = random.choice(agentes_por_equipo[equipo_asignado])

    cliente_empresa = random.choice(clientes_empresa)
    ciudad = random.choice(ciudades)
    tipo_cliente = random.choice(tipos_cliente)

    sla_horas = obtener_sla_horas(prioridad)

    tiempo_resolucion_horas = generar_tiempo_resolucion(prioridad, estado)

    fecha_cierre = calcular_fecha_cierre(
        fecha_creacion,
        tiempo_resolucion_horas,
        estado
    )

    if tiempo_resolucion_horas is None:
        cumple_sla = "No aplica"
    elif tiempo_resolucion_horas <= sla_horas:
        cumple_sla = "Sí"
    else:
        cumple_sla = "No"

    if fecha_cierre is None:
        dias_abierto = (FECHA_FIN - fecha_creacion).days
    else:
        dias_abierto = (fecha_cierre - fecha_creacion).days

    satisfaccion_cliente = calcular_satisfaccion(estado, cumple_sla)

    tickets.append({
        "ticket_id": ticket_id,
        "fecha_creacion": fecha_creacion.date(),
        "fecha_cierre": fecha_cierre.date() if fecha_cierre else None,
        "canal": canal,
        "prioridad": prioridad,
        "categoria": categoria,
        "subcategoria": subcategoria,
        "estado": estado,
        "equipo_asignado": equipo_asignado,
        "agente": agente,
        "cliente_empresa": cliente_empresa,
        "ciudad": ciudad,
        "tipo_cliente": tipo_cliente,
        "sla_horas": sla_horas,
        "tiempo_resolucion_horas": tiempo_resolucion_horas,
        "cumple_sla": cumple_sla,
        "dias_abierto": dias_abierto,
        "satisfaccion_cliente": satisfaccion_cliente,
    })


df = pd.DataFrame(tickets)


# =========================
# GUARDADO DE ARCHIVOS
# =========================

os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

df.to_csv(RUTA_RAW, index=False, encoding="utf-8-sig", sep=";")
df.to_csv(RUTA_PROCESSED, index=False, encoding="utf-8-sig", sep=";")


print("Dataset generado correctamente.")
print(f"Registros generados: {len(df)}")
print(f"Archivo raw: {RUTA_RAW}")
print(f"Archivo processed: {RUTA_PROCESSED}")