import routes

import json
#from pathlib import Path

# --- loads config.json
config_file = open("./config.json")
config = json.load(config_file)
# ---

# --- runs the app
if __name__ == "__main__":
    routes.app.run(host = config["socket"]["ip"], port = config["socket"]["port"])
# ---