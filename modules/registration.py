from modules.image_processing import click_image, find_image, pyautogui,click_and_hold_image
from modules.mail import mail
import modules.config
import pyperclip
import subprocess
from smsactivate.api import SMSActivateAPI
from modules.moving_folders import move_and_create_new_folder
from modules.window_management import resize_window
from modules.delete_and_install_tg import delete_and_install_tg
from modules.change_ip import change_ip
import time
import requests
from faker import Faker
import os,re
fake = Faker()
def registration(countries ,api_key, flag):
    if flag == 0:
        if find_image("image/sign_telegram.jpg", 120, 0.9):
            click_image("image/sign_telegram.jpg", False, 120)
            click_image("image/start.jpg", False, 30)
        elif  find_image("image/security.jpg", 2, 0.9):
            click_image("image/main_page.jpg", False, 30)
            click_image("image/sign_telegram.jpg", False, 120)
            click_image("image/start.jpg", False, 30)
        if find_image("image/continue.jpg", 2, 0.9):
            click_image("image/continue.jpg", False, 30)
            click_image("image/allow_calls.jpg", False, 30)

    sa = SMSActivateAPI(api_key)
    sa.debug_mode = True
    print(countries)
    try:
        activeActivations = countries['activeActivations']
        for activation in activeActivations:
            id = activation["activationId"]
            phone = activation['phoneNumber']
            time.sleep(1)
            command = f'"{modules.config.ADB_PATH}" shell input text "{phone}"'
            subprocess.run(command, shell=True)
            click_image("image/next_number.jpg", False, 30)
            click_image("image/yes_registration.jpg", False, 30)
            if find_image("image/attempts.jpg", 3, 0.9):
                click_image("image/main_page3.jpg", False, 30)
                change_ip()
                delete_and_install_tg()
                registration(countries, api_key, 0)
            if find_image("image/continue_registration.jpg", 2, 0.9):
                click_image("image/continue_registration.jpg", False, 30)
                click_image("image/allow_registration.jpg", False, 30)
                time.sleep(1)
                if find_image("image/allow_Calls1.jpg", 2, 0.9):
                    click_image("image/allow_calls.jpg", False, 30)
            if find_image("image/ban.jpg", 3, 0.9):
                click_image("image/ban_ok.jpg", False, 30)
                for _ in range(25):
                    pyautogui.press("backspace")
                activation_id_to_remove = id
                countries['activeActivations'] = [activation for
                                                  activation in countries[
                                                      'activeActivations']
                                                  if activation[
                                                      'activationId'] != activation_id_to_remove]
                print(countries)
                if len(countries['activeActivations'])!=0:
                                    continue
                else:
                    return 1,countries
            if find_image("image/email.jpg", 4, 0.9):
                    click_image("image/comeback_editCode.jpg", False, 30)
                    for _ in range(25):
                        pyautogui.press("backspace")
                    activation_id_to_remove = id
                    countries['activeActivations'] = [activation for
                                                      activation in countries[
                                                          'activeActivations']
                                                      if activation[
                                                          'activationId'] != activation_id_to_remove]
                    print(countries)
                    if len(countries['activeActivations'] )!= 0 :
                        continue
                    else:
                        return 1,countries
            if find_image("image/check_your_email.jpg", 4, 0.9):
                click_image("image/check_comeback.jpg", False, 30)
                click_image("image/edit.jpg", False, 30)
                if find_image("image/edit_phone1.jpg", 3, 0.9):
                    click_image("image/edit_phone.jpg", False, 30)
                for _ in range(25):
                    pyautogui.press("backspace")
                activation_id_to_remove = id
                countries['activeActivations'] = [activation for
                                                  activation in countries[
                                                      'activeActivations']
                                                  if activation[
                                                      'activationId'] != activation_id_to_remove]
                print(countries)
                if len(countries['activeActivations']) != 0:
                    continue
                else:
                    return 1, countries
            if find_image("image/choose_your_email.jpg",2,0.9):
                mail()
            if find_image("image/VOIP.jpg", 1, 0.9):
                click_image("image/voipOk.jpg", False, 30)
                for _ in range(25):
                    pyautogui.press("backspace")
                activation_id_to_remove = id
                countries['activeActivations'] = [activation for
                                                  activation in countries[
                                                      'activeActivations']
                                                  if activation[
                                                      'activationId'] != activation_id_to_remove]
                print(countries)
                if len(countries['activeActivations']) != 0:
                    continue
                else:
                    return 1, countries
            for i in range(5):
                res_activation = requests.get(
                    f"https://api.sms-activate.io/stubs/handler_api.php?api_key={api_key}&action=getStatus&id={id}")
                print(res_activation.text)
                if ':' in res_activation.text:
                    status, key = res_activation.text.split(':')
                    if status == "STATUS_OK":
                        time.sleep(2)
                        command = f'"{modules.config.ADB_PATH}" shell input text "{key}"'
                        command_enter = f'"{modules.config.ADB_PATH}" shell input keyevent 66'
                        subprocess.run(command, shell=True)
                        subprocess.run(command_enter, shell=True)
                        if find_image("image/password.jpg", 3, 0.9):
                            click_image("image/arrow_password.jpg", False, 30)
                            for _ in range(25):
                                pyautogui.press("backspace")
                            if len(countries['activeActivations'] )!= 0 :
                                continue
                            else:
                                return 1,countries
                        if find_image("image/allow_calls.jpg", 2, 0.9):
                            click_image("image/allow_calls.jpg", False, 30)
                        if find_image("image/choose_lang.jpg", 4, 0.9):
                            click_image("image/main_page2.jpg", False, 30)
                            activation_id_to_remove = id
                            countries['activeActivations'] = [activation for
                                                              activation in
                                                              countries[
                                                                  'activeActivations']
                                                              if activation[
                                                                  'activationId'] != activation_id_to_remove]
                            return 0, countries
                        find_image("image/profile_photo.jpg", 30, 0.9)
                        random_name = fake.first_name()
                        command = f'"{modules.config.ADB_PATH}" shell input text "{random_name}"'
                        subprocess.run(command, shell=True)
                        click_image("image/last_name.jpg", False, 30)
                        random_surname = fake.last_name()
                        command = f'"{modules.config.ADB_PATH}" shell input text "{random_surname}"'
                        subprocess.run(command, shell=True)
                        click_image("image/ok_makeAccount.jpg", False, 30)
                        click_image("image/accept.jpg", False, 30)
                        click_image("image/allow_registration.jpg", False, 30)
                        if find_image("image/turn_on.jpg", 3, 0.8):
                            click_image("image/continue_turn_on.jpg", False, 30)
                        if find_image("image/choose_lang.jpg", 2, 0.9):
                            click_image("image/ban_ok.jpg", False, 30)
                        script_dir = os.path.dirname(
                            os.path.abspath(__file__))
                        os.chdir(script_dir)
                        relative_path = os.path.join('..', 'Telegram',
                                                     'Telegram.exe')
                        absolute_path = os.path.abspath(relative_path)
                        process = subprocess.Popen(absolute_path)
                        time.sleep(1)
                        resize_window(modules.config.TELEGRAM_TITLE,
                                      modules.config.TELEGRAM_WIDTH,
                                      modules.config.TELEGRAM_HEIGHT, 700, 100)
                        click_image("../image/start_desktop.jpg", False, 30)
                        if find_image("../image/log_in.jpg", 2, 0.9):
                            click_image("../image/log_in.jpg", False, 30)
                            time.sleep(1.5)
                            for _ in range(5):
                                pyautogui.press("backspace")
                            pyautogui.write(phone)
                            pyautogui.press("enter")
                        click_image("../image/teleSign.jpg", False, 30)
                        time.sleep(1)
                        click_and_hold_image("../image/key.jpg", 2, 30)
                        time.sleep(1)
                        click_image("../image/copy.jpg", False, 30)
                        text = pyperclip.paste()
                        print(text)
                        numbers = ''.join(re.findall(r'\b\d{5}\b', text))
                        print(numbers)
                        click_image("../image/add_key.jpg", False, 30)
                        pyautogui.write(numbers)
                        time.sleep(2)
                        click_image("../image/lines.jpg", False, 30)
                        click_image("../image/settings1.jpg", False, 30)
                        click_image("../image/privacy.jpg", False, 30)
                        click_image("../image/sign_key.jpg", False, 30)
                        click_image("../image/create.jpg", False, 30)
                        time.sleep(2)
                        pyautogui.write("aisender2420")
                        click_image("../image/reEnter.jpg", False, 30)
                        time.sleep(1)
                        pyautogui.write("aisender2420")
                        click_image("../image/continue2fa.jpg", False, 30)
                        time.sleep(1)
                        pyautogui.write("aisender")
                        click_image("../image/continue2fa.jpg", False, 30)
                        click_image("../image/skipEmail.jpg", False, 30)
                        click_image("../image/skipEmail1.jpg", False, 30)
                        process.terminate()
                        move_and_create_new_folder(r'../users', r'../Telegram')
                        click_image("../image/main_page.jpg", False, 30)
                        activation_id_to_remove = id
                        countries['activeActivations'] = [activation for
                                                          activation in
                                                          countries[
                                                              'activeActivations']
                                                          if activation[
                                                              'activationId'] != activation_id_to_remove]
                        os.chdir("..")
                        current_directory = os.getcwd()
                        print("Текущая директория:", current_directory)
                        return 0, countries
                else:
                    time.sleep(5)
            if i == 4:
                click_image("image/arrow_comeback.jpg", False, 30)
                if find_image("image/edit.jpg", 2, 0.9):
                    click_image("image/edit.jpg", False, 30)
                for _ in range(25):
                    pyautogui.press("backspace")
                activation_id_to_remove = id
                countries['activeActivations'] = [activation for
                                                  activation in countries[
                                                      'activeActivations']
                                                  if activation[
                                                      'activationId'] != activation_id_to_remove]
                return 1, countries
        if len(activeActivations)==0:
            return 1,countries
        else:
            activation_id_to_remove = id
            countries['activeActivations'] = [activation for
                                              activation in countries[
                                                  'activeActivations']
                                              if activation[
                                                  'activationId'] != activation_id_to_remove]
            return 1,countries
    except Exception as e:
         print(e)
