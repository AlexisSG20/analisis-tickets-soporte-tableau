import pandas as pd


RUTA_DATASET = "data/processed/tickets_soporte.csv"

df = pd.read_csv(RUTA_DATASET, sep=";")


print("REVISIÓN GENERAL DEL DATASET")
print("=" * 40)

print("\nPrimeras filas:")
print(df.head())

print("\nCantidad de filas y columnas:")
print(df.shape)

print("\nColumnas:")
print(df.columns.tolist())

print("\nValores nulos por columna:")
print(df.isnull().sum())

print("\nTickets por estado:")
print(df["estado"].value_counts())

print("\nTickets por prioridad:")
print(df["prioridad"].value_counts())

print("\nCumplimiento SLA:")
print(df["cumple_sla"].value_counts())

print("\nTickets por canal:")
print(df["canal"].value_counts())

print("\nTickets por categoría:")
print(df["categoria"].value_counts())

print("\nResumen de tiempo de resolución:")
print(df["tiempo_resolucion_horas"].describe())

print("\nResumen de satisfacción:")
print(df["satisfaccion_cliente"].describe())