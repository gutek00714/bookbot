#count number of words in text
def count_words(text):
    all_words = text.split()
    number_of_words = len(all_words)
    return number_of_words


#count number of each symbol in text
def count_symbols(full_text):
    all_symbols_count = {}
    full_text = full_text.lower()
    for item in full_text:
        if item in all_symbols_count:
            all_symbols_count[item] += 1
        else:
            all_symbols_count[item] = 1
    return all_symbols_count


def sort_on(items):
    return items["num"]

#get a dict from count_symbols, remake it into a list of dicts and sort
def raport(char_counts):
    counted_list = []
    for char, num in char_counts.items():
        new_dict = {"char": char, "num": num}
        counted_list.append(new_dict)
    
    counted_list.sort(reverse=True, key=sort_on)
    return counted_list