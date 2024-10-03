# nextcloud-plugin-fuzzer
# @c411e 
# Enumerates Nextcloud Plugins/Apps by enumerating typical javascript and image files
# A list of plugins will be downloaded from official sources


import requests
import argparse
from alive_progress import alive_bar;
from bs4 import BeautifulSoup
import json

requests.packages.urllib3.disable_warnings() 
download_url ="https://apps.nextcloud.com/"
download_url_repository = "https://github.com/orgs/nextcloud/repositories?page="
status = "status.php"

# List of plugins
plugins = set()

# List of common accessible files
files = {"/js/admin.js","/js/script.js","/js/files.js","/img/app.svg","/img/change.svg","/js/bruteforcesettings-main.js","/img/circles.svg","/img/favicon.svg","/img/social-facebook.svg","/img/notifications.svg","/img/social.svg","/img/screenshot.png","/img/empty.svg","/img/widget.svg","/img/page.svg","/img/app-dark.svg","/js/settings.js"}


# args parsing
parser = argparse.ArgumentParser(description='nextcloud-plugin-fuzzer')
parser.add_argument('-u','--url', help='Nextcloud URL e.g. https://nexcloud.com/', required=True)
args = parser.parse_args()

nextcloud_url = args.url


# Downloads a current list of plugins from the nextcloud website
def download_plugin_lists(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    for a in soup.find_all('a', href=True):
        if "/apps/" in a['href']:
            plugins.add(a['href'][6:])


# Downloads a current list of plugins from the nextcloud repository
def download_plugin_lists_from_repository(url):
    for i in range (1,12):
        r = requests.get(url+str(i))
        soup = BeautifulSoup(r.content, 'html5lib')
        for a in soup.find_all('a', href=True):
            if a['href'].startswith("/nextcloud/"):
                plugins.add(a['href'].split("/")[2])


# Enumerate Plugins
def enumerate_plugins():
    with alive_bar(len(plugins) * len(files)) as bar:
        for plugin in plugins:
            for file in files:
                url = nextcloud_url + 'apps/' + plugin + file
                r = requests.get(url,verify=False,allow_redirects=False)
                bar()
                if r.status_code == 200:
                    print("Found Plugin %s: %s" %(plugin,url))



# Request status.php and get nextcloud version
def find_nextcloud(url):
    status_url = url + status
    r = requests.get(status_url,verify=False,allow_redirects=False)
    if r.status_code == 200 and "Nextcloud" in str(r.content):
        resp = json.loads(r.content)
        print("--- Identified Nextcloud ---")
        print("Version: %s" %resp["version"] )
    else:
        print("--- Can not find Nextcloud. Are you sure to continue? [y/n]")
        anwser = input()
        if anwser == 'n':
            exit(0)
        elif anwser != 'y':
            print("--- Wrong input... ---")
            exit(0)



print("--- Download Plugins from %s ---" %download_url)
download_plugin_lists(download_url)

print("--- Download Plugins from %s ---" %download_url_repository)
download_plugin_lists_from_repository(download_url_repository)

length_plugins = len(plugins)
print("--- Found a total of %i Plugins ---" %length_plugins)

find_nextcloud(nextcloud_url)

print("--- Enumerate Nextcloud Plugins from %s ---" %nextcloud_url)
enumerate_plugins()

