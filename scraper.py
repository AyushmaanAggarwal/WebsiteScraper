import requests
import pickle
from os.path import exists
from sendEmail import gmail_send_message

def get_request(url):
    return requests.get(url)

def save_request(request, fileName="instance/last_request"):
    with open(fileName, 'wb') as f:
        pickle.dump({0:request.text}, f)

def compare_request(request, fileName="instance/last_request"):
    with open(fileName, 'rb') as f:
        oldRequest = pickle.load(f)[0]
    return request.text == oldRequest

def get_sites():
    sites = []
    with open("instance/website_urls", "r") as f:
        for line in f:
            sites.append(line)
    return sites

if __name__ == '__main__':
    sites = get_sites()
    noChange = []
    changes = []
    request = {}
    for siteNum in range(len(sites)):
        site = sites[siteNum]
        request[site] = get_request(site)
        if exists(f"instance/{siteNum}"):
            if not compare_request(request[site], fileName=f"instance/{siteNum}"):
                changes.append(site)
                gmail_send_message("Change in sites", site)
            else:
                noChange.append(site)
        save_request(request[site], fileName=f"instance/{siteNum}")
    print(f"Sites: {sites}")
    print(f"Changed sites: {changes}")
    print(f"Unchanged sites: {noChange}")
        
        
    