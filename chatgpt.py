#!/usr/bin/env python3
import sys
import os
import requests
from prompt_toolkit import prompt
from argparse import ArgumentParser
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

parser = ArgumentParser()
parser.add_argument('text', nargs='?', default="")
parser.add_argument("-d", "--debug", action="store_true",
                    help="debug mode : show only the request", )
parser.add_argument("-dr", "--debug-response", action="store_true",
                    help="debug mode : show the complete response", )

args = parser.parse_args()


def chatGPT(text: str, debug_mode: bool = False) -> str:
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + OPENAI_API_KEY,
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{
            'role': 'system',
            'content': text,
        }],
        "temperature": 1.0,
    }
    response = requests.post(url, headers=headers, json=data).json()
    if 'error' in response:
        output = response['error']['message']
    else:
        output = response['choices'][0]['message']['content']
    return output


text = args.text

if not text == '':
    if sys.stdin:
        lines = sys.stdin.readlines()
        text = text + ''.join(lines)
        text = text + ", show only the result"
    else:
        text = "show only the linux command for '" + text + "'"
    if args.debug:
        print(text)
    else:
        print(chatGPT(text, args.debug_response))
else:
    while True:
        text = prompt("ChatGPT : ")
        if text == "":
            break
        print(chatGPT(text, args.debug_response))
