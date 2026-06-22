# import random
# qstbnk={"2+2=":{"6":False,"4":True,"5":False,"7":False},
#         "4/2=":{"6":False,"4":False,"2":True,"7":False},
#         "5+7=":{"6":False,"4":False,"5":False,"12":True},
#         "8-4=":{"6":False,"4":True,"5":False,"7":False},
#         "3-2=":{"1":True,"4":False,"5":False,"7":False}}
# paper=set()
# while len(paper)!=2:
#     lst=(list)(qstbnk.keys())
#     paper.add(random.choice(lst))
# score=0
# for qst in paper:
#     print("Question: ",qst)
#     option=qstbnk.get(qst)
#     print(option)
#     ans=input("Enter your answer:")
#     if option.get(ans)==True:
#         score+=10
#     else:
#         score-=2.5
# print(score)



# import time
# def time_ticker(nos=120):
#     while nos>=0:
#         min,sec=divmod(nos,60)
#         timer=f"{min:02d}:{sec:02d}"
#         print("\r",timer,end=" ")
#         nos-=1
#         time.sleep(1)
#     print("Time is up")
# time_ticker(5)



# import re
# def validate_email(emailid):
#     pat=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
#     return re.match(pat,emailid) is not None
# eml=input("Enter email: ")
# if validate_email(eml):
#     print("Email is Valid")
# else:
#     print("Not Valid")