import os
from distutils.dir_util import copy_tree

import gspread
from tqdm import tqdm

from ._utils import (make_about, make_contacts, make_footer, make_main,
                     make_project, make_recruitment)

if __name__ == "__main__":
    copy_tree("./content_generator/content", "./content")
    info = {
        "type": "service_account",
        "project_id": os.environ.get("PROJECT_ID", ""),
        "private_key_id": os.environ.get("PRIVATE_KEY_ID", ""),
        "private_key": os.environ.get("PRIVATE_KEY", "").replace("\\n", "\n"),
        "client_email": os.environ.get("CLIENT_EMAIL", ""),
        "client_id": os.environ.get("CLIENT_ID", ""),
        "auth_uri": os.environ.get("AUTH_URI", "https://accounts.google.com/o/oauth2/auth"),
        "token_uri": os.environ.get("TOKEN_URI", "https://oauth2.googleapis.com/token"),
        "auth_provider_x509_cert_url": os.environ.get(
            "AUTH_PROVIDER_X509_CERT_URL", "https://www.googleapis.com/oauth2/v1/certs"
        ),
        "client_x509_cert_url": os.environ.get("CLIENT_X509_CERT_URL", "https://www.googleapis.com/robot/v1/metadata/x509/nexters-website%40nexters-website.iam.gserviceaccount.com"),
    }

    with tqdm(total=25) as pbar:
        client = gspread.service_account_from_dict(info=info)
        pbar.update(1)
        spread_sheet = client.open("Nexters web admin")
        pbar.update(1)

        _main = spread_sheet.worksheet("M-Auto").get_all_values()
        pbar.update(1)
        _main_background = spread_sheet.worksheet(
            "M-background"
        ).get_all_values()
        pbar.update(1)
        make_main(_main, _main_background)
        pbar.update(1)

        _about = spread_sheet.worksheet("About").get_all_values()
        pbar.update(1)
        _about_top_image = spread_sheet.worksheet("A-image").get_all_values()
        pbar.update(1)
        _about_informations = spread_sheet.worksheet(
            "A-information"
        ).get_all_values()
        pbar.update(1)
        _about_reviews = spread_sheet.worksheet("A-review").get_all_values()
        pbar.update(1)
        make_about(
            data=_about,
            top_image=_about_top_image,
            informations=_about_informations,
            reviews=_about_reviews,
        )
        pbar.update(1)
        _footer = spread_sheet.worksheet("Footer").get_all_values()
        pbar.update(1)
        _sponsor = spread_sheet.worksheet("Sponsor").get_all_values()
        pbar.update(1)
        make_footer(_footer, _sponsor)
        pbar.update(1)

        _projects = spread_sheet.worksheet("Project").get_all_values()
        pbar.update(1)
        make_project(_projects)
        pbar.update(1)

        _recruitment = spread_sheet.worksheet("Recruitment").get_all_values()
        pbar.update(1)
        _recruitment_button = spread_sheet.worksheet(
            "R-button"
        ).get_all_values()
        pbar.update(1)
        _recruitment_qualification = spread_sheet.worksheet(
            "R-qualification"
        ).get_all_values()
        pbar.update(1)
        _recruitment_schedule = spread_sheet.worksheet(
            "R-schedule"
        ).get_all_values()
        pbar.update(1)
        _recruitment_caution = spread_sheet.worksheet(
            "R-caution"
        ).get_all_values()
        pbar.update(1)
        _recruitment_notice = spread_sheet.worksheet(
            "R-notice"
        ).get_all_values()
        pbar.update(1)
        _recruitment_background = spread_sheet.worksheet(
            "R-background"
        ).get_all_values()
        pbar.update(1)
        make_recruitment(
            _recruitment,
            _recruitment_button,
            _recruitment_qualification,
            _recruitment_schedule,
            _recruitment_caution,
            _recruitment_notice,
            _recruitment_background,
        )
        pbar.update(1)

        _contact = spread_sheet.worksheet("Contact-Us").get_all_values()
        pbar.update(1)
        _faq = spread_sheet.worksheet("FAQ").get_all_values()
        pbar.update(1)
        make_contacts(_contact, _faq)
        pbar.update(1)
