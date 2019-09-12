import requests, smtplib, time

def requestSite(URL):
    requestURL = requests.get(URL)

    while requestURL.status_code != 200:
        print(f"{URL} status: {requestURL.status_code} Trying again.")
        time.sleep(5)
        requestURL = requests.get(URL)

    print(f"{URL} status: {requestURL.status_code}")
    return requestURL