#!/bin/usr/python3.9
import json

if __name__ == "__main__":
    with open("./_content/main.json", mode="r") as f:
        google_results = f.read()

    _main = json.loads(google_results)
    rows = _main["results"][0]["result"]["rawData"]

    slogan, default_desc, default_a, default_href, th, recruitment_start, recruitment_deadline, recruitment_notice_desc, recruitment_notice_a, recruitment_in_progress_desc, recruitment_in_progress_a, recruitment_href = rows[1]
    main = {
        "slogan": slogan,
        "default_desc": default_desc,
        "default_a": default_a,
        "default_href": default_href,
        "th": th,
        "recruitment_start": recruitment_start,
        "recruitment_deadline": recruitment_deadline,
        "recruitment_notice_desc": recruitment_notice_desc,
        "recruitment_notice_a": recruitment_notice_a,
        "recruitment_in_progress_desc": recruitment_in_progress_desc,
        "recruitment_in_progress_a": recruitment_in_progress_a,
        "recruitment_href": recruitment_href,
    }

    with open(f"./content/main.json", mode="w", encoding="utf-8") as f:
        f.write(json.dumps(main, ensure_ascii=False, indent=2))
