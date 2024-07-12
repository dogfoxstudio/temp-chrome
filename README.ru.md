# temp-chrome
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://https://github.com/dogfoxstudio/temp-chrome/edit/main/README.md)
[![ru](https://img.shields.io/badge/lang-ru-green.svg)](https://https://github.com/dogfoxstudio/temp-chrome/main/README.ru.md)

Генерация и запуск анонимных профилей Chrome

![Скриншот программы](/screenshot.png)

Кнопкой `Новый профиль` создается новый профиль со случайным 6 значным именем, хранящийся в папке 
`./profiles/<имя профиля>` при этом используются случайные UserAgent из файла `useragents.txt` и прокси из файла `proxies.txt`.
Насатройки профиля хранятся в файле `./profiles/<имя профиля>/settings.txt`

При запуске существующего профиля используются UA и прокси выбранные при создании профиля, которые можно изменить редактированием `./profiles/<имя профиля>/settings.txt`.

Анонимность достигается за счет:
 - использования прокси
 - независимости профилей между собой
 - подмены UserAgent
 - спуфинга часовых поясов
 - подмены отпечатков шрифтов, Canvas, WebGL

В проекте используются следующие расширения Chrome от сторонних разработчиков:
 - [Canvas Defender](https://mybrowseraddon.com/canvas-defender.html)
 - [WebGL Defender](https://mybrowseraddon.com/webgl-defender.html)
 - [Font Defender](https://mybrowseraddon.com/font-defender.html)
 - [Spoof Timezone](https://webextension.org/listing/spoof-timezone.html)

## Запуск

Запуск осуществляется вызовом 
```{python}
python gui_launch.py
```

Если используется Windows предварительно необходимо добавить `WIN_PLATFORM = True` и указать путь до исполняемого файла в `CHROME_DIR` в файле `gui_launch.py`, в случаае Linux применеятся chromium из PATH. 

Единственное требование версия Chrome/Chromium должна быть не ниже 88, допускается использование браузеров производных от Chrome (Brave, Edge, Yandex.Browser)

Переменные `DELETE_USED_PROXIES`, `DELETE_USED_UA` определяют удаляются ли прокси и UA из файлов после создания профиля с ними.
