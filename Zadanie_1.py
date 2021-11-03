#/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    a = list(map(int, input().split()))
    s = 0
    for item in a:
        if item>3 and item<8:
            s += item

    print(s)


