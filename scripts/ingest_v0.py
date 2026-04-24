import csv
from datetime import datetime
from pathlib import Path

import requests
import yaml


CONFIG_PATH = Path("config/sources.yaml")
RAW_DIR = Path("data/raw")
METADATA_DIR = Path("data/metadata")
LOG_DIR = Path("outputs/logs")

METADATA_FILE = METADATA_DIR / "sources.csv"
LOG_FILE = LOG_DIR / "ingest_v0.log"


def ensure_dirs():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    METADATA_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)


def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(line + "\n")


def load_sources():
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    return config.get("sources", [])


def download_file(url, output_path):
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    with open(output_path, "wb") as file:
        file.write(response.content)


def write_metadata(source, output_path, status):
    file_exists = METADATA_FILE.exists()

    fields = [
        "id_documento",
        "titulo",
        "institucion",
        "tipo_documento",
        "tema",
        "url_origen",
        "nombre_archivo",
        "estado_descarga",
        "fecha_ingesta"
    ]

    with open(METADATA_FILE, "a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "id_documento": source.get("id"),
            "titulo": source.get("title"),
            "institucion": source.get("institution"),
            "tipo_documento": source.get("type"),
            "tema": source.get("topic"),
            "url_origen": source.get("url"),
            "nombre_archivo": output_path.name,
            "estado_descarga": status,
            "fecha_ingesta": datetime.now().strftime("%Y-%m-%d")
        })


def main():
    ensure_dirs()
    sources = load_sources()

    log("Inicio de ingesta versión 0")

    for source in sources:
        url = source.get("url")
        output_file = source.get("output_file")
        output_path = RAW_DIR / output_file

        if not url or "COLOCAR_URL_OFICIAL" in url:
            log(f"URL pendiente para {source.get('id')} - {source.get('title')}")
            write_metadata(source, output_path, "url_pendiente")
            continue

        if output_path.exists():
            log(f"Archivo ya existe. Se omite descarga: {output_path}")
            write_metadata(source, output_path, "ya_existia")
            continue

        try:
            log(f"Descargando {source.get('id')} - {source.get('title')}")
            download_file(url, output_path)
            log(f"Descarga completada: {output_path}")
            write_metadata(source, output_path, "descargado")

        except Exception as error:
            log(f"Error al descargar {source.get('id')}: {error}")
            write_metadata(source, output_path, "error")

    log("Fin de ingesta versión 0")


if __name__ == "__main__":
    main()