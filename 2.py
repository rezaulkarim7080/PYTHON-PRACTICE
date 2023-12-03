
# import keyword as kw

# print(kw.kwlist)

# print("length of kw list",len(kw.kwlist))

# a = "Rezaul Karim"

# print(a.upper())
# print(a.lower())

# a=10

# print("value of a",a)
# print("typeof value of a",type(a))

# b=3
# c=14

# print("typeof value b= {} of c= {} ".format(b,c))


# name=input("tere nam vol : ")
# print(name)

# n,k = map(int,input().split())#/// 10 20-->input
# n,k = map(int,input().split(","))#/// 10,20-->input

# print(n)
# print(k)

# print(n)
# print(k)


# c,d,e =5,10,"this is e";

# print(c)
# print(d)
# print(e)
# print(e[:])#full string
# print(e[0])#first character of e
# print(e[-1])#last character of e
# print(e[4:])#start 4 character of e
# print(e[:4])#end 4 character of e
# print(e[1:4])#start 1 end 4 character of e

# numbers = [10,20,30,40,50,60,70]
# print(numbers[::2])#// print after [10, 30, 50, 70]
# print(numbers[2::2])


# ----------- --------------- if else  -----------------------------

# a = 4

# if a > 10:
#     print("pass")
# elif 7 < a < 10:  # Fixing the syntax for the second condition
#     print("almost pass")

# print("false")



# loop


# for i in range(1,10):
#     print(i)


# for i in range(1,10,2):
#     print(i)
        
# ///prime numebr

# num=17
# for i in range(2,num):
#     if(num % i )== 0:
#         print(" NOT PRime Number")
#         break
#     else:
#       print(" PRime Number")   
#       break

# PRINT PRIME NUMBER 

# start = 50
# end = 100

# for num in range(start,end+1):
    
#     if num > 1:
#         for i in range(2,num):
            
#             if num%i ==0 :
#               break
#         else:
#           print(num)
         
         
# /////SUM 

# sum=0
# for i in range(1,10):
#     if(i % 2 )== 0:
#         sum+=i;
        
# print(sum)

# ----------- --------------- LIST -----------------------------
# LIST 


# lst = ["kg","viku","Chiku","kalam"]

# for i in range(len(lst)):
#      print(lst[i])
    #  or 
# for i in lst:
#      print(i)


# list_1 = ["one","two","three","four","five"]
# list_2 = [4, 55, 64, 32, 16, 32]
# list_3 = [[1,2],[5,8]]
# lsit_4 = [1,'chintu',12,4.5]

# print(list_1)
# print("list_1 is length is ", len(list_1))
# list_1.append("six")
# print("append list_1 is :",list_1)
# list_1.remove("six")
# print(list_1)
# list_1.insert(5,"six")
# print("insert list_1 is :",list_1)
# list_1.append(list_2)
# print("append list_1 is :" ,list_1)
# list_1.extend(list_2)
# print("extend list_1 is :" ,list_1)
# lsit_4.reverse()
# print("reverse list_4 is :" ,lsit_4)

# list_2.sort()
# print("sort list_2 is :" ,list_2)

# new_list = lsit_4+ list_1
# print(new_list)


# name = "my name rezaul karim"
# namesplit = name.split()
# print(namesplit)



# del list_2[1]
# print(list_2)      
# a = list_2.pop()
# print(a)           
# print(list_2) 
 
# if "one"  in list_1:
#     print("yes")
# if "ten"  not in list_1:
#     print("No")

# # LSIT Comprehance 

# squers = []

# for i in range(1,10):
#     squers.append(i**2)
# print("squers is : ", squers)

# squers2 = [i**2 for i in range(10)] 
# print("squers2 is : ", squers2)


# numners=[1,2,4,5,3,2,1,5,7,8,4,5]
# print(numners.count(1))#/count frequency 1

# ----------- --------------- Tuple -----------------------------
