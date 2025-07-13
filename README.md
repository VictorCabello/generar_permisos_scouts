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

- `--scouts`: Ruta al archivo Excel con información de scouts este archivo debe ser producido desde el reporteador de [sisas](https://sisas.scouts.org.mx/) (por defecto: scouts.xlsx).
- `--activities`: Ruta al archivo Excel con información de actividades, el archivo debe tener las mismas culumnas y tipo de celdas que el archivo [en assets](./assets/activities.xlsx) (por defecto: activities.xlsx)
- `--template`: Ruta al archivo de plantilla PDF, y debe ser una copia del [archivo en assets](.assets/template.pdf) (por defecto: template.pdf)

Los PDFs generados se guardan en el directorio `output`.

## Instalacion

Para instalar corre el siguiente comando:

```bash
pip install git+https://github.com/VictorCabello/generar_permisos_scouts.git
```
