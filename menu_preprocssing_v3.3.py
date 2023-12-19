import pandas as pd
import requests
import csv

# 데이터셋 불러오기
menu_df = pd.read_csv('data.csv')
menu_list = menu_df['메뉴명']

product_df = pd.read_csv('data.csv')
product_list = product_df['제품명']

# API 키 읽기
with open("api_key.txt", "r") as file:
    api_key = file.readline().strip()

# API 설정
url = 'https://maum-gpt4.openai.azure.com/openai/deployments/maum-gpt4/chat/completions?api-version=2023-03-15-preview'
headers = {
    'api-key': api_key,
    'Content-Type': 'application/json'
}

def process_items(items_list, csv_file_name):
    responses = []

    # result.csv 파일 초기화
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['수정된 항목'])

    for item in items_list:
        success = False
        attempts = 0
        while not success and attempts < 3:
            attempts += 1
            try:
                response = requests.post(url, headers=headers, json={"messages": [{"role": "user", "content": f"띄어쓰기가 되어있지 않은 상품명을 최대한 의미 단위로 띄어쓰기를 해줘. 다른 부가 설명은 하지 말고, 띄어쓰기 된 상품명만 출력해줘.상품명:{item} "}]})
                response_content = response.json()
                result_text = response_content['choices'][0]['message']['content']
                success = True
            except KeyError:
                print(f"API 요청 중 오류 발생: {item} 재시도 중 ({attempts}/3)")
                if attempts == 3:
                    result_text = item  # 오류 발생 시 원본 항목만 저장

        responses.append(result_text)
        print(result_text)
        
        # 결과 저장
        with open(csv_file_name, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([result_text])

    return responses

# 메뉴명 전처리 및 저장
menu_responses = process_items(menu_list, 'only_menu_result.csv')
menu_df['메뉴명'] = menu_responses
menu_df.to_csv('menu.csv', index=False)

# 제품명 전처리 및 저장
product_responses = process_items(product_list, 'only_product_result.csv')
product_df['제품명'] = product_responses
product_df.to_csv('product.csv', index=False)
