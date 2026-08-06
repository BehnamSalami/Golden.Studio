[app]

title = Golden Studio

package.name = goldenstudio
package.domain = com.goldenstudio

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,json,db,txt,ttf

version = 1.0


requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,sqlite3

p4a.branch = release-2024.01.21


orientation = portrait

fullscreen = 0


android.api = 35

android.minapi = 24


android.ndk = 25b


android.archs = arm64-v8a


android.accept_sdk_license = True


android.permissions = INTERNET



[buildozer]

log_level = 2

warn_on_root = 1