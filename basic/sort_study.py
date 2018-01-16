def compare_second_ele(l):
    return l[1]


def compare_num_of_chars(string1):
    return len(string1)


def remove_if_exist(value, l):
    if value in l:
        l.remove(value)


def remove_if_exist_more_than_once(value, l):
    if value in l and l.count(value)-1:
        l.remove(value)
