#---------q5.8------------------
'''
Q8
Yek chatbote sade benevisid, ke baid aval bege salam, har dafe user chizi benevise , 
in kheyli sade benevise '[Javabe chatbot]' va in karo oonghdr edame bede, 
zamani ke user neevshte 'bye' in chatbot goftego ro tamom kone va bege 'good bye'
'''

print("=================Q8=======================")
print("==========================================")

print("salam")

while True:
    user = input("user: ")

    if user == "bye":
        print("good bye")
        break

    print("[Javabe chatbot]")