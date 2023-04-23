import json
from typing import List

GoogleSheetResult = List[List[str]]


def make_image_scss(path: str, data: GoogleSheetResult) -> None:
    with open(path, mode="w", encoding="utf-8") as f:
        for row in data[1:]:
            name, value = row
            if value:
                f.write(
                    f'${name}: url("https://drive.google.com/uc?export=view&id={value}");\n'
                )


def make_main(data: GoogleSheetResult, background: GoogleSheetResult) -> None:
    work_dir = "./content"
    slogan, default_desc, default_a, default_href, th, recruitment_notice, recruitment_start, recruitment_end, recruitment_notice_desc, recruitment_notice_a, recruitment_in_progress_desc, recruitment_in_progress_a, recruitment_href = data[
        1
    ]
    main = {
        "slogan": slogan,
        "default_desc": default_desc,
        "default_a": default_a,
        "default_href": default_href,
        "th": th,
        "recruitment_notice": recruitment_notice,
        "recruitment_start": recruitment_start,
        "recruitment_end": recruitment_end,
        "recruitment_notice_desc": recruitment_notice_desc,
        "recruitment_notice_a": recruitment_notice_a,
        "recruitment_in_progress_desc": recruitment_in_progress_desc,
        "recruitment_in_progress_a": recruitment_in_progress_a,
        "recruitment_href": recruitment_href,
    }
    with open(f"{work_dir}/main.json", mode="w", encoding="utf-8") as f:
        f.write(json.dumps(main, ensure_ascii=False, indent=2))

    make_image_scss(f"{work_dir}/main-bg.scss", background)


def make_about(
    data: GoogleSheetResult,
    top_image: GoogleSheetResult,
    informations: GoogleSheetResult,
    reviews: GoogleSheetResult,
) -> None:
    work_dir = "./content/about"
    slogan, info_title, info_desc, activity_title, activity_desc, review_title, review_desc = data[
        1
    ]
    about = {
        "slogan": slogan,
        "info_title": info_title,
        "info_desc": info_desc,
        "activity_title": activity_title,
        "activity_desc": activity_desc,
        "review_title": review_title,
        "review_desc": review_desc,
    }
    with open(f"{work_dir}/text.json", mode="w", encoding="utf-8") as f:
        f.write(json.dumps(about, ensure_ascii=False, indent=2))

    for idx, review in enumerate(reviews[1:]):
        author, th, title, href = review
        _review = {
            "id": idx,
            "author": author,
            "th": th,
            "title": title,
            "href": href,
        }
        with open(
            f"{work_dir}/reviews/{idx}.json", mode="w", encoding="utf-8"
        ) as f:
            f.write(json.dumps(_review, ensure_ascii=False, indent=2))
    for idx, information in enumerate(informations[1:]):
        title, value, description = information
        _information = {
            "title": title,
            "value": value,
            "description": description,
        }
        with open(
            f"{work_dir}/informations/{idx}.json", mode="w", encoding="utf-8"
        ) as f:
            f.write(json.dumps(_information, ensure_ascii=False, indent=2))
    make_image_scss("./assets/css/about-top-image.scss", top_image)


def make_project(data: GoogleSheetResult) -> None:
    projects = []
    # 첫 행은 header이므로 제외
    for idx, row in enumerate(data[1:]):
        _, app_name, _thumbnail, th, year, team_name, _members, description, ppt, android_link, ios_link, web_link = (
            row
        )
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
            "link": {},
        }
        if android_link:
            project["link"]["Google Play"] = android_link
        if ios_link:
            project["link"]["App Store"] = ios_link
        if web_link:
            project["link"]["Go to Page"] = web_link
        projects.append(project)

    for idx, project in enumerate(projects):
        with open(
            f"./content/projects/{idx}.json", mode="w", encoding="utf-8"
        ) as f:
            f.write(json.dumps(project, ensure_ascii=False, indent=2))


