[app]

title = Golden Studio

package.name = goldenstudio

package.domain = com.goldenstudio


source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,db,txt


version = 0.1


requirements = python3,kivy==2.3.0,kivymd==1.2.0


orientation = portrait


fullscreen = 0


# Android

android.api = 34

android.minapi = 24

android.ndk = 25b


android.archs = arm64-v8a


android.accept_sdk_license = True


# استفاده از SDK نصب شده در GitHub Actions

android.sdk_path = /usr/local/lib/android/sdk


android.permissions = INTERNET



[buildozer]

log_level = 2

warn_on_root = 1