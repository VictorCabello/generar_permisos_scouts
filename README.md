# Generar Permisos Scouts

Generar Permisos Scouts es una herramienta en Python para generar permisos de actividades scouts en PDF a partir de archivos Excel y una plantilla. Automatiza la creación de documentos de autorización personalizados para scouts que participan en diversas actividades.

## Características

- Lee datos de scouts y actividades desde archivos Excel
- Rellena una plantilla PDF con información personalizada
- Genera archivos PDF individuales para cada scout y actividad

## Uso

Ejecuta la herramienta desde la línea de comandos:

```bash
python -m generar_permisos_scouts.cli \
  --scouts ruta/a/scouts.xlsx \
  --activities ruta/a/activities.xlsx \
  --template ruta/a/template.pdf
```

- `--scouts`: Ruta al archivo Excel con información de scouts (por defecto: scouts.xlsx)
- `--activities`: Ruta al archivo Excel con información de actividades (por defecto: activities.xlsx)
- `--template`: Ruta al archivo de plantilla PDF (por defecto: template.pdf)

Los PDFs generados se guardan en el directorio `output`.

## Requisitos

- Python 3.10+
- pypdf
- reportlab
- tqdm

Instala las dependencias:

```bash
pip install pypdf reportlab tqdm
```
