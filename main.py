
def main():
    path = "books/frankenstein.txt"
    text = read_file(path)
    amount_of_words = count_words(text)
    charcter_dictionary = character_dict(text)
    #print(charcter_dictionary)
    #make_report(charcter_dictionary)
    make_report(charcter_dictionary, amount_of_words)

def read_file(path):
    with open(path) as file:
        text = file.read()
        return text


def count_words(text):
    words = text.split()
    return len(words)

def character_dict(text):
    character_dict = {}
    lower_txt = text.lower()
    for char in lower_txt:
        character_dict[char] = character_dict.get(char, 0) + 1
    return character_dict

def sort_on(dict):
    return dict["num"]

def make_report(dict, word_count):
    dict_as_list = []
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                'o','p','q','r','s','t','u','v','w','x','y','z']
    counter = 0
    for key in dict:
        if key in alphabet:
            dict_as_list.append({"char": key, "num": dict[key]})
    dict_as_list.sort(reverse=True, key= sort_on)
    print(f"*** Begin report of frankenstein.txt ***\n{word_count} words were found in the document\n")
    for dict in dict_as_list:
        char = dict['char']
        number = dict['num']
        print(f"The {char} character was found {number} times")
    print("\n*** Finale my friends ***")

# Where this program runs
main()