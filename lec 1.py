# from math import sqrt,isqrt
# lst=[]
# for i in range(1,11):
#     num=int(input("Enter a number:"))
#     lst.append(num)
#
# for i in lst:
#     if sqrt(i)==int(sqrt(i)):
#         print("Perfect Square: ",i )
#


# price=[100,200,400,500]
# qty=[2,4,3,5,3]
# amount=0
# print("price\tqty\tamount")
# for i,j in zip(price,qty):
#     print(f"{i}\t{j}\t{i*j}")
#     amount+=i*j
#     print("TotalBill:",amount)



# lst=[10,20,20,49,40,33,33]
# while True:
#     if 49 in lst:
#         lst.remove(49)
#     else:
#         break
#
# print(lst)


# st="Rezal Muskan riya"
# lst=st.split()
# print(lst)
# for word in lst:
#     print(word," ",len(word))
# lst.sort(key=len)
# print("largest string: ",lst[-1])



# lst=[10,20,30,20,10]
# res=30
# ans=set()
# for num in lst:
#     cmp=res-num
#     if cmp in ans:
#         print((num,cmp))
#     ans.add(num)



# from random import randint
# s=set()
# while len(s)!=10:
#     s.add(randint(1,20))
# print(s)



# import random
# ques=["3-2=","4+3=","3+2=","5-7=","3/3="]
# q_ppr=set()
# while len(q_ppr)!=2:
#     q_ppr.add(random.choice(ques))
# print(q_ppr)


# lst1={10,20,33,42}
# lst2={22,33,43,20}
# a=lst1.intersection(lst2)
# print(a)
