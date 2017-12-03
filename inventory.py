stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def print_inventory():
    print('Item          amount')
    for k, v in stuff.items():
        print(k.ljust(14, '.') + str(v))

def add_stuff(key, add_value):
    if key not in stuff:
        stuff.setdefault(key, add_value)
        print("new item")
    else:
        print(key+"origin num:" + str(stuff[key]) + ", after add:" + str(stuff[key]+add_value))
        stuff[key] += add_value

print_inventory()