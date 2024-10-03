# nextcloud-plugin-fuzzer
- Enumerates Nextcloud Plugins/Apps by enumerating typical javascript and image files
- Downloads a list current list of plugins from official sources

## Installation

    git clone git@github.com:C411e/nextcloud-plugin-fuzzer.git
    cd nextcloud-plugin-fuzzer
    pip3 install -r requirements.txt

## Parameters
    -u, --url       Nextcloud URL to test e.g. https://nextcloud.com/

## Examples

    python3 nextcloud-plugin-fuzzer.py -u https://nextcloud.com/
    --- Download Plugins from https://apps.nextcloud.com/ ---
    --- Download Plugins from https://github.com/orgs/nextcloud/repositories?page= ---
    --- Found a total of 647 Plugins ---
    --- Identified Nextcloud ---
    Version: 24.0.12.1
    --- Enumerate Nextcloud Plugins from https://nextcloud.com/ ---
    on 151: Found Plugin files_automatedtagging: https://nextcloud.com/apps/files_automatedtagging/img/app.svg
    on 326: Found Plugin deck: https://nextcloud.com/apps/deck/img/favicon.svg
    on 336: Found Plugin deck: https://nextcloud.com/apps/deck/img/circles.svg
    on 545: Found Plugin activity: https://nextcloud.com/apps/activity/js/script.js
    on 551: Found Plugin activity: https://nextcloud.com/apps/activity/img/change.svg
    on 554: Found Plugin activity: https://nextcloud.com/apps/activity/js/admin.js
    on 560: Found Plugin activity: https://nextcloud.com/apps/activity/js/settings.js
    on 1191: Found Plugin quicknotes: https://nextcloud.com/apps/quicknotes/js/script.js
    on 1205: Found Plugin quicknotes: https://nextcloud.com/apps/quicknotes/img/app.svg
    on 1459: Found Plugin theming: https://nextcloud.com/apps/theming/img/app-dark.svg
    on 1460: Found Plugin theming: https://nextcloud.com/apps/theming/img/app.svg
    on 1935: Found Plugin registration: https://nextcloud.com/apps/registration/img/app-dark.svg
    on 1936: Found Plugin registration: https://nextcloud.com/apps/registration/img/app.svg
    on 2126: Found Plugin keeweb: https://nextcloud.com/apps/keeweb/js/script.js
    on 2140: Found Plugin keeweb: https://nextcloud.com/apps/keeweb/img/app.svg
    on 2179: Found Plugin tasks: https://nextcloud.com/apps/tasks/img/favicon.svg
    on 2330: Found Plugin serverinfo: https://nextcloud.com/apps/serverinfo/js/script.js
    on 2343: Found Plugin serverinfo: https://nextcloud.com/apps/serverinfo/img/app-dark.svg
    on 2344: Found Plugin serverinfo: https://nextcloud.com/apps/serverinfo/img/app.svg
    on 4418: Found Plugin text: https://nextcloud.com/apps/text/img/app.svg
    on 4876: Found Plugin privacy: https://nextcloud.com/apps/privacy/img/app-dark.svg
    on 4877: Found Plugin privacy: https://nextcloud.com/apps/privacy/img/app.svg
    on 5047: Found Plugin viewer: https://nextcloud.com/apps/viewer/img/app.svg
    on 5739: Found Plugin nextcloud_announcements: https://nextcloud.com/apps/nextcloud_announcements/js/admin.js
    on 5743: Found Plugin nextcloud_announcements: https://nextcloud.com/apps/nextcloud_announcements/img/app-dark.svg
    on 5744: Found Plugin nextcloud_announcements: https://nextcloud.com/apps/nextcloud_announcements/img/app.svg
    on 6083: Found Plugin sendent: https://nextcloud.com/apps/sendent/img/app-dark.svg
    on 6084: Found Plugin sendent: https://nextcloud.com/apps/sendent/img/app.svg
    on 6085: Found Plugin sendent: https://nextcloud.com/apps/sendent/js/settings.js
    on 6424: Found Plugin polls: https://nextcloud.com/apps/polls/img/app.svg
    on 6463: Found Plugin notes: https://nextcloud.com/apps/notes/img/favicon.svg
    on 7211: Found Plugin forms: https://nextcloud.com/apps/forms/img/favicon.svg
    on 7259: Found Plugin bruteforcesettings: https://nextcloud.com/apps/bruteforcesettings/js/bruteforcesettings-main.js
    on 7660: Found Plugin files_retention: https://nextcloud.com/apps/files_retention/js/admin.js
    on 7665: Found Plugin files_retention: https://nextcloud.com/apps/files_retention/img/app.svg
    on 7728: Found Plugin survey_client: https://nextcloud.com/apps/survey_client/js/admin.js
    on 7732: Found Plugin survey_client: https://nextcloud.com/apps/survey_client/img/app-dark.svg
    on 7733: Found Plugin survey_client: https://nextcloud.com/apps/survey_client/img/app.svg
    on 7766: Found Plugin logreader: https://nextcloud.com/apps/logreader/img/app-dark.svg
    on 7767: Found Plugin logreader: https://nextcloud.com/apps/logreader/img/app.svg
    on 8282: Found Plugin contacts: https://nextcloud.com/apps/contacts/img/favicon.svg
    on 8284: Found Plugin contacts: https://nextcloud.com/apps/contacts/img/social.svg
    on 8292: Found Plugin contacts: https://nextcloud.com/apps/contacts/img/circles.svg
    on 8294: Found Plugin contacts: https://nextcloud.com/apps/contacts/img/app.svg
    on 8378: Found Plugin quota_warning: https://nextcloud.com/apps/quota_warning/img/app-dark.svg
    on 8379: Found Plugin quota_warning: https://nextcloud.com/apps/quota_warning/img/app.svg
    on 8380: Found Plugin quota_warning: https://nextcloud.com/apps/quota_warning/js/settings.js
    on 8496: Found Plugin circles: https://nextcloud.com/apps/circles/img/circles.svg
    on 8617: Found Plugin files_pdfviewer: https://nextcloud.com/apps/files_pdfviewer/img/app.svg
    on 8702: Found Plugin password_policy: https://nextcloud.com/apps/password_policy/img/app.svg
    on 9229: Found Plugin photos: https://nextcloud.com/apps/photos/img/app.svg
    on 9232: Found Plugin files_rightclick: https://nextcloud.com/apps/files_rightclick/js/script.js
    on 9237: Found Plugin files_rightclick: https://nextcloud.com/apps/files_rightclick/js/files.js
    on 9382: Found Plugin files_videoplayer: https://nextcloud.com/apps/files_videoplayer/img/app.svg
    on 9563: Found Plugin notifications: https://nextcloud.com/apps/notifications/img/notifications.svg
    on 9620: Found Plugin firstrunwizard: https://nextcloud.com/apps/firstrunwizard/img/app.svg
    on 9846: Found Plugin spreed: https://nextcloud.com/apps/spreed/img/favicon.svg
    on 9857: Found Plugin spreed: https://nextcloud.com/apps/spreed/img/app-dark.svg
    on 9858: Found Plugin spreed: https://nextcloud.com/apps/spreed/img/app.svg
    |████████████████████████████████████████| 10999/10999 [100%] in 34:25.0 (5.33/s) 
