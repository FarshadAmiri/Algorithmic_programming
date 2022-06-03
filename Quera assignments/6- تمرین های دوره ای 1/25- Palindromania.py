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

# s= input()
s_org = s
# def check_palindrome(string):
#     for i in range(len(string)):
#         try:
#             if (string[i] != '?') and (string[i] == string[i + 2]):
#                 return True # It means that string is a palindrome
#         except:
#             continue
#     return False #It means that string is NOT a palindrome

def check_palindrome2(string):
    for i in range(len(string)):
        if (string[i] != '?'):
            ii = i + 2
            while (ii>=0) and (ii<len(string)):
                if (string[i] == string[ii]):
                    return True # It means that string is a palindrome
                ii = ii + 4

    for i in range(len(string)):
        if (string[i] != '?'):
            ii = i + 4
            while (ii>=0) and (ii<len(string)):
                if string[ii] != '?':
                    if (string[i] != string[ii]):
                        return True # It means that string is a palindrome
                ii = ii + 4
    return False #It means that string is NOT a palindrome

# def assign_certain_chars(string):
#     for i in range(len(string)):
#         if s[i] == '?':
#             if i < 2:
#                 try:
#                     if string[i + 2] == 'a':
#                         string = string[:i] + 'b' + string[i + 1:]
#                     if string[i + 2] == 'b':
#                         string = string[:i] + 'a' + string[i + 1:]
#                 except:
#                     continue
#             if i >= 2:
#                 try:
#                     if string[i-2] == 'a':
#                         string = string[:i] + 'b' + string[i+1:]
#                     if string[i-2] == 'b':
#                         string= string[:i] + 'a' + string[i+1:]
#                     if string[i+2] == 'a':
#                         string = string[:i] + 'b' + string[i+1:]
#                     if string[i+2] == 'b':
#                         string = string[:i] + 'a' + string[i+1:]
#                 except:
#                     continue
#     return string


def assign_certain_chars3(st):
    a_list = []
    b_list = []
    for i in range(len(st)):
        if st[i] == 'a':
            a_list.append(i)
        if st[i] == 'b':
            b_list.append(i)
    for i in a_list:
        ip4 = i
        while (ip4 >= 0) and (ip4 < len(st)):
            if ip4 not in a_list:
                a_list.append(ip4)
            ip4 = ip4 + 4
        in4 = i
        while (in4 >= 0) and (in4 < len(st)):
            if in4 not in a_list:
                a_list.append(in4)
            else:
                in4 = in4 - 4
        ip2 = i + 2
        while (ip2 >= 0) and (ip2 < len(st)):
            if ip2 not in b_list:
                b_list.append(ip2)
            ip2 = ip2 + 4
        in2 = i - 2
        while (in2 >= 0) and (in2 < len(st)):
            if in2 not in b_list:
                b_list.append(in2)
            else:
                in2 = in2 - 4
    for i in b_list:
        ip4 = i
        while (ip4 >= 0) and (ip4 < len(st)):
            if ip4 not in b_list:
                b_list.append(ip4)
            ip4 = ip4 + 4
        in4 = i
        while (in4 >= 0) and (in4 < len(st)):
            if in4 not in b_list:
                b_list.append(in4)
            else:
                in4 = in4 - 4
        ip2 = i + 2
        while (ip2 >= 0) and (ip2 < len(st)):
            if ip2 not in a_list:
                a_list.append(ip2)
            ip2 = ip2 + 4
        in2 = i - 2
        while (in2 >= 0) and (in2 < len(st)):
            if in2 not in a_list:
                a_list.append(in2)
            else:
                in2 = in2 - 4
    for i in a_list:
        if st[i] != 'a':
            try:
                st = st[:i] + 'a' + st[i+1:]
            except:
                continue
    for i in b_list:
        if st[i] != 'b':
            try:
                st = st[:i] + 'b' + st[i+1:]
            except:
                continue
    return st


status = 'undefined'

palindrome_status = check_palindrome(s)
if palindrome_status == True:
    status = 0

s = assign_certain_chars3(s)
# for i in range(len(s_org)):
#     s = assign_certain_chars(s)


print(s)
print(palindrome_status)


if palindrome_status == False:
    if s.count('?') == 0:
        status = 1

if palindrome_status == False:
    for i in range(len(s)):
        if i == 0:
            try:
                if (s[i] == '?') and (s[i + 1] == '?'):
                    status = 4
                    break
            except:
                continue
        if i > 0:
            try:
                if (s[i] == '?') and ((s[i-1] == '?') or (s[i+1] == '?')):
                    status = 4
                    break
            except:
                continue

if status == 'undefined':
    status = 2

if s_org.count('?') == 0:
    if palindrome_status == True:
        status = 0
    if palindrome_status == False:
        status = 1

if s_org == '?':
    status = 2

print(int(status % (1e9 + 7)))