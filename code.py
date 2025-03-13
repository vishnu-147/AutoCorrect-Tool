from collections import deque

dictionary = [
    'apple', 'banana', 'orange', 'pear', 'grape', 'pineapple',
    'blueberry', 'strawberry', 'watermelon', 'kiwi', 'mango', 'papaya',
    'apricot', 'cherry', 'fig', 'lemon', 'lime', 'plum', 'raspberry',
    'blackberry', 'coconut', 'nectarine', 'peach', 'persimmon', 'tangerine',
    'cranberry', 'guava', 'lychee', 'melon', 'passionfruit', 'love'
]

def bfs_spell_check(word):
    queue = deque([word])
    visited = set()
    corrections = []

    while queue and len(corrections) < 3:
        current_word = queue.popleft()
        if current_word in visited:
            continue

        visited.add(current_word)

        if current_word in dictionary:
            corrections.append(current_word)

        # Generating all possible edits within an edit distance of 1
        for i in range(len(current_word)):
            for j in range(97, 123):  # ASCII for lowercase alphabets
                new_word = current_word[:i] + chr(j) + current_word[i+1:]
                if new_word not in visited:
                    queue.append(new_word)

    return corrections

def autocorrect(sentence):
    corrected_sentence = []
    spell_check_info = {}

    words = sentence.split()

    for word in words:
        if len(word) > 1 and word.lower() not in dictionary:
            suggestions = bfs_spell_check(word.lower())
            spell_check_info[word] = suggestions
            if suggestions:
                # Take the first suggestion for simplicity
                corrected_sentence.append(suggestions[0])
            else:
                # If no suggestions found, keep the original word
                corrected_sentence.append(word)
        else:
            corrected_sentence.append(word)

    return ' '.join(corrected_sentence), spell_check_info

# Example usage
input_sentence = input("Enter a sentence: ")
corrected_output, spell_check_info = autocorrect(input_sentence)

print("\nInput:", input_sentence)
print("Spell checking each word:")
for word, suggestions in spell_check_info.items():
    print(f"{word}: {suggestions if suggestions else ['No suggestions']}")

print("Corrected:", corrected_output)
