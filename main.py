from stats import convert_to_dict_list, get_num_chars, get_num_words
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    # book_name = "frankenstein"
    # path = f"./books/{book_name}.txt"
    args = sys.argv
    if not len(args) > 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = args[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    obj = get_num_chars(text)
    list_of_obj = convert_to_dict_list(obj)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words") 
    print("--------- Character Count -------")  
    for obj in list_of_obj:
        if obj["char"].isalpha():
            print(f"{obj["char"]}: {obj["num"]}")
    print("============= END ===============")
    # print(f"{num_words} words found in the document")
    # print(obj)

main()