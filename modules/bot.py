import os
import sys
import vimeo
from datetime import datetime
from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests
from dotenv import load_dotenv
from modules.logging_setup import logger

load_dotenv()
app = FastAPI()

BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
VIDEO_TOKEN = os.getenv("VIDEO_TOKEN")
KEY = os.getenv("KEY")
SECRET= os.getenv("SECRET")
CHATS_IDS = os.getenv("CHATS_IDS", '').split(',')

class Telegram(BaseModel):
    update_id:int
    message: dict

def upload_transfersh(file, description):
    client = vimeo.VimeoClient(
        token=VIDEO_TOKEN,
        key=KEY,
        secret=SECRET
    )
    curr_time = (datetime.now()).strftime("%Y-%m-%d %H-%M-%S")
    try:
        uri = client.upload(file, data={
            'name': f'{curr_time}',
            'description': f'{description}'
        })
        print('Видео успешно загружено. URI видео: %s' % uri)

        response = client.get(uri + '?fields=link').json()
        video_link = response.get('link')
        if video_link:
            return video_link
        else:
            print("Ошибка при получении ссылки на видео.")

    except vimeo.exceptions.VideoUploadFailure as e:
        print("Ошибка при загрузке видео:", e)


def send_video(video_path, description):
    link = upload_transfersh(video_path, description)
    if link:
        return link
    else:
        return "Ошибка при отправке ссылки на видео "


def send_messages(text:str):
    url = f'{BASE_URL}/sendMessage'
    for chat in CHATS_IDS:
        message ={
            'chat_id': chat,
            'text':text
        }
        response = requests.post(url, json = message)
        if response.status_code != 200:
            logger.error(f"Ошибка при отправке сообщения в чат {chat} {response.text}")

@app.get('/start_registration')
def start_registration():
    #main()
    return {
        'status':'Запущена регистрация'
    }
@app.get('/stop')
def stop_registration():
    sys.exit()
    return {
        'status': 'Остановка регистрация'
    }