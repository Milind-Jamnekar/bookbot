def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    array = []
    for item in text:
        array.append(item.lower())
    obj = {}
    for item in array:
        if item in obj:
            obj[item] += 1
        else:
            obj[item] = 1
    return obj

def sort_on(items):
    return items["num"]

def convert_to_dict_list(d:dict[str,int]):
    arr_of_dict = []
    for key ,value in d.items():
        arr_of_dict.append({"char":key,"num":value})
    
    arr_of_dict.sort(reverse=True,key=sort_on)
    return arr_of_dict