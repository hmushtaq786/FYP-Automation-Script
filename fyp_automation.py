import pyautogui as pg

# a shortcut version to click on the center of the image provided
# pg.rightClick('vscode_icon.png')
# pg.click('vscode_angular-updated_tile.png')

vscode_icon = None
# i = 0

while vscode_icon is None:
    vscode_icon = pg.locateOnScreen('vscode_icon_dark.png')
    if vscode_icon is None:
        vscode_icon = pg.locateOnScreen('vscode_icon_light.png')
    if vscode_icon is None:
        vscode_icon = pg.locateOnScreen('vscode_icon_tiled.png')
    # i += 1
    # print(i)

# right click vscode icon
pg.rightClick(pg.center(vscode_icon))

vscode_angular_tile = None
# i = 0

while vscode_angular_tile is None:
    vscode_angular_tile = pg.locateOnScreen('vscode_angular-updated_tile.png')
    print(vscode_angular_tile)
    # i += 1
    # print(i)
