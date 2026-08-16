first =  input()
second = input()
diff = 0
if first.lower() < second.lower():
    diff = -1
elif first.lower() > second.lower():
    diff = 1
else:
    diff = 0
print(diff)