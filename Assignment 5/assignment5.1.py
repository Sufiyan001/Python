while True:
    input_word= input("Please enter two words: ").strip()

    if not input_word:
        break
    elif input_word.lower() == "done":
        break

    word = input_word.split()
    
    if len(word) == 2:
        word1, word2 = word
        if word1 < word2:
            print(f"{word1} comes first")
        else:
            print(f"{word2} comes first")
    elif len(word) == 1:
        print("Please enter two words separated by a space.")
    else:
        print("Invalid input. Please enter two words separated by a space.")
print("--bye!!")