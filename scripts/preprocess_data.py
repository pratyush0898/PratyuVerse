import os

def preprocess_text(text):
    # Basic text cleanup: convert to lowercase and remove extra spaces
    text = text.lower().strip()
    return " ".join(text.split())

def preprocess_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = f.read()

    preprocessed_data = preprocess_text(data)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(preprocessed_data)

if __name__ == "__main__":
    input_file = "../data/collected_data.txt"
    output_file = "../data/preprocessed_data.txt"
    preprocess_data(input_file, output_file)
