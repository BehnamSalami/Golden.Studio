[app]

title = Golden Studio

package.name = goldenstudio

package.domain = com.goldenstudio


source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,json,db,txt,ttf


version = 0.1


requirements = python3,kivy==2.3.0,kivymd==1.2.0


orientation = portrait


fullscreen = 0


icon.filename = assets/icon.png


presplash.filename = assets/splash.png



[buildozer]


log_level = 2


warn_on_root = 1



[android]


android.api = 34

android.minapi = 24

android.ndk = 27c


android.archs = arm64-v8a


android.accept_sdk_license = True


android.permissions = INTERNET


p4a.branch = master