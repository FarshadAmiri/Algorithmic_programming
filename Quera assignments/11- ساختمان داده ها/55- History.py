q = int(input())
history = ['']

def insert_it(query):
    global history

    string = history[-1]
    loc = int(query.split()[1])
    char = query.split()[2]

    string = string[ : loc - 1] + char + string[loc - 1 : ]
    history.append(string)


def delete_it(query):
    global history

    string = history[-1]
    loc = int(query.split()[1])
    string = string[ : loc - 1] + string[loc : ]
    history.append(string)


def undo_it():
    global history

    history.pop()


def do_query(query):
    query_type = query.split()[0]

    if query_type == 'undo':
        undo_it()
    elif query_type == 'insert':
        insert_it(query)
    elif query_type == 'delete':
        delete_it(query)


for i in range(q):
    query = input()
    do_query(query)

print(history[-1])