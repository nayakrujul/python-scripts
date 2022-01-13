import string
import arrow
from typing import *


class Sort:

    def __init__(self,
                 sort_lst: Iterable,
                 scale=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation,
                 last=sorted):
        self.sort_lst = list(sort_lst)
        self.scale = list(scale)
        self.last = last

    def __str__(self):
        return 'Sort object: "' + str(self.sort()) + '" at ' + arrow.now().format('YYYYMMDDTHHmmss')

    def __repr__(self):
        return self.sort()

    def sort(self) -> list:
        sorted_lst = []
        for item in self.sort_lst:
            if not len(sorted_lst):
                sorted_lst.insert(0, item)
            else:
                for thing in sorted_lst:
                    least_len = len(thing) if len(thing) < len(item) else len(item)
                    for index in range(least_len):
                        if self.compare_char(item[index], thing[index]) == 0:
                            sorted_lst.insert(sorted_lst.index(thing), item)
                            break
                        elif self.compare_char(item[index], thing[index]) == 1:
                            break
                    if sorted_lst.count(item) == self.sort_lst.count(item):
                        break
                else:
                    sorted_lst.append(item)
        return sorted_lst

    def compare_char(self, x: str, y: str) -> int(0 or 1 or 2):
        if x in self.scale and y in self.scale:
            if self.scale.index(x) < self.scale.index(y):
                return 0
            elif self.scale.index(x) > self.scale.index(y):
                return 1
            else:
                return 2
        elif x in self.scale and (not (y in self.scale)):
            return 0
        elif y in self.scale and (not (x in self.scale)):
            return 1
        else:
            return self.last(x + y)[0]


sort = Sort("let's sort this sentence in alphabetical order.".split())
print(' '.join(repr(sort)))
