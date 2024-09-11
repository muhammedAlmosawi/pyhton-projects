import pandas as pd
import re
import nltk
from nltk.translate import AlignedSent, IBMModel1


def clean_sentences(sentences):
    cleaned_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()
        sentence = sentence.lower()
        sentence = re.sub(r"^a-zA-Z0-9", " ", sentence)
        cleaned_sentences.append(sentence.strip())
    return cleaned_sentences

def train_translation_model(source_sentence, target_sentence):
    aligned_sentences = [AlignedSent(source.split(), target.split()) for source, target in zip(source_sentence, target_sentence)]
    ibm_model = IBMModel1(aligned_sentences, 10)
    return ibm_model

def translate_input(ibm_model):
    while True:
        input_source = input("enter the english sentence (press 'q' to quit): ")
        if input_source == "q":
            print("Quitting.........")
            break
        clean_text = clean_sentences(input_source.split())
        source_words = clean_text
        translated_words = []
        for source_word in source_words:
            max_probability = 0.0
            translated_word = None
            for target_word in ibm_model.translation_table[source_word]:
                probability = ibm_model.translation_table[source_word][target_word]
                if probability > max_probability:
                    max_probability = probability
                    translated_word = target_word
            if translated_word is not None:
                translated_words.append(translated_word)
        translated_text = " ".join(translated_words)
        print(f"Translated text: {translated_text}")
        print("----------------------------------")

data_frame = pd.read_csv(r"D:\my-github-draft\pandas\engspn.csv")
english_sentences = data_frame["english"].tolist()
spanish_sentences = data_frame["spanish"].tolist()

cleaned_english_sentence = clean_sentences(english_sentences)
cleaned_spanish_sentence = clean_sentences(spanish_sentences)

ibm_model = translation_model = train_translation_model(cleaned_english_sentence, cleaned_spanish_sentence)

translate_input(ibm_model)