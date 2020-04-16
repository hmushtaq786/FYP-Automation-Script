import pyautogui as pg
import time
import subprocess

# a shortcut version to click on the center of the image provided
# pg.rightClick('vscode_icon.png')
# pg.click('vscode_angular-updated_tile.png')


def click_vscode():
    vscode_icon = None
    # i = 0
    while vscode_icon is None:
        vscode_icon = pg.locateOnScreen('./images/vscode_icon_dark.png')
        if vscode_icon is None:
            vscode_icon = pg.locateOnScreen('./images/vscode_icon_light.png')
        if vscode_icon is None:
            vscode_icon = pg.locateOnScreen('./images/vscode_icon_tiled.png')
        if vscode_icon is None:
            vscode_icon = pg.locateOnScreen(
                './images/vscode_icon_multiple.png')
        # i += 1
        # print(i)

    # right click vscode icon
    pg.rightClick(pg.center(vscode_icon))


def click_console():
    vscode_console = None
    # i = 0

    while vscode_console is None:
        vscode_console = pg.locateOnScreen(
            './images/vscode_console.PNG')
    # i += 1
    # print(i)
    return vscode_console


click_vscode()
vscode_connectico_tile = None
# # i = 0
while vscode_connectico_tile is None:
    vscode_connectico_tile = pg.locateOnScreen(
        './images/vscode_connectico_tile.png')
    if vscode_connectico_tile is None:
        vscode_connectico_tile = pg.locateOnScreen(
            './images/vscode_connectico_tile_light.png')
# # i += 1
# # print(i)

# click vscode connectico tile
pg.click(pg.center(vscode_connectico_tile))
time.sleep(3)
pg.hotkey('winleft', 'up')

pg.click(pg.center(click_console()))
pg.write('conda activate myDjangoEnv')
pg.press('enter')

vscode_django_activated = None
# # i = 0

while vscode_django_activated is None:
    vscode_django_activated = pg.locateOnScreen(
        './images/vscode_django_activated.PNG')
#     # i += 1
#     # print(i)

pg.write('python manage.py runserver')
pg.press('enter')


click_vscode()

vscode_angular_tile = None
# # i = 0

while vscode_angular_tile is None:
    vscode_angular_tile = pg.locateOnScreen(
        './images/vscode_angular-updated_tile.png')
    if vscode_angular_tile is None:
        vscode_angular_tile = pg.locateOnScreen(
            './images/vscode_angular-updated_tile_light.png')
#     # i += 1
#     # print(i)

# click vscode angular tile
pg.click(pg.center(vscode_angular_tile))
time.sleep(3)
pg.hotkey('winleft', 'up')

pg.click(pg.center(click_console()))
pg.write('ng serve')
pg.press('enter')

subprocess.call(
    'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
time.sleep(3)
pg.write('http://localhost:4200/')
pg.press('enter')
