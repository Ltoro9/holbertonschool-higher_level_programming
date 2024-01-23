#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    my_list = dir(hidden_4)
    max_len = len(my_list)
    for i in range(0, max_len):
        string = my_list[_]
        if string[:2] != "__" != string[-2:]:
            print(string)
