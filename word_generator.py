import random
import string

def generate_unique_words(num_words):
    words = set()

    while len(words) < num_words:
        word_length = random.randint(3, 10)
        new_word = ''.join(random.choice(string.ascii_lowercase) for _ in range(word_length))
        words.add(new_word)

    return words

def write_words_to_file(words, filename):
    with open(filename, 'w') as file:
        for word in words:
            file.write(word + '\n')

if __name__ == "__main__":
    num_unique_words = 72875
    generated_words = generate_unique_words(num_unique_words)

    # Use the provided path for 'words.txt'
    file_path = r'C:\\Users\\user\\Desktop\\programming assignments\\SpellChecker\\words.txt'

    write_words_to_file(generated_words, file_path)
    print(f"{num_unique_words} unique words generated and written to '{file_path}'.")
