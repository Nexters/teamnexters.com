#!/bin/usr/python3.9
import json
from typing import Dict, Any

def make_image_scss(path: str, data: Dict[str, Any]) -> None:
    with open(path, mode="w", encoding="utf-8") as f:
        for row in data[1:]:
            name, value = row
            if value:
                f.write(f'${name}: url("https://drive.google.com/uc?export=view&id={value}");\n')

def make_recruitment(data: Dict[str, Any]) -> None:
    recruitment, r_banner_buttons, r_qualification, r_schedule, r_caution, r_notice, r_background = data["results"]

    bg, th, recruitment_start, recruitment_end, is_visible_notice, notice_title, type = recruitment["result"]["rawData"][1]

    # recruitment
    recruitment = {
        "bg": bg,
        "th": th,
        "recruitment_start": recruitment_start,
        "recruitment_end": recruitment_end,
        "is_visible_notice": is_visible_notice == "TRUE",
        "notice_title": notice_title,
        "type": type,
    }

    # banner box
    banner_boxes = []
    for idx, boxes in enumerate(r_banner_buttons["result"]["rawData"][1:]):
        name, link, is_visible, type = boxes
        _box = {
            "id": idx,
            "name": name,
            "link": link,
            "type": type,
            "is_visible_box": is_visible == "TRUE"
        }
        banner_boxes.append(_box)

    # qualification
    qualifications = []
    for idx, qualification in enumerate(r_qualification["result"]["rawData"][1:]):
        qa, is_visible = qualification
        _qualification = {
            "id": idx,
            "qualification": qa,
            "is_visible_qualification": is_visible == "TRUE"
        }
        qualifications.append(_qualification)

    # schedules
    schedules = []
    for idx, schedule in enumerate(r_schedule["result"]["rawData"][1:]):
        title, date = schedule
        _schedule = {
            "id": idx,
            "schedule": title,
            "date": date
        }
        schedules.append(_schedule)

    # cautions
    cautions = []
    for idx, caution in enumerate(r_caution["result"]["rawData"][1:]):
        content, is_visible = caution
        _caution = {
            "id": idx,
            "caution": content,
            "is_visible_caution": is_visible == "TRUE"
        }
        cautions.append(_caution)

    # notice
    notices = []
    for idx, notice in enumerate(r_notice["result"]["rawData"][1:]):
        content, is_visible = notice
        _notice = {
            "id": idx,
            "notice": content,
            "is_visible_notice": is_visible == "TRUE"
        }
        notices.append(_notice)

    make_image_scss("./assets/css/recruitment-bg.scss", r_background["result"]["rawData"])

    recruitment["boxes"] = banner_boxes
    recruitment["qualifications"] = qualifications
    recruitment["schedules"] = schedules
    recruitment["cautions"] = cautions
    recruitment["notices"] = notices

    with open(f"./content/recruitment/recruitment.json", mode="w", encoding="utf-8") as f:
        f.write(json.dumps(recruitment, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    with open("./_content/recruitment.json", mode="r") as f:
        google_results = f.read()
    data = json.loads(google_results)
    make_recruitment(data)
