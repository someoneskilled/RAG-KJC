import difflib
import os
from groq import Groq

os.environ["GROQ_API_KEY"] = "API_KEY_HERE"

client = Groq()

MAX_INPUT_TOKENS = 4000  # Max input tokens allowed
TOKEN_RATIO = 0.75  # Approximate words per token


def chunk_text(text, chunk_size=500):
    words = text.split()
    return [" ".join(words[i : i + chunk_size]) for i in range(0, len(words), chunk_size)]


def load_college_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Loading data and create text chunks
college_text = load_college_data("test.txt")
chunks = chunk_text(college_text)


def find_best_matching_chunk(query):
    best_match = max(chunks, key=lambda chunk: difflib.SequenceMatcher(None, query, chunk).ratio())
    max_words = int(MAX_INPUT_TOKENS * TOKEN_RATIO)  # Enforce token limit
    return " ".join(best_match.split()[:max_words])


def query_college_bot(question):
    relevant_text = find_best_matching_chunk(question)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": relevant_text},
            {"role": "user", "content": question},
        ],
        temperature=0.5,
        top_p=1,
        stream=False,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    
    while True:
        user_input = input("Ask me about the college: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        print("\nBot:", query_college_bot(user_input))