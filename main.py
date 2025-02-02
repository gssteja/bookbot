def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = get_word_count(text)
    dict = get_char_count(text)
    list = print_alphabet(dict)
    list.sort(reverse=True, key=sort_on)

    print(f'--- Begin report of {path} ---')
    print(f'{word_count} words found in the document')
    print('')
    for item in list:
        print(f'The \'{item["alphabet"]}\' character was found {item["count"]} times')
    print(f'--- End Report ---')


def sort_on(dict):
    return dict["count"]

def print_alphabet(dict):
    alphabets = list_alphabets(dict)
    return count_chars(dict,alphabets)
    

def count_chars(dict,alphabets):
    list = []
    for alphabet in alphabets:
        dictionary = {}
        if alphabet in dict:
            dictionary["alphabet"]=alphabet
            dictionary["count"]=dict[alphabet]
        list.append(dictionary)
    return list
    

def list_alphabets(dict):
    list = []
    for i in dict:
        if i.isalpha():
            list.append(i)
    return list

def get_char_count(text):
    dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def get_word_count(text):
    words = text.split()
    return len(words)
44
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()