from konlpy.tag import Okt

def transform_compound_nouns(sentence):
    okt = Okt()
    morphs = okt.pos(sentence)
    transformed_sentence = sentence
    last_index = 0

    for i in range(len(morphs)):
        if morphs[i][1] == 'Noun' and i+1 < len(morphs) and morphs[i+1][1] == 'Noun':
            # 연속된 명사 찾기
            compound_noun = morphs[i][0] + morphs[i+1][0]
            start_index = transformed_sentence.find(compound_noun, last_index)

            if start_index != -1:
                # 복합 명사를 공백으로 분리하여 재구성
                transformed_sentence = transformed_sentence[:start_index] + morphs[i][0] + " " + morphs[i+1][0] + transformed_sentence[start_index+len(compound_noun):]
                last_index = start_index + len(morphs[i][0]) + 1  # 공백을 추가했으므로 인덱스 조정

    return transformed_sentence

# 예시 문장
sentence = "치킨버섯치즈 + 한우곰탕숙주된장덮밥소스의 표시광고 사전 심의필은 어떻게 되나요?"
transformed = transform_compound_nouns(sentence)
print("변형된 문장:", transformed)
