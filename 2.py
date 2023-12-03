
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


# if else 


# a = 4

# if a > 10:
#     print("pass")
# elif 7 < a < 10:  # Fixing the syntax for the second condition
#     print("almost pass")

# print("false")



# loop


for i in range(1,10):
    print(i)
        
# ///prime numebr

num=17
for i in range(2,num):
    if(num % i )== 0:
        print(" NOT PRime Number")
        break
    else:
      print(" PRime Number")   
      break

# /////SUM 

sum=0
for i in range(1,10):
    if(i % 2 )== 0:
        sum+=i;
        
print(sum)