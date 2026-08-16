chat_message = input()
pos = chat_message.find('h')
if pos != -1:
    pos = chat_message.find('e', pos + 1)
if pos != -1:
    pos = chat_message.find('l', pos + 1)
if pos != -1:
    pos = chat_message.find('l', pos + 1)
if pos != -1:
    pos = chat_message.find('o', pos + 1)

##print(chat_message)
if pos != -1:
    print("YES")
else:
    print("NO")