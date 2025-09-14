
def get_num_words(text):
    words = text.split()
    return len(words)

def char_num(text):
    list_of_chars = list(text)
    Char_Dict = {}
    for char in list_of_chars:
        lowchar = char.lower()
        char = lowchar
        if char in Char_Dict:
            Char_Dict[char] += 1
        else:
            Char_Dict[char] = 1
    return Char_Dict
        
def sort_dict(Char_Dict):
    Charcount = []
    sorted_dict = {}
    for ch, count in Char_Dict.items():
        sorted_dict = {"char": ch, "num": count}
        Charcount.append(sorted_dict)
    Charcount = sorted(Charcount, key=lambda x: x["num"], reverse=True)
    return Charcount















  