d = {}# creates empty dict


marks = {
    "Harry" : 100,
    "Impana" : 83,
    "Akash" :98
}

# print(marks.items())

# print(marks.values())
# print(marks.keys())
# marks.update({"Impana": 88, "Ram": 100})

print(marks.get("Harry"))# prints None
print(marks["Harry"])# returns keyerror
print(marks)

