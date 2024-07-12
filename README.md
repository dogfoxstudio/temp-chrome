# temp-chrome

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://https://github.com/dogfoxstudio/temp-chrome/edit/main/README.md)
[![ru](https://img.shields.io/badge/lang-ru-green.svg)](https://https://github.com/dogfoxstudio/temp-chrome/main/README.ru.md)

Generate and launch anonymous Chrome profiles

![Program Screenshot](/screenshot.png)

By pressing `Новый профиль` one creates new anonymous profile with random 6 character name, which stores in folder `./profiles/<profile name>` using random UserAgent from the file `useragents.txt ` and the proxy from the file `proxies.txt `.
Profile settings are stored in `./profiles/<profile_name>/settings.txt`

When launching an existing profile, the UserAgent and proxy selected when creating the profile are used, which can be changed by editing `./profiles/<profile name>/settings.txt`.

Anonymity is achieved by:
- using proxy
- independence of profiles among themselves
- UserAgent spoofing
- time zone spoofing
- substitution of fake font, Canvas and WebGL footprints

The project uses the following Chrome extensions from third-party developers:
 - [Canvas Defender](https://mybrowseraddon.com/canvas-defender.html)
 - [WebGL Defender](https://mybrowseraddon.com/webgl-defender.html)
 - [Font Defender](https://mybrowseraddon.com/font-defender.html)
 - [Spoof Timezone](https://webextension.org/listing/spoof-timezone.html)

## Launch

The launch is carried out by execution of
```{python}
python gui_launch.py
```

If you are using Windows, you must first add `WIN_PLATFORM = True` and specify the path to the executable file in `CHROME_DIR` in the file `gui_launch.py `, in the case of Linux, chromium from PATH is used.

The only requirement is that the Chrome/Chromium version must be at least 88, it is allowed to use browsers derived from Chrome (Brave, Edge, Yandex.Browser)

The variables `DELETE_USED_PROXIES`, `DELETE_USED_UA` determine whether proxies and UA are deleted from files after creating a profile with them.
