import requests
import pickle
import json
from jsondiff import diff
from os.path import exists
from sendEmail import gmail_send_message


def get_request(url):
    r = requests.get(url)
    for line in r.text.split("\n"):
        if "data-json" in line:
            return json.loads(line.split("'")[1])


def save_request(request, fileName):
    with open(fileName, 'w') as f:
        json.dump(request, f)


def get_old_request(fileName):
    with open(fileName, 'r') as f:
        return json.load(f)


def request_equals(request1, request2):
    return diff(request1, request2)=={}


def get_sites():
    sites = []
    with open("instance/website_urls", "r") as f:
        for line in f:
            sites.append(line)
    return sites


def run():
    sites = get_sites()
    noChange = []
    changes = []
    request = {}
    for siteNum in range(len(sites)):
        site = sites[siteNum]
        new_request = get_request(site)
        courseName = new_request["displayName"]
        oldSiteFileName = f"instance/websites/{courseName}.json"

        if exists(oldSiteFileName):
            old_request = get_old_request(oldSiteFileName)

            if not request_equals(new_request, old_request):
                changes.append(site)
                gmail_send_message(f"Change in {courseName}", f"Website: {courseName}\n{diff(old_request, new_request)}")
            else:
                noChange.append(site)
                gmail_send_message(f"No change in {courseName}", f"Website: {courseName}")


        save_request(new_request, fileName=oldSiteFileName)

    print(f"Sites: {sites}")
    print(f"Changed sites: {changes}")
    print(f"Unchanged sites: {noChange}")



if __name__ == '__main__':
    run()
        

    