[app]
title = MzindaTrack
package.name = mzindatrack
package.domain = org.mzindatrack
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ico,json
source.include_patterns = assets/*,data/*,*.py
source.exclude_exts = spec,md,yml,yaml
source.exclude_dirs = tests, bin, __pycache__, .git, .github, .buildozer
version = 1.0.0

# Use a Cython version compatible with the Python headers used by python-for-android
# Upgrading Cython avoids the _PyLong_AsByteArray signature mismatch when building
# against newer Python headers (e.g., Python 3.14).
requirements = python3,Cython>=3.0.15,kivy==2.2.1,requests,plyer,pyjnius==1.5.1

presplash.filename = assets/presplash.png
icon.filename = assets/icon.png
orientation = portrait
fullscreen = 0

# Android permissions
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,ACCESS_NETWORK_STATE

# API levels
android.api = 30
android.minapi = 21
android.ndk = 28c
android.ndk_api = 21

# Build flags
android.skip_update = False
android.accept_sdk_license = True
android.entrypoint = org.kivy.android.PythonActivity
android.apptheme = @style/Theme.AppCompat
android.archs = arm64-v8a
android.copy_libs = 1
android.use_androidx = True
android.neon = 0

# Disable libthorvg to avoid download failures
p4a.libthorvg = 0

# WebView support
android.gradle_dependencies = 'androidx.webkit:webkit:1.6.1'

# Python-for-Android settings
p4a.branch = master
p4a.bootstrap = sdl2

# Additional android configuration
android.window_background_color = #0a0f1e
android.logcat_filters = *:S python:D
android.debug = 1

[buildozer]
log_level = 2
warn_on_root = 1
build_dir = ./.buildozer
bin_dir = ./bin
