# nextcloud-plugin-fuzzer
# @c411e 
# Enumerates Nextcloud and ownCloud Plugins/Apps by enumerating typical javascript and image files
# A list of plugins will be downloaded from official sources


import requests
import argparse
from alive_progress import alive_bar;
from bs4 import BeautifulSoup
import json

requests.packages.urllib3.disable_warnings() 
download_url_nextcloud_marketplace = "https://apps.nextcloud.com/"
download_url_owncloud_marketplace = "https://marketplace.owncloud.com/ajax/products"
download_url_nextcloud_repository = "https://github.com/orgs/nextcloud/repositories?page="
download_url_owncloud_repository = "https://github.com/orgs/owncloud/repositories?page="
status = "status.php"

# List of plugins
plugins = set()

# List of common accessible files
files = {"/js/admin.js","/js/script.js","/js/files.js","/img/app.svg","/img/change.svg","/js/bruteforcesettings-main.js","/img/circles.svg","/img/favicon.svg","/img/social-facebook.svg","/img/notifications.svg","/img/social.svg","/img/screenshot.png","/img/empty.svg","/img/widget.svg","/img/page.svg","/img/app-dark.svg","/js/settings.js"}


# args parsing
parser = argparse.ArgumentParser(description='nextcloud-plugin-fuzzer')
parser.add_argument('-u','--url', help='Target URL e.g. https://nexcloud.com/', required=True)
parser.add_argument('-o','--owncloud', help='Target ownCloud instead of NextCloud', default=False, action='store_true')
args = parser.parse_args()

cloud_url = args.url
target_name = "ownCloud" if args.owncloud else "Nextcloud"


# Downloads a current list of plugins from the nextcloud website
def download_plugin_lists(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')

    if args.owncloud:
        response_json = r.json()
        plugin_urls = [item["url"] for item in response_json if "url" in item]
        plugins.update(plugin_urls)
    else:
        for a in soup.find_all('a', href=True):
            if "/apps/" in a['href']:
                plugins.add(a['href'][6:])


# Downloads a current list of plugins from the official repository
def download_plugin_lists_from_repository(url):
    for i in range (1,12):
        r = requests.get(url+str(i))
        print("--- Download Plugins from %s%s ---" %(url,str(i)))
        soup = BeautifulSoup(r.content, 'html5lib')
        for a in soup.find_all('a', href=True):
            target_subdirectory = "owncloud" if args.owncloud else "nextcloud"
            if a['href'].startswith(f"/{target_subdirectory}/"):
                plugins.add(a['href'].split("/")[2])


# Enumerate Plugins
def enumerate_plugins():
    with alive_bar(len(plugins) * len(files)) as bar:
        for plugin in plugins:
            for file in files:
                url = cloud_url + 'apps/' + plugin + file
                r = requests.get(url,verify=False,allow_redirects=False)
                bar()
                if r.status_code == 200:
                    print("Found Plugin %s: %s" %(plugin,url))



# Request status.php and get target version
def find_cloud(url):
    status_url = url + status
    r = requests.get(status_url,verify=False,allow_redirects=False)
    lower_content = str(r.content).lower()
    if r.status_code == 200 and ("nextcloud" in lower_content or "owncloud" in lower_content):
        resp = json.loads(r.content)
        print(f"--- Identified {target_name} ---")
        print("Version: %s" %resp["version"] )
    else:
        print(f"--- Can not find {target_name}. Are you sure to continue? [y/n]")
        anwser = input()
        if anwser == 'n':
            exit(0)
        elif anwser != 'y':
            print("--- Wrong input... ---")
            exit(0)



marketplace_url = download_url_owncloud_marketplace if args.owncloud else download_url_nextcloud_marketplace
repository_url = download_url_owncloud_repository if args.owncloud else download_url_nextcloud_repository

print(f"--- Download {target_name} Plugins from %s ---" %marketplace_url)
download_plugin_lists(marketplace_url)

download_plugin_lists_from_repository(repository_url)

length_plugins = len(plugins)
print("--- Found a total of %i Plugins ---" %length_plugins)

find_cloud(cloud_url)

print(f"--- Enumerate {target_name} Plugins from %s ---" %cloud_url)
enumerate_plugins()

