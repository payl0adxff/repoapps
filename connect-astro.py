import requests

if __name__ == "__main__":
    timeout = 10
    url = "https://astrobox.hotmart.com/"
    header_data = {'Content-Type': 'application/x-www-form-urlencoded'}
    header_data = {}
    payload = "username=trisla.kessi@hotmart.com"
    r = requests.request("POST", url, data=payload, headers=header_data, timeout=timeout)
    print (r.request.body)
