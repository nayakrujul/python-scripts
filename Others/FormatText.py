from string import ascii_letters, digits
import re

class Colours:
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"

def remove_all(s, l):
    for x in l:
        s = s.replace(x, '')
    return s
    
def compare(x, y, c):
    x += '`' * (len(y) - len(x))
    r = ''
    i = 0
    for j in range(len(y)):
        if x[j-i] != y[j]:
            i += 1
            r += Colours.END + y[j]
        else:
            r += c + x[j-i]
    return r

def isvar(x):
    try:
        while x[0] in '[](){}':
            x = x[1:]
    except:
        pass
    for c in x:
        if c not in (ascii_letters + '_'):
            return False
    return True

class FormatText:
    def __init__(self, line):
        self.line = line
        self.formatted = self.format()
    def __str__(self):
        return self.formatted
    def format(self):
        string, strstart = False, None
        last_char = ''
        ret = ''
        for char in self.line:
            ending = False
            if not string and char in '"\'':
                ret += Colours.YELLOW
                string, strstart = True, char
            elif string and char == strstart:
                string = False
                ending = True
            elif (not string) and ((char in digits) or ((char == '.') and (last_char in digits))):
                if last_char not in (ascii_letters + '_'):
                    ret += Colours.GREEN
            elif not string:
                ret += Colours.END
            ret += char
            if ending:
                ret += Colours.END
            last_char = char
        keywords = [
            'False', 'None', 'True', 'and', 'as',
            'assert', 'async', 'await', 'break', 'class',
            'continue', 'def', 'del', 'elif', 'else',
            'except', 'finally', 'for', 'from', 'global',
            'if', 'import', 'in', 'is', 'lambda',
            'nonlocal', 'not', 'or', 'pass', 'raise',
            'return', 'try', 'while', 'with', 'yield'
        ]
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        new_ret = []
        for word in ret.split():
            append = ''
            result = ansi_escape.sub('', word)
            if remove_all(result, '(){}[],') in keywords:
                append += compare(remove_all(result, '(){}[],'), result, Colours.LIGHT_BLUE)
            elif '(' in word and isvar(result.split('(')[0]):
                append += compare(remove_all(result.split('(')[0], '[]{}'), result.split('(')[0], Colours.PURPLE) + Colours.END + '(' + '('.join(word.split('(')[1:])
            else:
                append += word
            new_ret.append(append + Colours.END)
        return ' '.join(new_ret)

print(FormatText('[print(x) for x in [1, 2.3, "abc", False]]'))