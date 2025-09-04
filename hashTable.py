stock_prices = [("I-Phone", 2200), ("Oppo", 4500), ("Infinix", 2700)]

for item in stock_prices:
    if item[0] == "Infinix":
        print(f"The price of {item[0]} is: {item[1]}")
        break

stock_prices = {"I-phone": 2200, "Oppo": 2500, "Infinix": 2700}

print(f"Price of Infinix is: {stock_prices["Infinix"]}")


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        h = h % self.MAX
        # print(h)
        return h

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                print(element[1])
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                print(f"del {idx}")
                del self.arr[h][idx]
                break

    def print_array(self):
        print(self.arr)


t = HashTable()
# t.setitem("march 9", 40)
# t.getitem("march 9")
# t.setitem("march 10", 29)
# t.delitem("march 9")
# t.print_array()
t["cab"] = 2
t["abc"] = 3
t["abc"]
t["cab"]
t["cab"] = 2200
t["cab"]
t.print_array()
del t["cab"]
t.print_array()
