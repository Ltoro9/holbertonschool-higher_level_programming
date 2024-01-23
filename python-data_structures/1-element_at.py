#!/usr/bin/python3
def element_at(my_list, idx):
    argc = len(my_list)
    if idx < 0 or idx >= argc:
        return None
    else:
        return f"{my_list[idx]}"
