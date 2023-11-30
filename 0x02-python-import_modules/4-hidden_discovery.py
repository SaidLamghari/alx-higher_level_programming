#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    names = dir(hidden_4)
    count = 0
    while count < len(names):
        name = names[count]
        if not name.startswith('__'):
            print(name)
        count += 1
