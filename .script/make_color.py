#!/bin/python3.9
import json

if __name__ == "__main__":
    with open("./_content/color.json", mode="r") as f:
        google_results = f.read()

    _color = json.loads(google_results)
    rows = _color["results"][0]["result"]["rawData"]
    with open("./assets/css/setting.scss", mode="w") as f:
        for row in rows[1:]:
            name, value = row
            f.write(f"${name}: {value};\n")
        
