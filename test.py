"while循环乘法表"
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={i * j}", end='\t')
        j += 1
    print()
    i += 1

"""
字符串左对齐、右对齐
"""
a = "hello"
print(a.ljust(10, "."))
print(a.rjust(10, "."))
print(a.center(10, "."))
bb = "hello word"
print(bb.startswith("hello"))
print(bb.endswith("word"))
a = lambda: 100
print(a())
list1 = [
    {"name": "abc"},
    {"name": "cd"},
    {"name": "gd"},
    {"name": "hd"}

]

list1.sort(key=lambda x: x["name"],reverse=True)
print(list1)
