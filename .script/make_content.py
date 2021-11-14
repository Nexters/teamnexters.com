#!/bin/usr/python3.9
import json
from typing import Dict, Any

def make_image_scss(path: str, data: Dict[str, Any]) -> None:
    with open(path, mode="w", encoding="utf-8") as f:
        for row in data[1:]:
            name, value = row
            if value:
                f.write(f'${name}: url("https://drive.google.com/uc?export=view&id={value}");\n')

def make_main(data: Dict[str, Any], background: Dict[str, Any]) -> None:
    slogan, default_desc, default_a, default_href, th, recruitment_notice, recruitment_start, recruitment_deadline, recruitment_notice_desc, recruitment_notice_a, recruitment_in_progress_desc, recruitment_in_progress_a, recruitment_href = data[1]
    main = {
        "slogan": slogan,
        "default_desc": default_desc,
        "default_a": default_a,
        "default_href": default_href,
        "th": th,
        "recruitment_notice": recruitment_notice,
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

    make_image_scss("./assets/css/main-bg.scss", background)

def make_about(
    data: Dict[str, Any],
    top_image: Dict[str, Any],
    informations: Dict[str, Any],
    reviews: Dict[str, Any]
) -> None:
    slogan, info_title, info_desc, activity_title, activity_desc, review_title, review_desc = data[1]
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

    for idx, review in enumerate(reviews[1:]):
        author, th, title, href, _ = review
        _review = {
            "id": idx,
            "author": author,
            "th":th,
            "title":title,
            "href":href
        }
        with open(f"./content/about/reviews/{idx}.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(_review, ensure_ascii=False, indent=2))
    for idx, information in enumerate(informations[1:]):
        title, value, description = information
        _information = {
            "title": title,
            "value": value,
            "description": description,
        }
        with open(f"./content/about/informations/{idx}.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(_information, ensure_ascii=False, indent=2))
    make_image_scss("./assets/css/about-top-image.scss", top_image)

def make_project(data: Dict[str, Any]) -> None:
    projects = []
    # 첫 행은 header이므로 제외
    for idx, row in enumerate(data[1:]):
        _, app_name, _thumbnail, th, year, team_name, _members, description, ppt, android_link, ios_link, web_link = row
        thumbnail = (
            f"https://drive.google.com/uc?export=view&id={_thumbnail}"
            if _thumbnail 
            else ""
        )
        project = {
            "idx": idx,
            "app_name": app_name,
            "thumbnail": thumbnail,
            "th": th,
            "year": year,
            "team_name": team_name,
            "members": [member.strip() for member in _members.split(",")],
            "description": description,
            "ppt": ppt,
            "link":{}
        }
        if android_link:
            project["link"]["Google Play"] = android_link
        if ios_link:
            project["link"]["App Store"] = ios_link
        if web_link:
            project["link"]["Go to Page"] = web_link
        projects.append(project)

    for idx, project in enumerate(projects):
        with open(f"./content/projects/{idx}.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(project, ensure_ascii=False, indent=2))

def make_footer(data: Dict[str, Any]) -> None:
    sns_items = []
    for idx, row in enumerate(data[1:]):
        name, href, _black, _white = row
        black = f"https://drive.google.com/uc?export=view&id={_black}"
        white = f"https://drive.google.com/uc?export=view&id={_white}"
        sns_items.append({"idx":idx, "name": name, "href": href, "black": black, "white": white})

    for idx, sns in enumerate(sns_items):
        with open(f"./content/footers/sns/{idx}.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(sns, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    with open("./_content/data.json", mode="r") as f:
        google_results = f.read()
    data = json.loads(google_results)
    main, main_background, about, about_top_image, informations, reviews, footer = data["results"]
    make_main(main["result"]["rawData"], main_background["result"]["rawData"])
    make_about(
        about["result"]["rawData"],
        about_top_image["result"]["rawData"],
        informations["result"]["rawData"],
        reviews["result"]["rawData"]
    )
    
    with open("./_content/project.json", mode="r") as f:
        google_results = f.read()
    data = json.loads(google_results)
    projects = data["results"][0]["result"]["rawData"]
    make_project(projects)
    make_footer(footer)

