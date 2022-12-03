items = {
    "milk": 2.6,
    "bread": 1.4,
    "egg": 5
}

lst = ["milk", "bread", "Egg"]
total = 0

for ele in lst:
    print(ele, items[ele])
    total += items[ele]
    
print('-'*8)
print('Total:', total)
print('-'*8)
