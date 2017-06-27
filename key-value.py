"""docstinrg"""
kv_store = {}
answering = True

while (answering):
    user_answer = input('get, insert, delete? ')
    if user_answer == 'insert':
        key = input('> ')
        value = input('> ')
        kv_store[key] = value
    elif user_answer == 'get':
        print('\n')
        for key in kv_store:
            print(key,)
        user_answer = input('what value to get? ')
        try:
            temp = kv_store[user_answer]
            print('{{{}: {}}}'.format(user_answer, temp))
        except Exception as e:
            print(e)
    else:
        user_answer = input('What do delete? ')
        del kv_store[user_answer]
            




