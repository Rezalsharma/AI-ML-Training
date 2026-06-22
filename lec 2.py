# s=input("Enter a string: ")
# dict={}
# for i in s:
#     if i in dict.keys():
#         dict[i]=dict[i]+1
#     else:
#         dict[i]=1
# print(dict)



# str=input("Enter a string: ")
# s=str.split()
# dict={}
# for i in s:
#     if i in s:
#         dict[i]=dict.get(i,0)+1
# print(dict)



# l=["ramanpreet","rezal","muskan","devagya"]
# dict={}
# for i in l:
#     c=i.lower()[0]
#     if c not in dict.keys():
#         dict[c]=[i]
#     else:
#         dict[c]=dict[c]+[i]
# print(dict)



# str=["ramanpreet","shiavam","muskan","devagya"]
# dict={}
# for i in str:
#     l=len(i)
#     if l not in dict.keys():
#         dict[l]=[i]
#     else:
#         dict[l]=dict[l]+[i]
# print(dict)



# msg=input("Enter a message: ")
# emotions={"happy":"\U0001F601","laughing":"\U0001F602","angry":"\U0001F621"}
# opt=""
# s=msg.split()
# for i in s:
#     if i in emotions.keys():
#         opt=opt+emotions[i]+" "
#     else:
#         opt=opt+i+" "
# print(opt)



# def reg(dic):
#     usr=input("Enter a Username: ")
#     if usr in dic.keys():
#         print("Username already exist,Try Login")
#         r = input("Enter L for Login: ").upper()
#         if r == "L":
#             login(dic)
#         else:
#             print("Wrong Choice")
#     else:
#         psw = int(input("Enter a Password: "))
#         dic[usr]=psw
#         print('Registration Done!')
# def login(dic):
#     usr = input("Enter a Username: ")
#     psw = int(input("Enter a Password: "))
#     if usr in dic.keys():
#         if psw==dic[usr]:
#             print("Login Successful")
#         else:
#             print("Wrong Username or password!")
#             r=input("Enter C for change password: ").upper()
#             if r=="C":
#                 change_psw(dic)
#             else:
#                 print("Wrong Choice")
# def change_psw(dic):
#     usr1=input("Enter Username: ")
#     print("Verify")
#     old_psw=int(input("Enter Old Password: "))
#     if old_psw==dic[usr1]:
#         new_psw=int(input("Enter new password: "))
#         dic[usr1]=new_psw
#     else:
#         print("Wrong Password:")
# dic={"Rezal":564789,"Muskan":766564}
# m=input("Enter Y if u wanna continue: ").upper()
# while m=="Y":
#     c=input("Enter R for register, L for Login, C for change password: ").upper()
#     if c=="R":
#         reg(dic)
#     elif c=="L":
#         login(dic)
#     elif c=="C":
#         change_psw(dic)
#     else:
#         print("Wrong Choice!")
#     m = input("Enter Y if u wanna continue: ").upper()