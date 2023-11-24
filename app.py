import streamlit as st
import nltk
from nltk import word_tokenize
from nltk.util import ngrams

def extract_ngrams(text, n):
    tokens = word_tokenize(text)
    n_grams = ngrams(tokens, n)
    return [' '.join(gram) for gram in n_grams]

def main():
    st.title("N-Gram Extractor")

    text_input = st.text_area("Enter your text here:", "Your default text here.")

    n = st.slider("Select n for n-grams:", 2, 5, 2)

    if st.button("Extract N-Grams"):
        ngrams_result = extract_ngrams(text_input, n)
        st.write(f"{n}-grams: {ngrams_result}")

if __name__ == "__main__":
    nltk.download('punkt')  # Download the tokenizer data
    main()
