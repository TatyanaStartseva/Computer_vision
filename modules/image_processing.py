import time
import cv2
import pyautogui
import numpy as np
from modules.logging_setup import logger


def find_image(image_path, timeout=30, threshold=0.9):
    start_time = time.time()
    while time.time() - start_time < timeout:
        needle_image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        haystack_image = pyautogui.screenshot()
        haystack_image = np.array(haystack_image)[:, :, ::-1]
        result = cv2.matchTemplate(haystack_image, needle_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val >= threshold:
            logger.info(f"Изображение {image_path} найдено")
            return True
        else:
            time.sleep(1)
    logger.info(f"Изображение {image_path} не найдено за {timeout} сек.")
    return False


def click_image(image_path, right_click=False, timeout=60):
    start_time = time.time()
    logger.info(f"Начинаю поиск координат для элемента {image_path}")
    needle_image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    while True:
        if time.time() - start_time > timeout:
            raise TimeoutError(f"Картинка {image_path} не найдена за {timeout} секунд")
        time.sleep(0.5)
        haystack_image = pyautogui.screenshot()
        haystack_image = np.array(haystack_image)[:, :, ::-1]
        result = cv2.matchTemplate(haystack_image, needle_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.9:
            x, y = max_loc
            logger.info(f"Координаты элемента {image_path} найдены: ({x}, {y})")
            pyautogui.moveTo(x, y)
            if right_click:
                pyautogui.rightClick(x, y)
                logger.info(f"Выполнено правое нажатие на координатy ({x}, {y})")
            else:
                pyautogui.click(x, y)
                logger.info(f"Выполнено нажатие на координатy ({x}, {y})")
            break


def click_and_hold_image(image_path, hold_time=3, timeout=60):
    start_time = time.time()
    logger.info(f"Начинаю поиск координат для элемента {image_path}")
    needle_image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    while True:
        if time.time() - start_time > timeout:
            raise TimeoutError(f"Картинка {image_path} не найдена за {timeout} секунд")

        time.sleep(0.5)
        haystack_image = pyautogui.screenshot()
        haystack_image = np.array(haystack_image)[:, :, ::-1]
        result = cv2.matchTemplate(haystack_image, needle_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.9:
            x, y = max_loc
            logger.info(f"Координаты элемента {image_path} найдены: ({x}, {y})")
            pyautogui.moveTo(x, y)
            pyautogui.mouseDown(x, y)
            logger.info(
                f"Удержание левой кнопки мыши на координате ({x}, {y}) в течение {hold_time} секунд"
            )
            time.sleep(hold_time)
            pyautogui.mouseUp()
            logger.info(f"Левая кнопка мыши отпущена на координате ({x}, {y})")
            break
