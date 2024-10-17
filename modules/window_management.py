import pygetwindow as gw
from modules.logging_setup import logger


def resize_window(title, width, height, move_to_x=20, move_to_y=20):
    window = gw.getWindowsWithTitle(title)
    if window:
        window = window[0]
        window.resizeTo(width, height)
        window.activate()
        window.moveTo(move_to_x, move_to_y)
        logger.info(f"Окно '{title}' теперь имеет размер {width}x{height}.")
    else:
        logger.info(f"Окно '{title}' не найдено.")
