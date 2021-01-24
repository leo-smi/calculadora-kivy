[app]
icon.filename = %(source.dir)s/icon.png
title = Calculadora
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3, kivy
orientation = portrait
fullscreen = 0
android.arch = armeabi-v7a
osx.kivy_version = 1.9.1
presplash.filename = splash.png
android.presplash_color = #000000

[buildozer]
log_level = 2
warn_on_root = 1

