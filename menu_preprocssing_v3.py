import pandas as pd
import csv
import requests
import json

#import dataset
df = pd.read_csv('menu.csv')
menu_list = df['메뉴명']

# read api key
with open("api_key.txt", "r") as file:
    api_key = file.readline().strip()

# set api key 
url = 'https://maum-gpt4.openai.azure.com/openai/deployments/maum-gpt4/chat/completions?api-version=2023-03-15-preview'
headers = {
    'api-key': api_key,
    'Content-Type': 'application/json'
}

# api request
responses = []

for menu in menu_list:
    print(menu)
    #quit()
    data = {
        "messages": [
            {
                "role": "user", 
                "content": f"띄어쓰기가 되어있지 않은 상품명을 최대한 의미 단위로 띄어쓰기를 해줘. 다른 부가 설명은 하지 말고, 띄어쓰기 된 상품명만 출력해줘. 상품명:{menu} "
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    response_content = response.json()
    print(response_content)
    result_json = response_content['choices'][0]['message']['content']
    print()
    print(result_json)
    quit()
    