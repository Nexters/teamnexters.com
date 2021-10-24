#!/bin/usr/python3.9
import json

if __name__ == "__main__":
    with open("./_content/about.json", mode="r") as f:
        google_results = f.read()

    _about = json.loads(google_results)
    rows = _about["results"][0]["result"]["rawData"]

    slogan, info_title, info_desc, activity_title, activity_desc, review_title, review_desc = rows[1]
    about = {
        "slogan":slogan,
        "info_title": info_title,
        "info_desc": info_desc,
        "activity_title": activity_title,
        "activity_desc": activity_desc,
        "review_title": review_title,
        "review_desc": review_desc
    }

    with open(f"./content/about/text.json", mode="w", encoding="utf-8") as f:
        f.write(json.dumps(about, ensure_ascii=False, indent=2))
