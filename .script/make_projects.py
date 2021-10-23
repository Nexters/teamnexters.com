#!/bin/usr/python3.9
import json

with open("./content/project.json", mode="r") as f:
    google_results = f.read()

_projects = json.loads(google_results)
rows = _projects["results"][0]["result"]["rawData"]

projects = []
# 첫 행은 header이므로 제외
for idx, row in enumerate(rows[1:]):
    app_name, _thumbnail, th, year, team_name, _members, description, ppt, android_link, ios_link, web_link = row
    thumbnail = (
        _thumbnail 
        if f"https://drive.google.com/uc?export=view&id={_thumbnail}" 
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

# # content/_projects 폴더를 생성하고, 폴더 안에 파일 쓰기

# with open("./content/_projects/")
