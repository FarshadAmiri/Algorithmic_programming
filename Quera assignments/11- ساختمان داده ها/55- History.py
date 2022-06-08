q = int(input())
history = []
string = ''

def insert_it(char, loc):
    global history, string

    string = string[ : loc - 1] + char + string[loc - 1 : ]
    history.append(string)


def delete_it(loc):
    global history, string

    string = string[ : loc - 1] + string[loc : ]
    history.append(string)


def undo_it():
    global history, string

    history.pop()
    string = history[-1]


def do_query(query):
    query_entities = query.split()
    query_type = query_entities[0]
    if len(query_entities) == 1:
        q_loc = query_entities[1]
    elif len(query_entities) == 2:
        q_what = query_entities[2]

    if query_type == 'undo':
        undo_it()
    else:
        q_loc = int(query.split()[1])
        q_what = query.split()[2]
        if query_type == 'insert':
            insert_it(q_what, q_loc)
        elif query_type == 'delete':
            delete_it(q_loc)



for i in range(q):
    query = input()
    do_query(query)

print(string)