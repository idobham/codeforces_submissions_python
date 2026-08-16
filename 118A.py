raw_words = input()
words = raw_words.lower()
final = ''
for i in words:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'y':
        continue
    else:
        final += '.' + i
print(final)
