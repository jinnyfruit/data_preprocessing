import pandas as pd
import requests
import csv

# 데이터셋 불러오기
df = pd.read_csv('data.csv')
menu_list = df['메뉴명']

# API 키 읽기
with open("api_key.txt", "r") as file:
    api_key = file.readline().strip()

# API 설정
url = 'https://maum-gpt4.openai.azure.com/openai/deployments/maum-gpt4/chat/completions?api-version=2023-03-15-preview'
headers = {
    'api-key': api_key,
    'Content-Type': 'application/json'
}

# API 요청 및 응답 저장
responses = []

# result.csv 파일 초기화
with open('result.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['수정된 메뉴명'])

for menu in menu_list:
    success = False
    attempts = 0
    while not success and attempts < 3:
        attempts += 1
        try:
            response = requests.post(url, headers=headers, json={"messages": [{"role": "user", "content": f"띄어쓰기가 되어있지 않은 상품명을 최대한 의미 단위로 띄어쓰기를 해줘. 다른 부가 설명은 하지 말고, 띄어쓰기 된 상품명만 출력해줘.상품명:{menu} "}]})
            response_content = response.json()
            result_text = response_content['choices'][0]['message']['content']
            success = True
        except KeyError:
            print(f"API 요청 중 오류 발생: {menu} 재시도 중 ({attempts}/3)")
            if attempts == 3:
                result_text = menu  # 오류 발생 시 원본 메뉴명만 저장

    responses.append(result_text)
    print(result_text)
    
    # result.csv에 결과 저장
    with open('result.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([result_text])

# 모든 요청 완료 후 원본 데이터 파일에 메뉴명 교체
df['메뉴명'] = responses
df.to_csv('menu.csv', index=False)
