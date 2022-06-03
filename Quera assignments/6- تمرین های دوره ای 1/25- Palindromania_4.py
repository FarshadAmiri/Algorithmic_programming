# s = 'a?b?a?b?a?b?a?b?'
# s = 'abbaa?baabb'
# s = 'aa?baab?aa'
# s = 'a?a'
# s = '???a???'
# s = 'a??????'
s = '????????????????????????b'
# s = '???'
# s = 'abaabbaabb'
# s = 'a'
# s = 'aa'
# s = 'aaa'
# s = 'aab'
# s = '?'
# s = '??'
# s = '?a?'
# s = 'a?b?a?bbaa'
# s = '??a'
# s = 'ba???a??'
# s = '???'
# s = 'ab?'
s = '????????a'

# s= input()

# s = s.split()

def change_string_char(string, indice, char):
    string = string[:indice] + char + string[indice + 1:]
    return string


def check_palindrome(string):
    for i in range(len(string)):
        if (string[i] != '?'):
            ii = i + 2
            while ii < len(string):
                if (string[i] == string[ii]):
                    return True  # It means that string contains at least one palindrome subset
                break
    return False  # It means that string does NOT contain any palindrome subset


def fill_string(string):
    characters = ['a','b']
    for id, char in enumerate(string):
        if char != '?':
            char_indeices = []
            while (id + 2) < len(string):
                string = string



blank_locs = []
for i, char in enumerate(s):
    if char == '?':
        blank_locs.append(i)


res = 0
def palindromania(string, index):
    global res
    if string.count('?') == 0:
        if check_palindrome(string) == False:
            return True
    else:
        if palindromania(string[:blank_locs[index]] + 'a' + string[blank_locs[index] + 1:], index + 1):
            res+= 1
        elif palindromania(string[:blank_locs[index]] + 'b' + string[blank_locs[index] + 1:], index + 1):
            res+= 1


if len(blank_locs) == 0:
    if check_palindrome(s) == True:
        print(0)
    else:
        print(1)
else:
    palindromania(s, 0)
    print(res)
