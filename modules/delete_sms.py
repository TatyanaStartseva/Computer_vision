from modules.image_processing import find_image,click_and_hold_image, click_image


def delete_sms():
    click_image("image/messages.jpg", False, 30)
    if not find_image("image/no_saved_messages.jpg", 2.5, 0.9):
        click_and_hold_image("image/profile.jpg", 2, 30)
        click_image("image/points.jpg", False, 30)
        click_image("image/highlight.jpg", False, 30)
        click_image("image/trash_messages.jpg", False, 30)
        click_image("image/yes.jpg", False, 30)
    click_image("image/main_page.jpg", False, 30)
