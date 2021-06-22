# Scored 85
# s = 'a?b?a?b?a?b?a?b?'
# s = 'abbaa?baabb'
# s = 'aa?baab?aa'
# s = 'a?a'
# s = '???a???'
# s = 'a??????'
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
s= input()
s_org = s

def check_palindrome(string):
    for i in range(len(string)):
        try:
            if (string[i] != '?') and (string[i] == string[i + 2]):
                return True # It means that string is a palindrome
        except:
            continue
    return False #It means that string is NOT a palindrome

# def assign_certain_chars(string):
#     for i in range(len(string)):
#         if s[i] == '?':
#             try:
#                 if string[i-2] == 'a':
#                     string = string[:i] + 'b' + string[i+1:]
#                 if string[i-2] == 'b':
#                     string= string[:i] + 'a' + string[i+1:]
#                 if string[i+2] == 'a':
#                     string = string[:i] + 'b' + string[i+1:]
#                 if string[i+2] == 'b':
#                     string = string[:i] + 'a' + string[i+1:]
#             except:
#                 continue
#     return string

# ---------------male avvali---------------
def assign_certain_chars(string):
    for i in range(len(string)):
        if s[i] == '?':
            if i < 2:
                try:
                    if string[i + 2] == 'a':
                        string = string[:i] + 'b' + string[i + 1:]
                    if string[i + 2] == 'b':
                        string = string[:i] + 'a' + string[i + 1:]
                except:
                    continue
            if i >= 2:
                try:
                    if string[i-2] == 'a':
                        string = string[:i] + 'b' + string[i+1:]
                    if string[i-2] == 'b':
                        string= string[:i] + 'a' + string[i+1:]
                    if string[i+2] == 'a':
                        string = string[:i] + 'b' + string[i+1:]
                    if string[i+2] == 'b':
                        string = string[:i] + 'a' + string[i+1:]
                except:
                    continue
    return string

# ------------------------------------------

status = 'undefined'
s = assign_certain_chars(s)
s = assign_certain_chars(s)
# print(s)
palindrome_status = check_palindrome(s)

if palindrome_status == True:
    status = 0

if palindrome_status == False:
    if s.count('?') == 0:
        status = 1

# if palindrome_status == False:
#     for i in range(len(s)):
#         try:
#             if (s[i] == '?') and ((s[i-1] == '?') or (s[i+1] == '?')):
#                 status = 4
#                 break
#         except:
#             continue
#----------------------male avvali--------------------
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
# ---------------------------------------------------

if status == 'undefined':
    status = 2

if s_org.count('?') == 0:
    if palindrome_status == True:
        status = 0
    if palindrome_status == False:
        status = 1

print(int(status % (1e9 + 7)))