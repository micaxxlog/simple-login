import json
import os

daemon_config = {
    "dns": ["8.8.8.8", "8.8.4.4"]
}

daemon_json_path = "/etc/docker/daemon.json"

with open(daemon_json_path, "w") as f:
    json.dump(daemon_config, f)

print(f"Configuración de daemon.json creada en {daemon_json_path}")
