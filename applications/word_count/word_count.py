import re

def word_count(s):
    # Your code here
    s = s.lower()
    s = re.sub(r'[":;,.\-+=/\\|[\]{}()*^&]', '', s)
    words = s.split()

    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts        


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))