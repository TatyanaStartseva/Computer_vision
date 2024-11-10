import cv2
import  pyautogui
import numpy as np
import threading
from modules.logging_setup import logger

stop_recording = threading.Event()

def record_screen(file='recording.mp4', fps=3):
    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(file, fourcc, fps,screen_size)
    logger.info("Началась запись экрана ")
    while not stop_recording.is_set():
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame= cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)
    out.release()
    logger.info('Запись экрана остановлена и сохранена')