#/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = list(map(int, input().split()))
    s = 0
    b = list(filter(lambda x: x>3 and x<8, a))
    print(sum(b))


