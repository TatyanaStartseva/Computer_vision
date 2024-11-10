import subprocess
import time
import modules.config
from modules.image_processing import find_image, click_image, click_and_hold_image, pyautogui


def delete_and_install_tg():
    click_and_hold_image("image/sign_telegram.jpg", 1, 30)
    click_image("image/about_app.jpg", False, 30)
    click_image("image/trash.jpg", False, 30)
    click_image("image/ok_delete.jpg", False, 30)

    click_image("image/folder.jpg", False, 3)
    if find_image("image/apk.jpg", 4, 0.9):
        click_image("image/apk.jpg", False, 30)
    click_image("image/teleApk.jpg", False, 10)
    click_image("image/setApk.jpg", False, 3)
    click_image("image/openApk.jpg", False, 30)
    return
    # click_image("image/play.jpg", False, 30)
    # if find_image("image/loupe.jpg", 3, 0.9):
    #     click_and_hold_image("image/loupe.jpg", 1)
    #     click_image("image/loupe.jpg", False, 30)
    # else:
    #     if find_image("image/loupe2.jpg", 2, 0.9):
    #         click_image("image/loupe2.jpg", False, 30)
    #         click_image("image/loupe3.jpg", False, 30)
    #     else:
    #         click_image("image/loupe3.jpg", False, 30)
    # for _ in range(30):
    #     pyautogui.press("backspace")
    # time.sleep(3)
    # formatted_text = modules.config.SEARCH_TEXT.replace(" ", "%s")
    # command = f'"{modules.config.ADB_PATH}" shell input text "{formatted_text}"'
    # command_enter = f'"{modules.config.ADB_PATH}" shell input keyevent 66'
    # subprocess.run(command, shell=True)
    # subprocess.run(command_enter, shell=True)
    # click_image("image/set_up.jpg", False, 30)
    # click_image("image/main_page.jpg", False, 30)
