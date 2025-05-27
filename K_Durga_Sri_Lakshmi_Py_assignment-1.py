inv = [
    ["Strawberry", "Fruit", 3.50, 40, 10],
    ["Broccoli", "Vegetable", 2.20, 25, 8],
    ["Cheddar", "Dairy", 5.00, 18, 4],
    ["Baguette", "Bakery", 2.80, 35, 2],
    ["Blueberry", "Fruit", 4.00, 22, 6],
    ["Spinach", "Vegetable", 1.80, 30, 12],
    ["Yogurt", "Dairy", 1.20, 50, 15],
    ["Croissant", "Bakery",3.00,28,3]]
s = 0
for i in inv:
    s += i[2]*i[3]
    if i[4] < 5:
        print(i[0])
print(s)
s1 = set()
for i in inv:
    s1.add(i[1])

cat = dict()
for j in s1:
    cat[j] = 0

#print(cat)

for i in inv:
    cat[i[1]] += i[2]*i[3]
print(cat)



