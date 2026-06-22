# Variable length arguments
# def max(*values):
#     maxi=0
#     for i in values:
#         if i>maxi:
#             maxi=i
#     return maxi
# r=max(22,33,4,2,1,333,23)
# print(r)



# def create_user(**kwargs):
#     print(kwargs)
# create_user(id="101",name="Rezal",age=47)



# def maketag(tag,content,**attr):
#     st=""
#     for key,val in attr.items():
#         st=st+"'"+key+"="+val+"'"
#     return f"<{tag} {st}>{content}</{tag}"
# s=maketag("a","Visit Google",href="https://google.com",target="_blank")
# print(s)



# def makefilters(**conditions):
#     query="Select * from tbproducts where "
#     cond=[]
#     for field,value in conditions.items():
#         cond.append(f"{field}={value} ")
#         query=query+"and ".join(cond)
#     return query
# s=makefilters(price="500",size="L",brand="abc")
# print(s)



# d=[{"empno":111,"name":"shiven","salary":32000},
#    {"empno":101,"name":"riya","salary":34000},
#    {"empno":102,"name":"manya","salary":36000},
#    {"empno":100,"name":"shiv","salary":30000}]
# d.sort(key=lambda x:x["name"])
# print(d)



# def pipeline(value,*funcs):
#     for func in funcs:
#         value=func(value)
#     return value
# s=pipeline(5,lambda x:x+3,lambda x:x-1, lambda x:x/2)
# print(s)

#Filter
# fruits=['Apple','Orange','Mango']
# print(list(filter(lambda x:'e' in x,fruits)))


#Map
# student=[{"empno":111,"name":"shiven","salary":32000},
#          {"empno":101,"name":"manya","salary":33000}]
# print(list(map(lambda students : students['empno'],student)))



#Reduce
# import functools
# l=[22,33,2,4,3]
# print(functools.reduce(lambda x,y: x if x>y else y,l))



# l=[2,3,42,5,32]
# l=[i*2 for i in l]
# print(l)



# l2=[i*2 for i in range(10) if i%2==0]
# print(l2)



fruits=['Apple','Orange','Mango']
l1=[i for i in fruits if 'o' in i]
print(l1)