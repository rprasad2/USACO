with open("blocks.in") as f:
    lines = [line.strip() for line in f.readlines()]

words = []
for i in range(1, int(lines[0]) + 1):
    words_arr = lines[i].split()
    words.append((words_arr[0], words_arr[1]))

num_letter = {
}

for code in range(ord('a'), ord('z') + 1):
    num_letter[chr(code)] = 0

def count_letters(word):
    ind_letter = {} # letter frequency
    for letter in word:
        ind_letter[letter] = ind_letter[letter] + 1 if letter in ind_letter else 1

    return ind_letter

for word_pair in words:
    letters1 = count_letters(word_pair[0])
    letters2 = count_letters(word_pair[1])

    for shared_letter in set(word_pair[0]).union(set(word_pair[1])):
        if shared_letter in letters1 and shared_letter in letters2:
            num_letter[shared_letter] = max(letters1[shared_letter], letters2[shared_letter])
        elif shared_letter in letters1:
            num_letter[shared_letter] += letters1[shared_letter]
        else:
            num_letter[shared_letter] += letters2[shared_letter]

with open("blocks.out", 'w') as f:
    for code in range(ord('a'), ord('z') + 1):
        f.write(str(num_letter[chr(code)]) + '\n')
