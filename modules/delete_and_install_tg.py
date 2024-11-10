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
    
