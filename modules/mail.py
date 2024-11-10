import requests
import json
import time
import re
import modules.config
import subprocess
import pyautogui
from modules.image_processing import click_image, find_image
base_url = 'https://app.sonjj.com/v1'

headers = {
    'Accept': 'application/json',
    'X-Api-Key': '513d74dab7b98f6ea4e873d12dfc4646'
};

def get_inbox(email):
    print(type(email))
    email = str(email)
    url = f"https://app.sonjj.com/v1/temp_gmail/inbox?email={email}&timestamp=0"
    print(url)
    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code == 200:
        inbox_data = response.json()
        print(inbox_data)
        if inbox_data and inbox_data.get('messages'):
            print(f"Found {len(inbox_data['messages'])} messages.")
            return inbox_data['messages']
        else:
            print("No messages found.")
            return None
    else:
        click_image("image/arrow_comeback.jpg", False, 30)
        for _ in range(25):
            pyautogui.press("backspace")
        mail()

def get_message(email, message_id):
    url = f'{base_url}/temp_gmail/message?email={email}&mid={message_id}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        message_data = response.json()
        print("Message data:", message_data)
        return message_data
    else:
        print(f"Error fetching message: {response.text}")
        return None

def mail():
    while True:
        with open('modules/emails.json', 'r') as f:
            data = json.load(f)
        email = data[0]
        with open('modules/emails.json', 'w') as f:
            json.dump(data[1:], f)
        print(email)
        if email:
                command = f'"{modules.config.ADB_PATH}" shell input text "{email}"'
                subprocess.run(command, shell=True)
                click_image("image/next_email.jpg", False, 30)
                time.sleep(10)
                messages = get_inbox(email)
                if messages:
                    for message in messages:
                        print(message)
                        message_id = message['mid']
                        print(message_id)
                        message = get_message(email, message_id)
                        if message:
                            match = re.search(r'\b\d{6}\b', str(message['body']))
                            code = None
                            if match:
                                code = match.group()
                            print("Message content:", code)
                            command = f'"{modules.config.ADB_PATH}" shell input ' \
                                      f'text "{code}"'
                            subprocess.run(command, shell=True)
                            time.sleep(1)
                            if find_image("image/wrongEmail.jpg", 6, 0.7):
                                click_image("image/wrongEmail.jpg", False, 30)
                                click_image("image/ok_wrongEmail.jpg", False, 30)
                                click_image("image/arrowComeback.jpg", False, 30)
                                click_image("image/arrow_choose.jpg", False, 30)
                                for _ in range(25):
                                    pyautogui.press("backspace")
                            else:
                                return message

