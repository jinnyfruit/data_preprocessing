import json

# 특수문자를 일반 문자로 대체하는 함수
def replace_special_characters(text):
    replacements = {
        '※': '-',
        '①': '1.',
        '②': '2.',
        '③': '3.',
        '④': '4.',
        '⑤': '5.',
        '⑥': '6.',
        '⑦': '7.',
        '⑧': '8.',
        '⑨': '9.',
        '⑩': '10.'
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def process_jsonl(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as input_file, \
         open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in input_file:
            data = json.loads(line)
            # 가정: JSON 객체 내에서 문자열을 처리할 필드의 이름이 'text'라고 가정
            if 'text' in data:
                data['text'] = replace_special_characters(data['text'])
            json.dump(data, output_file)
            output_file.write('\n')

# 파일 처리
# input_file_path = 'input.jsonl'  # 입력 JSONL 파일 경로
# output_file_path = 'output.jsonl'  # 출력 JSONL 파일 경로

#process_jsonl(input_file_path, output_file_path)
result = replace_special_characters("※공지사항 안내드립니다※ ①김지우 ②김준이 ③최영우")
print(result)