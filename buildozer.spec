[app]

title = Golden Studio

package.name = goldenstudio
package.domain = com.goldenstudio

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,json,db,txt,ttf

version = 1.0

requirements = python3==3.11,kivy==2.3.0,kivymd==1.2.0

orientation = portrait

fullscreen = 0

android.api = 34
android.minapi = 24

android.ndk = 27b

android.archs = arm64-v8a

android.accept_sdk_license = True

android.permissions = INTERNET


# جلوگیری از گرفتن Python جدید
p4a.branch = master

# استفاده از نسخه پایدار
p4a.version = 2024.1.21


[buildozer]

log_level = 2

warn_on_root = 1