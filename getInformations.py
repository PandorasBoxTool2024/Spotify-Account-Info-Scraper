import requests

def getInformations(sp_dc, sp_key):
    url = "https://www.spotify.com/de/api/account/v1/datalayer/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Referer": "https://www.spotify.com/de/account/profile/?flow_ctx=8867bcfc-7843-447e-81b6-03f464f1f1a2%3A1717810238",
        "Cookie": f"sp_m=de; sp_t=afffe70e-a421-4f8b-9e62-123267ff609c; sp_new=1; sp_landing=https%3A%2F%2Fwww.spotify.com%2Fde%2Faccount%2Fprofile%2F; sp_dc={sp_dc}; sp_key{sp_key}; __Host-sp_csrf_sid=17a16efe700250daf3e2ad12daf27eebaaa2eb5d15596149dac1a0ff1b7b0a3b; sp_gaid=0088fc889850a9f68f197b9e0029fa4492839a521de5d95ba59819"
    }

    response = requests.get(url, headers=headers)

    print(response.text)
