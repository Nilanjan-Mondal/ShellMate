import json
import os
from datetime import datetime

LOG_FILE = "log.json"

def log_activity(entry: dict):
    allowed_keys = {"type", "instruction", "gen_comm", "meta"}
    filtered_entry = {k: v for k, v in entry.items() if k in allowed_keys}
    filtered_entry["timestamp"] = datetime.now().isoformat()

    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []

    logs.append(filtered_entry)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=4)
