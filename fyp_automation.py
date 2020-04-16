import pyautogui as pg

# a shortcut version to click on the center of the image provided
# pg.rightClick('vscode_icon.png')
# pg.click('vscode_angular-updated_tile.png')


def click_vscode():
    vscode_icon = None
    # i = 0
    while vscode_icon is None:
        vscode_icon = pg.locateOnScreen('vscode_icon_dark.png')
        if vscode_icon is None:
            vscode_icon = pg.locateOnScreen('vscode_icon_light.png')
        if vscode_icon is None:
            vscode_icon = pg.locateOnScreen('vscode_icon_tiled.png')
        if vscode_icon is None:
            vscode_icon = pg.locateOnScreen('vscode_icon_multiple.png')
        # i += 1
        # print(i)

    # right click vscode icon
    pg.rightClick(pg.center(vscode_icon))


click_vscode()

vscode_angular_tile = None
# # i = 0

while vscode_angular_tile is None:
    vscode_angular_tile = pg.locateOnScreen('vscode_angular-updated_tile.png')
    if vscode_angular_tile is None:
        vscode_angular_tile = pg.locateOnScreen(
            'vscode_angular-updated_tile_light.png')
#     # i += 1
#     # print(i)

# click vscode angular tile
pg.click(pg.center(vscode_angular_tile))


click_vscode()
vscode_connectico_tile = None
# i = 0
while vscode_connectico_tile is None:
    vscode_connectico_tile = pg.locateOnScreen('vscode_connectico_tile.png')
    if vscode_connectico_tile is None:
        vscode_connectico_tile = pg.locateOnScreen(
            'vscode_connectico_tile_light.png')
# i += 1
# print(i)

# click vscode angular tile
pg.click(pg.center(vscode_connectico_tile))
