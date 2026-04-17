

def calculate_mean(num_list):
    total = 0
    for x in num_list:
        total += int(x)
    return total/len(num_list)

def find_maximum(num_list):
    int_list = []
    for x in num_list:
        int_list.append(int(x))

    maximum = int_list[0]
    for y in int_list:
        if(y > maximum):
            maximum = y
    return maximum

def find_minimum(num_list):
    int_list = []
    for x in num_list:
        int_list.append(int(x))

    minimum = int_list[0]
    for y in int_list:
        if (y < minimum):
            minimum = y
    return minimum



