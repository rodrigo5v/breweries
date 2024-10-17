import json, requests, os
from requests import HTTPError, Timeout
from datetime import datetime

ingestion_date = datetime.now().date()
filename = "breweries.json"
storage_path = f"/home/rods/storage/bronze/inserted_at={ingestion_date}/"

try:
    response = requests.get("https://api.openbrewerydb.org/breweries")
    data = response.json()

    os.makedirs(storage_path, exist_ok=True)
    lake = os.path.join(storage_path, filename)

    with open(lake, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
except HTTPError as http:
    print(f"HTTPError: {http}")
except Timeout:
    print("Tempo limite excedido")
except Exception as err:
    print(f"Ocorreu o seguinte erro: {err}")