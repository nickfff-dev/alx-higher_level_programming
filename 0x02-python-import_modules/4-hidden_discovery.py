#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    folders = dir(hidden_4)
    for folder in folders:
        if folder[0] != '_':
            print('{}'.format(folder))
