import json
from modules.logging_setup import logger
import time
import threading
import serial
import requests
import os
import sys
import subprocess
from dotenv import load_dotenv
from modules.window_management import resize_window
from modules import config
from modules.delete_and_install_tg import delete_and_install_tg
from modules.bot import send_messages, send_video
from modules.filming import record_screen,stop_recording
from modules.change_ip import change_ip
from modules.image_processing import click_image, find_image
from modules.registration import registration
load_dotenv()
api_key = os.getenv('API_KEY')
SERIAL_PORT = 'CON'
BAUD_RATE = 1200
DATA_BITS = serial.SEVENBITS
PARITY = serial.PARITY_NONE
STOP_BITS = serial.STOPBITS_ONE
video_file = 'screen_recording.mp4'

def main():
    resize_window(config.WINDOW_TITLE, config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    flag = 1 #0
    active_activations = []
    countries = {}
    recording_thread = threading.Thread(target=record_screen, args=(video_file,))

    while True:
        try:
            if not recording_thread.is_alive():
                recording_thread = threading.Thread(target=record_screen, args=(video_file,))
                recording_thread.start()

            response = requests.get(
                f"https://api.sms-activate.io/stubs/handler_api"
                f".php?api_key={api_key}&action=getNumber&service=tg&country=16&maxPrice=105")
            parts = response.text.split(":")
            balance = requests.get(f"https://api.sms-activate.guru/stubs/handler_api.php?api_key={api_key}&action=getBalance")
            _, balance = balance.text.split(":")

            if len(parts) != 3 or parts[0] != "ACCESS_NUMBER":
                print("Запрос на получение номера не был успешным, повтор попытки. Ответ:", parts[0])
                send_messages(f"Запрос на получение номера не был успешным, повтор попытки. Ответ: {parts[0]}")

                if parts[0] == "NO_BALANCE":
                    active_id = requests.get(f"https://api.sms-activate.guru/stubs/handler_api.php?api_key={api_key}&action=getActiveActivations")
                    active_id = json.loads(active_id.text)
                    list_id = [i['activationId'] for i in active_id['activeActivations']]
                    for activation_id in list_id:
                        answer = requests.get(f"https://api.sms-activate.guru/stubs/handler_api.php?api_key={api_key}&action=setStatus&status=8&id={int(activation_id)}")
                        print(answer.text)
                continue

            activation_id = parts[1]
            phone_number = parts[2]
            active_activations.append({
                'activationId': activation_id,
                'phoneNumber': phone_number
            })
            countries['activeActivations'] = active_activations

            if flag == 0:
                change_ip()
                delete_and_install_tg()

            flag, countries = registration(countries, api_key, flag, balance, recording_thread, video_file)
            active_activations = []

        except Exception as e:
            logger.error("Ошибка в main", exc_info=True)
            send_messages(f"Ошибка в main: {e}")
            stop_recording.set()
            recording_thread.join()
            send_video(video_file, '*** Ошибка в main')
            os.remove(video_file)
            time.sleep(100)
            subprocess.run([sys.executable, 'main.py'])
            sys.exit()
        finally:
            stop_recording.set()
            recording_thread.join()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        send_messages(f"Глобальная ошибка {e}")
        logger.critical("Ошибка", exc_info=True)
        time.sleep(100)
        if find_image("image/main_page.jpg", 3, 0.9):
            click_image("image/main_page.jpg", False, 30)
        delete_and_install_tg()
        stop_recording.set()
        send_video(video_file, '*** Глобальная ошибка')
        os.remove(video_file)
        subprocess.run([sys.executable, 'main.py'])
        sys.exit()