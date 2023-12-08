import pandas as pd
from konlpy.tag import Okt
print("hello world")
def transform_compound_nouns(sentence):
    print(sentence)
    print()
    
    okt = Okt()
    morphs = okt.pos(sentence)
    transformed_sentence = sentence
    last_index = 0

    for i in range(len(morphs)):
        if morphs[i][1] == 'Noun' and i+1 < len(morphs) and morphs[i+1][1] == 'Noun':
            compound_noun = morphs[i][0] + morphs[i+1][0]
            start_index = transformed_sentence.find(compound_noun, last_index)

            if start_index != -1:
                transformed_sentence = transformed_sentence[:start_index] + morphs[i][0] + " " + morphs[i+1][0] + transformed_sentence[start_index+len(compound_noun):]
                last_index = start_index + len(morphs[i][0]) + 1

    print(transformed_sentence)
    print()

    return transformed_sentence

def process_txt(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        sentences = file.readlines()

    transformed_sentences = [transform_compound_nouns(sentence.strip()) for sentence in sentences]

    with open(output_file_path, 'w', encoding='utf-8') as file:
        for sentence in transformed_sentences:
            file.write(sentence + '\n')

# 텍스트 파일 처리
input_file_path = 'data.txt'  # 입력 텍스트 파일 경로
output_file_path = 'transformed_data.txt'  # 출력 텍스트 파일 경로

process_txt(input_file_path, output_file_path)
