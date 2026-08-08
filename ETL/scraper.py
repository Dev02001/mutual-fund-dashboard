import requests


def fetch_funds_data():
    url = "https://apimf.icicipruamc.com/fs/v1/funds"
    payload = {
        "component": "NAV",
        "filters" : [
            {"filterColumn": "TYPE", "filterValue": ["ALL"]},
            {"filterColumn": "PLAN", "filterValue": ["DIRECT"]},
            {"filterColumn":"SCHEME_OPTION", "filterValue":["GROWTH"]},
        ],
        "fundName":"",
        "loadAllSchemes": False,
        "sorts":[
            {
                "sortColumn": "SCHEME_NAME",
                "sortOrder": "asc"
            }
        ]
    }
    headers = {
        "Content-Type": "application/json",
        "Origin" : "https://www.icicipruamc.com",
        "Referer": "https://www.icicipruamc.com/",
        "Env": "api"
    }
    response = requests.post(
        url,
        json=payload,
        headers=headers
    )
    # response.raise_for_status()
    #print(response.status_code)
    #print(response.text)
    data = response.json()

    return data


def get_fund_by_scheme_code(data, scheme_code):
    for category in data ["success"]["data"]:
        for scheme in category["schemes"]:
            if scheme["schemeCode"] == scheme_code:
                return scheme

    return None

def get_latest_nav(fund_details):
    latest_nav = fund_details["latestNav"]
    nav_date = fund_details["navDate"]
    return  latest_nav, nav_date