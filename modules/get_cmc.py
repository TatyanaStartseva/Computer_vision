from smsactivate.api import SMSActivateAPI
from main import request, api_key
import time
import subprocess
import modules.config
from modules.image_processing import find_image, click_image, pyautogui

def main(countries):
    sa = SMSActivateAPI(api_key)
    sa.debug_mode = True
    try:
        activeActivations = countries['activeActivations']
        for activation in activeActivations:
            id = activation["activationId"]
            phone = activation['phoneNumber']
            for i in range(4):
                command = f'"{modules.config.ADB_PATH}" shell input text "{phone}"'
                subprocess.run(command, shell=True)
                if find_image("image/ban.jpg", 2, 0.9):
                    click_image("image/ban_ok.jpg", False, 30)
                    for _ in range(10):
                        pyautogui.press("backspace")
                    activation_id_to_remove = id
                    countries['activeActivations'] = [activation for
                                                      activation in countries[
                                                          'activeActivations']
                                                      if activation[
                                                          'activationId'] != activation_id_to_remove]

                    continue
                click_image("image/next_number.jpg", False, 30)
                click_image("image/yes_registration.jpg", False, 30)
                res_activation = requests.get(
                    f"https://api.sms-activate.io/stubs/handler_api.php?api_key={api_key}&action=getStatus&id={id}")
                print(res_activation.text)
                if ':' in res_activation.text:
                    status, key = res_activation.text.split(':')
                    if status == "STATUS_OK":
                        command = f'"{modules.config.ADB_PATH}" shell input text "{key}"'
                        command_enter = f'"{modules.config.ADB_PATH}" shell input keyevent 66'
                        subprocess.run(command, shell=True)
                        subprocess.run(command_enter, shell=True)
                        click_image("image/continue_registration.jpg", False,
                                    30)
                        click_image("image/allow_registration.jpg", False, 30)
                        if find_image("image/allow_calls.jpg", 2, 0.9):
                            click_image("image/allow_calls.jpg", False, 30)
                        find_image("image/profile_photo.jpg", 30, 0.9)
                        random_name = fake.first_name()
                        command = f'"{modules.config.ADB_PATH}" shell input text "{random_name}"'
                        subprocess.run(command, shell=True)
                        click_image("image/last_name.jpg", False, 30)
                        random_surname = fake.last_name()
                        command = f'"{modules.config.ADB_PATH}" shell input text "{random_surname}"'
                        subprocess.run(command, shell=True)
                        return
                else:
                    time.sleep(5)
            if i == 4:
                click_image("image/arrow_comeback.jpg", False, 30)
                click_image("image/edit.jpg", False, 30)
                for _ in range(10):
                    pyautogui.press("backspace")
                activation_id_to_remove = id
                countries['activeActivations'] = [activation for
                                                  activation in countries[
                                                      'activeActivations']
                                                  if activation[
                                                      'activationId'] != activation_id_to_remove]
    except Exception as e:
        print(e)
if __name__ =="__main__":
    main()
