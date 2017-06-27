"""key value store"""
import sys
kv_store = {}
answering = True

while (answering):
    user_answer = input('get, insert, delete, update, or quit? ')
    if user_answer == 'insert':
        key = input('key = ')
        value = input('value = ')
        kv_store[key] = value
    elif user_answer == 'get':
        keys = {k for k in kv_store}
        if len(keys) != 0: 
            print(keys)
            user_answer = input('what value to get? ')
            if user_answer not in kv_store:
                print("key doesn't exist")
            else:
                temp = kv_store[user_answer]
                print('{{{}: {}}}'.format(user_answer, temp))
        else:
            print('nothing to get')
    elif user_answer == 'update':
        if len(kv_store) != 0:
            print(keys)
            user_answer = input('what to update? ')
            value = input('what to update to? ')
            kv_store[user_answer] = value
        else:
            print('nothing to update')
    elif user_answer == 'delete':
        if len(kv_store) != 0:
            print(kv_store)
            user_answer = input('what to delete? ')
            if user_answer not in kv_store:
                print("key doesn't exist")
            else:
                del kv_store[user_answer]
        else:
            print('nothing to delete')
    elif user_answer == 'quit':
        print('goodbye')
        sys.exit()

            




