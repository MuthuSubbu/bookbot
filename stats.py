def get_num_words(text):
    words = text.split()
    return len(words)

def get_characters(word):
    d = {}
    w = word.lower()
    for i in w:
        if i in d:
            d[i] +=1
        else:
            d[i] = 1
    return d

# def report(d):
#     final_dict = []
#     alpha_list = []
#     sorted_dict = sorted(d.items(), key=lambda item: item[1], reverse = True)
#     for key,value in sorted_dict:
#         final_dict.append({"char": key, "num": value})
#     for j in final_dict:
#         if j["char"].isalpha():
#             alpha_list.append(j)
#     return alpha_list
def sort_on(dict):
    return dict["num"]
def report(d):
    sorted_list = []
    for i in d:
        sorted_list.append({"char": i, "num": d[i]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
