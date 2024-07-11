# temp-crhome

Генерация и запуск анонимных профилей Chrome

![Скриншот программы](/screenshot.png)

Анонимность достигается за счет:
 - использования прокси
 - подмены UserAgent
 - спуфинга часовых поясов
 - подмены отпечатков шрифтов, Canvas, WebGL

В проекте используются следующие расширения Chrome от сторонних разработчиков:
 - [Canvas Defender](https://mybrowseraddon.com/canvas-defender.html)
 - [WebGL Defender](https://mybrowseraddon.com/webgl-defender.html)
 - [Font Defender](https://mybrowseraddon.com/font-defender.html)
 - [Spoof Timezone](https://webextension.org/listing/spoof-timezone.html)

Если используется Windows необходимо добавить `WIN_PLATFORM = True` и указать путь до исполняемого файла в `CHROME_DIR`, в случаае Linux применеятся chromium из PATH.

Переменные `DELETE_USED_PROXIES`, `DELETE_USED_UA` определяют удаляются ли прокси и UA из файлов после создания профиля с ними.
