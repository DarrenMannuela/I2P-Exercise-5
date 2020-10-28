def word_frequencies(my_list):
    my_list = my_list.split()
    word_counter = {}

    for count in my_list:
        if count in word_counter:
            word_counter[count] += 1
        else:
            word_counter[count] = 1
    return word_counter


if __name__ == "__main__":
    words = input("Give me a sentence:")
    print(word_frequencies(words))