def make_footer(data: GoogleSheetResult, sponsor: GoogleSheetResult) -> None:
    sns_items = []
    for idx, row in enumerate(data[1:]):
        name, href, _black, _white, _visible = row
        black = f"https://drive.google.com/uc?export=view&id={_black}"
        white = f"https://drive.google.com/uc?export=view&id={_white}"
        visible = bool(_visible)
        sns_items.append(
            {
                "idx": idx,
                "name": name,
                "href": href,
                "black": black,
                "white": white,
                "visible": _visible == "TRUE",
            }
        )

    for idx, sns in enumerate(sns_items):
        with open(
            f"./content/footers/sns/{idx}.json", mode="w", encoding="utf-8"
        ) as f:
            f.write(json.dumps(sns, ensure_ascii=False, indent=2))

    sponsors = []
    for idx, row in enumerate(sponsor[1:]):
        name, href, isVisible = row
        sponsors.append(
            {
                "idx": idx,
                "name": name,
                "href": href,
                "isVisible": isVisible == "TRUE",
            }
        )

    for idx, sponsor in enumerate(sponsors):
        with open(
            f"./content/footers/sponsor/{idx}.json", mode="w", encoding="utf-8"
        ) as f:
            f.write(json.dumps(sponsor, ensure_ascii=False, indent=2))


def make_recruitment(
    recruitment: GoogleSheetResult,
    r_banner_buttons: GoogleSheetResult,
    r_qualification: GoogleSheetResult,
    r_schedule: GoogleSheetResult,
    r_caution: GoogleSheetResult,
    r_notice: GoogleSheetResult,
    r_background: GoogleSheetResult,
) -> None:

    bg, th, recruitment_start, recruitment_end, is_visible_notice, notice_title = recruitment[
        1
    ]

    # recruitment
    _recruitment = {
        "bg": bg,
        "th": th,
        "recruitment_start": recruitment_start,
        "recruitment_end": recruitment_end,
        "is_visible_notice": is_visible_notice == "TRUE",
        "notice_title": notice_title,
    }

    # banner box
    banner_boxes = []
    for idx, boxes in enumerate(r_banner_buttons[1:]):
        name, link, is_visible, type = boxes
        _box = {
            "id": idx,
            "name": name,
            "link": link,
            "type": type,
            "is_visible_box": is_visible == "TRUE",
        }
        banner_boxes.append(_box)

    # qualification
    qualifications = []
    for idx, qualification in enumerate(r_qualification[1:]):
        qa, is_visible = qualification
        _qualification = {
            "id": idx,
            "qualification": qa,
            "is_visible_qualification": is_visible == "TRUE",
        }
        qualifications.append(_qualification)

    # schedules
    schedules = []
    for idx, schedule in enumerate(r_schedule[1:]):
        title, date = schedule
        _schedule = {"id": idx, "schedule": title, "date": date}
        schedules.append(_schedule)

    # cautions
    cautions = []
    for idx, caution in enumerate(r_caution[1:]):
        content, is_visible = caution
        _caution = {
            "id": idx,
            "caution": content,
            "is_visible_caution": is_visible == "TRUE",
        }
        cautions.append(_caution)

    # notice
    notices = []
    for idx, notice in enumerate(r_notice[1:]):
        content, is_visible = notice
        _notice = {
            "id": idx,
            "notice": content,
            "is_visible_notice": is_visible == "TRUE",
        }
        notices.append(_notice)

    make_image_scss("./assets/css/recruitment-bg.scss", r_background)

    _recruitment["boxes"] = banner_boxes
    _recruitment["qualifications"] = qualifications
    _recruitment["schedules"] = schedules
    _recruitment["cautions"] = cautions
    _recruitment["notices"] = notices

    with open(
        f"./content/recruitment/recruitment.json", mode="w", encoding="utf-8"
    ) as f:
        f.write(json.dumps(_recruitment, ensure_ascii=False, indent=2))


def make_color(data: GoogleSheetResult) -> None:
    with open("./assets/css/setting.scss", mode="w") as f:
        for row in data[1:]:
            name, _, value = row
            if value:
                f.write(f"${name}: {value};\n")


def make_contacts(contact_us: GoogleSheetResult, faq: GoogleSheetResult) -> None:
    _contacts = []

    for idx, c in enumerate(contact_us[1:]):
        title, text, contact_type, is_visible = c
        _contact = {
            "id": idx,
            "title": title,
            "text": text,
            "type": contact_type,
            "isVisible": is_visible == "TRUE"
        }
        _contacts.append(_contact)

    _faqs = []
    for idx, f in enumerate(faq[1:]):
        question, answer = f
        _faq = {
            "id": idx,
            "question": question,
            "answer": answer
        }
        _faqs.append(_faq)

    for idx, _contact in enumerate(_contacts):
        with open(f"./content/contacts/{idx}.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(_contact, ensure_ascii=False, indent=2))

    for idx, _faq in enumerate(_faqs):
        with open(f"./content/contacts/faq/{idx}.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(_faq, ensure_ascii=False, indent=2))


