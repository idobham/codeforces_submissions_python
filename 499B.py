def language_swap(phrase, words):
    first_lang = {}
    for i in range(words):
        first_word, second_word = input().split()
        if len(first_word) > len(second_word):
            first_lang[first_word] = second_word
        else:
            first_lang[first_word] = first_word

    lecture_text = input().split()
    for word in lecture_text:
        print(first_lang[word])

phrase, words = list(map(int, input().split()))
language_swap(phrase, words)


