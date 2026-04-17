def remove_duplicates(data_list):
    data_set = set(data_list)
    data_set.discard("")
    data_set.discard(",")
    return list(data_set)

def strip_whitespaces(string_list):
    newList = []
    for x in string_list:
        newList.append(x.strip())
    return newList

