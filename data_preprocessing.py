import pandas as pd
import json

# Function to preprocess text as per the requirements
def preprocess_text(text):
    if not isinstance(text, str):
        return ""
    
    # Replace new line characters with \n
    text = text.replace("\n", "\\n")

    # Replace " with '
    text = text.replace("\"", "'")

    # Remove ^ characters
    text = text.replace("^", "")

    # Remove \ characters, except for \n
    text = text.replace("\\", "")  # First remove all \
    text = text.replace("n", "\\n")  # Then restore \n

    return text

# Revised version of the function to save the output as a JSONL file
def csv_to_jsonl_and_save(file_path, output_path):
    df = pd.read_csv(file_path)

    processed_data = []
    for _, row in df.iterrows():
        processed_question = preprocess_text(row['질문'])
        processed_answer = preprocess_text(row['답변'])
        processed_data.append({"text": processed_question, "answer": processed_answer})

    # Save to JSON Lines file
    with open(output_path, 'w', encoding='utf-8') as f:
        for record in processed_data:
            f.write(json.dumps(record, ensure_ascii=False) + '\n')


# Apply the function to the provided CSV file
file_path = 'test.csv'

# Specify the output path for the JSONL file
output_path = 'processed_data.jsonl'

# Apply the function to save the processed data as a JSONL file
csv_to_jsonl_and_save(file_path, output_path)

# Print the first few lines of the output
print("Saved "+output_path)  # Show a snippet of the jsonl data
