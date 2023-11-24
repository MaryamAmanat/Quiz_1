# app.py

import streamlit as st
from nltk import ngrams
from nltk.tokenize import word_tokenize

# Function to generate n-grams
def generate_ngrams(text, n):
    tokens = word_tokenize(text)
    n_grams = list(ngrams(tokens, n))
    return [' '.join(gram) for gram in n_grams]

# Streamlit web interface
def main():
    st.title("N-gram Generator")

    # User input
    text_input = st.text_area("Enter text:", "")

    # Select n-gram type
    n_gram_type = st.selectbox("Select n-gram type:", ["Bigram", "Trigram", "Custom"])

    if n_gram_type == "Bigram":
        n = 2
    elif n_gram_type == "Trigram":
        n = 3
    else:
        n = st.number_input("Enter the value of n:", min_value=1, step=1)

    # Generate n-grams
    if st.button("Generate N-grams"):
        if text_input:
            ngrams_result = generate_ngrams(text_input, n)
            st.write(f"{n}-grams:", ngrams_result)
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
