# Análisis Operativo de Tickets de Soporte con Tableau

Proyecto de análisis de datos orientado a monitorear el desempeño operativo de un área de soporte tecnológico mediante un dashboard interactivo en Tableau.

## Empresa ficticia

**AndinaTech Services S.A.C.**

Empresa ficticia dedicada a brindar soporte tecnológico a clientes internos y externos.

## Caso de negocio

AndinaTech Services S.A.C. recibe tickets de soporte por distintos canales, categorías, prioridades y equipos de atención.  
Debido al crecimiento del volumen de tickets, la gerencia necesita una solución visual que permita monitorear el estado de la operación, medir el cumplimiento de SLA, identificar backlog y analizar los tiempos de resolución.

## Objetivo del proyecto

Construir un dashboard en Tableau que permita analizar:

- Volumen total de tickets.
- Tickets abiertos, en progreso, resueltos y cerrados.
- Cumplimiento de SLA.
- Tickets vencidos.
- Backlog operativo.
- Tiempo promedio de resolución.
- Satisfacción promedio del cliente.
- Carga de tickets por equipo, categoría, prioridad y canal.
- Tendencia mensual de tickets.

## Dashboard

Vista principal del dashboard operativo desarrollado en Tableau:

![Dashboard operativo de soporte](docs/capturas/dashboard-operativo-soporte.png)

Dashboard interactivo publicado en Tableau Public:

[Ver dashboard en Tableau Public](https://public.tableau.com/views/AnlisisOperativodeTicketsdeSoporte/DashboardOperativoSoporte?:language=es-ES&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

Archivo principal del dashboard:

```text
tableau/analisis-tickets-soporte-tableau.twbx
```

## Principales hallazgos

- Se analizaron **2500 tickets de soporte** generados de forma sintética para simular una operación anual de mesa de ayuda.
- El backlog operativo fue de **700 tickets** entre abiertos y en progreso, lo que permite identificar una carga pendiente relevante para el equipo de soporte.
- El cumplimiento de SLA fue de **32.4%**, lo que evidencia una oportunidad de mejora en la atención dentro de los tiempos definidos.
- La mayoría de tickets se concentró en **prioridad media**, lo que sugiere que la operación recibe principalmente incidencias de impacto moderado.
- Los tickets **resueltos** representan el mayor volumen dentro del estado de atención, lo que indica que una parte importante de la demanda sí fue gestionada durante el periodo.
- El análisis por categoría y equipo permite identificar áreas con mayor carga operativa y priorizar acciones de seguimiento.

## Herramientas utilizadas

- Python
- Pandas
- Tableau
- CSV
- Git / GitHub

## Cómo reproducir el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/AlexisSG20/analisis-tickets-soporte-tableau.git
```

2. Entrar a la carpeta del proyecto:

```bash
cd analisis-tickets-soporte-tableau
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

4. Generar nuevamente el dataset sintético:

```bash
py scripts/generar_dataset_tickets.py
```

5. Revisar el dataset generado:

```bash
py scripts/revisar_dataset.py
```

6. Abrir en Tableau el archivo:

```text
tableau/analisis-tickets-soporte-tableau.twbx
```

## Documentación técnica

La documentación técnica del proyecto describe el caso de negocio, la generación del dataset, las métricas utilizadas, el diseño del dashboard, los principales hallazgos y las mejoras futuras.

[Ver documentación técnica en PDF](docs/documentacion_tecnica_tickets_soporte_tableau.pdf)

## Estructura del proyecto

```text
analisis-tickets-soporte-tableau/
│
├── data/
│   ├── raw/
│   │   └── tickets_soporte_raw.csv
│   └── processed/
│       └── tickets_soporte.csv
│
├── scripts/
│   ├── generar_dataset_tickets.py
│   └── revisar_dataset.py
│
├── tableau/
│   └── analisis-tickets-soporte-tableau.twbx
│
├── docs/
│   ├── capturas/
│   │   └── dashboard-operativo-soporte.png
│   └── documentacion_tecnica_tickets_soporte_tableau.pdf
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Dataset

El dataset fue generado de forma sintética con Python y contiene **2500 tickets de soporte** correspondientes al periodo **enero a diciembre de 2025**.

El archivo CSV utiliza codificación `utf-8-sig` y separador `;`, para facilitar su apertura en Excel con configuración regional en español.

Las columnas principales son:

- ticket_id
- fecha_creacion
- fecha_cierre
- canal
- prioridad
- categoria
- subcategoria
- estado
- equipo_asignado
- agente
- cliente_empresa
- ciudad
- tipo_cliente
- sla_horas
- tiempo_resolucion_horas
- cumple_sla
- dias_abierto
- satisfaccion_cliente

## Métricas principales

- Total de tickets.
- Tickets resueltos.
- Tickets abiertos.
- Backlog.
- Tickets vencidos.
- Porcentaje de cumplimiento de SLA.
- Tiempo promedio de resolución.
- Satisfacción promedio.
- Tickets por prioridad.
- Tickets por canal.
- Tickets por categoría.
- Tickets por equipo.

## Estado del proyecto

Finalizado.

## Autor

**Alexis Suasnabar**
