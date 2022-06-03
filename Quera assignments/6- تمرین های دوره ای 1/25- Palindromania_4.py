# s = 'a?b?a?b?a?b?a?b?'
# s = 'abbaa?baabb'
# s = 'aa?baab?aa'
# s = 'a?a'
# s = '???a???'
# s = 'a??????'
# s = '???????????????????????????????????????????????????????????????????????????????????????????????b'
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
# s = '????????a'
# s = 'ba??????????'
# s= input()


def change_string_char(string, indice, char):
    string = string[:indice] + char + string[indice + 1:]
    return string


def complete_string(string):
    for id, char in enumerate(string):
        if char != '?':
            id2 = id + 4
            while (id2) < len(string):
                if string[id2] == '?':
                    string = change_string_char(string, id2 ,char)
                id2 += 4

            id2 = id - 4
            while (id2) >= 0:
                if string[id2] == '?':
                    string = change_string_char(string, id2 ,char)
                id2 -= 4
# ----------------------------------------------------------------
            other_char = 'b' if char == 'a' else 'a'

            id3 = id + 2
            while (id3) < len(string):
                if string[id3] == '?':
                    string = change_string_char(string, id3, other_char)
                id3 += 4

            id3 = id - 2
            while (id3) >= 0:
                if string[id3] == '?':
                    string = change_string_char(string, id3, other_char)
                id3 -= 4
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


s = complete_string(s)
# print('completed string is ', s)

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

    elif complete_string(string).count('?') == 0:
        if check_palindrome(string) == False:
            res += 1
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
