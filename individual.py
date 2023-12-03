#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# вариант-11


def sum_after_positive(*a):
    if not a:
        return None
    flag = False
    count = 0
    for i in a:
        if flag:
            count += i
        elif i >= 0:
            flag = True
    return count


if __name__ == "__main__":
    print(sum_after_positive(-10, -9, 1, 2, 4, 5))
