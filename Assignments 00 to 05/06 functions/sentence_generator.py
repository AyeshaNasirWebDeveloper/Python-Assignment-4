def create_sentence(word, word_type):
    if word_type == 0:
        print("I am excited to add this", word, "to my vast collection of them!")
    elif word_type == 1:
        print("It's so nice outside today it makes me want to", word + "!")
    elif word_type == 2:
        print("Looking out my window, the sky is big and", word + "!")
    else:
        print("Oops! Please enter 0 for noun, 1 for verb, or 2 for adjective.")

def main():
    user_word = input("Please type a noun, verb, or adjective: ")
    print("Is this a noun, verb, or adjective?")
    word_choice = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    create_sentence(user_word, word_choice)

if __name__ == '__main__':
    main()
