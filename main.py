import serial
import requests
import os
from dotenv import load_dotenv
from modules.window_management import resize_window
from modules import config
from modules.delete_and_install_tg import delete_and_install_tg
from modules.change_ip import change_ip
from modules.registration import registration
load_dotenv()
api_key = os.getenv('API_KEY')
SERIAL_PORT = 'CON'
BAUD_RATE = 1200
DATA_BITS = serial.SEVENBITS
PARITY = serial.PARITY_NONE
STOP_BITS = serial.STOPBITS_ONE


def main():
    resize_window(config.WINDOW_TITLE, config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    flag = 0
    active_activations =[]
    countries = {}
    while True:
        response = requests.get(
            f"https://api.sms-activate.io/stubs/handler_api"
            f".php?api_key="
            f"{api_key}&action=getNumber&service=tg&country=16&maxPrice=105")
        parts = response.text.split(":")
        if len(parts) != 3 or parts[0] != "ACCESS_NUMBER":
            print(f"Запрос на получение номера не был успешным, повтор попытки. Ответ : ",parts[0])
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
        flag,countries = registration(countries, api_key, flag)
        print("aften registration", countries)
        active_activations = []



if __name__ == "__main__":
    main()
