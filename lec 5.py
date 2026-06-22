# import time
# start = time.time()
# lst=[1,4,22,53]
# lst1=[ i for i in lst if i%2==0]
# end=time.time()
# print(f"{start-end} milliseconds")

# import time
# start=time.time()
# lst=[1,4,22,53]
# lst1=[]
# for i in lst:
#     lst1.append(lst)
# end=time.time()
# print(f"{start-end} milliseconds")


# num1,num2,num3=[int(i) for i in input("Enter three numbers: ").split(" ")]
# print(num1,num2,num3)


# lst=["shalini","shjhk","jdghk"]
# lst1=[i for i in lst if any([x for x in i if x in "aeiou"])]
# print(lst1)


#Map
# from math import factorial
# lst=[2,4,6,5]
# m=list(map(factorial,lst))
# print(m)


# prices=[220,330,250,150]
# qty=[2,4,3,2]
# lst=list(map(lambda x,y: x*y if x<300 else x*y*0.09, prices,qty))
# print(lst)


# lst=["string","rezal","shjjh","000076565"]
# lst1=list(filter(str.isalpha,lst))
# print(lst1)



# marks={'Aarav':85,'Priya':45,'Rohan':92,'Meera':38,'Vikram':67 }
# dict=dict(filter(lambda x:x[1]>=50,marks.items()))
# print(dict)



# students=[('Aarav',85),('Priya',92),('Rohan',78),('Meera',95)]
# lst=sorted(students,key=lambda x: x[1], reverse=True)
# print(lst)



# c=[0,20,37,200]
# f=list(map(lambda x:x*9/5+32,c))
# print(f)



# records=[{'name':"Aarav","age":16},{'name':"Priya","age":15},{'name':"Vikram","age":17},{'name':"Meera","age":14}]
# lst=list(map(lambda x:x['name'],records))
# s=sorted(lst,key=lambda x:len(x),reverse=True)
# print(s)



# records=[{'name':"Aarav","age":16},{'name':"Priya","age":15},{'name':"Vikram","age":17},{'name':"Meera","age":14}]
# f=list(filter(lambda x:x['age']>15,records))
# s=list(map(lambda x:x['name'],f))
# print(s)



# records=[{'name':"Aarav","age":16},{'name':"Priya","age":15},{'name':"Vikram","age":17},{'name':"Meera","age":14}]
# result=sorted(records,key= lambda x: (x['name'], -x['age']))
# print(result)


# l=['a','B']
# s=set(map(str.upper,l))
# print(s)


