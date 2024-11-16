import requests
import json

import requests


import requests
import json

def get_login_info(email, password):
    """
    :param email: Account Email (Not Username)
    :param password: Account Password
    :return:
    This function returns JSON user auth info, below is an example returned JSON
    {
    "uauth":
        {
            "uid":123456,"salt":"1a2b3c4d5e6f7g",
            "authsig":"0df4496478dn65n76c6d5b71246udfgbhzw4zn3c346vw"
        },
    "user":
        {
        "name":"AccountUsername",
        "email":"accountEmail@domain.com",
        "lang":1
        }
    }
    """

    url = "https://bdsmtest.org/ajax/login"

    # Headers required for the request
    headers = {
        "Host": "bdsmtest.org",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Accept-Language": "en-GB,en;q=0.9",
        "Sec-Ch-Ua": "\"Not?A_Brand\";v=\"99\", \"Chromium\";v=\"130\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://bdsmtest.org",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://bdsmtest.org/login",
        "Accept-Encoding": "gzip, deflate, br",
        "Priority": "u=1, i"
    }

    # Cookies required for the request
    cookies = {
        "_gid": "GA1.2.440141939.1731716440",
        "_ga_HB2GZNDNS2": "GS1.1.1731716439.1.0.1731716439.60.0.0",
        "_ga": "GA1.1.440471492.1731716440"
    }

    # Data to be sent in the request body
    data = {
        "email": email,
        "pass": password,
        "lang": "EN"
    }

    try:
        # Send the POST request
        response = requests.post(url, headers=headers, cookies=cookies, data=data, verify=False)

        # Debugging: Print status code and headers
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")

        # Check if the response was successful
        if response.status_code == 200:
            # Debugging: Print raw response text
            print(f"Raw Response Text: {response.text}")

            # Attempt to parse the JSON response
            try:
                return response.json()
            except json.JSONDecodeError:
                print("Error: Response is not valid JSON.")
                return None
        else:
            print(f"Failed to login: Status Code {response.status_code}")
            print(f"Response Text: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None



def pull_data(link):
    pass