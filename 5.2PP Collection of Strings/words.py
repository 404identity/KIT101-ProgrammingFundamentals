"""
5.2PP Collection of Strings
"""

__author__ = "Blake Natoli"


def add_word(word_list: list[str], word: str):
    """
    Adds a new word to the word list if there is capacity and
    the word is not empty.
    """
    if word == "":
        print("New word can't be empty!")
        return
    
    if word in word_list:
        print("That is already a word within your word list!")
        return
    
    if word.__contains__(" "):
        print("One word!")
        return
    
    word_list.append(word)


def display_entries(word_list: list[str]):
    """
    Displays all words in the word list, separated by a comma.
    """
    string = ""

    for index, word in enumerate(word_list):
        if index == len(word_list) - 1:
            string += word
        else:
            string += word + ", "
    
    print(string)


def average_len(word_list: list[str]) -> float:
    """
    Returns the average length of all the words in word_list
    """
    total_len = 0

    for word in word_list:
        total_len += len(word)

    return total_len / len(word_list)


def main():
    words: list[str] = []
    choice: str = ""
    new_word: str = ""

    print("Words!")
    while choice != "4":
        print("\n1. Add a word\n2. Display entries\n3. Display average word length\n4. Quit\n")
        choice = input("Action: ")
        match choice:
            case "1":
                new_word = input("New Word: ")
                add_word(words, new_word)
            case "2":
                display_entries(words)
            case "3":
                print(f"Average word length: {average_len(words):.2f}") 
            case "4":
                print("Bye!")
            case _:
                print("Invalid Action")


if __name__ == "__main__":
    main()
