keys = input("Enter keys: ").split()
values = list(map(int, input("Enter values: ").split()))

d = {}

for i in range(len(keys)):
    d[keys[i]] = values[i]

print("\nDictionary: ", d)

values_list = list(d.values())
values_list.sort()

sorted_dict = {}

for v in values_list:
    for k in d:
        if d[k] == v and k not in sorted_dict:
            sorted_dict[k] = v

print("Sorted dictionary: ", sorted_dict)


keys2 = input("Enter keys for second dictionary: ").split()
values2 = list(map(int, input("Enter values for second dictionary: ").split()))

d2 = {}

for i in range(len(keys2)):
    d2[keys2[i]] = values2[i]

merged = d.copy()
merged.update(d2)

print("Merged dictionary: ", merged)


text = input("\nEnter a word: ")

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Frequency: ", freq)


set1 = set(map(int, input("\nEnter elements of set1: ").split()))
set2 = set(map(int, input("Enter elements of set2: ").split()))

print("Common elements: ", set1.intersection(set2))
print("Unique elements: ", set1.symmetric_difference(set2))