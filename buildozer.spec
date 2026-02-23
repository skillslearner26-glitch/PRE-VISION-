[app]
title = Gurujodi
package.name = gurujodi
package.domain = org.test
source.dir = .
# This includes your .ttf font files in the APK
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 0.1
# Added requirements for your Firebase and Kivy code
requirements = python3,kivy==2.3.0,requests,urllib3,openssl,certifi
orientation = portrait
fullscreen = 0
# Permission needed for Firebase database
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.private_storage = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
