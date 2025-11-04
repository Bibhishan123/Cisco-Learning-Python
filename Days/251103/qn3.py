sentence = input("Enter a sentence: ")

words_list = sentence.split()
upper_words = []

for word in words_list:
    upper_words.append(word.upper)

words_tuple=tuple(upper_words)

with open('sentence_data.txt', 'w') as out_file:
    out_file.write(f'List: {words_list}\n')
    out_file.write(f'Tuple: {words_tuple}\n')

with open('sentence_data.txt', 'r') as in_file:
    line1 = in_file.readline()
    line2 = in_file.readline()   
    print(line1, end='')
    print(line2, end='')
   