import pandas as pd
from konlpy.tag import Okt

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

def process_csv(input_file_path, output_file_path, column_name):
    df = pd.read_csv(input_file_path)
    df['transformed'] = df[column_name].apply(transform_compound_nouns)
    df.to_csv(output_file_path, index=False)

# CSV 파일 처리
input_file_path = 'data.csv'  # 입력 CSV 파일 경로
output_file_path = 'transformed_data.csv'  # 출력 CSV 파일 경로
column_name = 'question'  # 변형할 컬럼의 이름

process_csv(input_file_path, output_file_path, column_name)
