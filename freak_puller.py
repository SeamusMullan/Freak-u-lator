import requests
import time

def pull_data(link):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Referer": link,
        "X-Requested-With": "XMLHttpRequest",
    }

    data = {
        "Content-Length": "149",
        "Host": "www.bdsmtest.org",
        "Origin": "https://www.bdsmtest.org",
        "Sec-Ch-Ua": "",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }

    sess=requests.Session()
    sess.get(link, headers=headers)
    res=sess.post("https://bdsmtest.org/ajax/getresult", data=data, headers=headers)

    print(f"Status Code: {res.status_code}")
    print(f"Response Body: {res.text}")  # If the response is in JSON format
    try:
        print(res.json())
    except:
        print("brokey :(")

pull_data("https://www.bdsmtest.org/r/5RaEQF6w")