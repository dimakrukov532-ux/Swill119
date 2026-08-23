[app]
title = SWILL
package.name = swill
package.domain = org.swill
version = 1.0
source.dir = .
requirements = python3, flask, requests, telebot, pyjnius
android.permissions = INTERNET, ACCESS_WIFI_STATE, ACCESS_NETWORK_STATE, WRITE_EXTERNAL_STORAGE, FOREGROUND_SERVICE, SYSTEM_ALERT_WINDOW
android.api = 30
android.minapi = 21
android.target_sdk = 30
android.ndk = 28c
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r28c
android.sdk_path = /home/runner/android-sdk

[buildozer]
log_level = 2
warn_on_root = 1
