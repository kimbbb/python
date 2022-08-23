#https://codeup.kr/problemsetsol.php?psid=33

# #1
# print("Hello")
#
# #2
# print("Hello","World")
#
# #3
# print("Hello")
# print("World")
#
# #4
# print("'Hello'")
#
# #5
# print('"Hello World"')
#
# #6
# print('\"!@#$%^&*()\'')
#
# #7
# print("\"C:\\Download\\'hello\'.py\"")
#
# #8
# print("print(\"Hello\\nWorld\")")

#입력
# #9
# a=input()
# print(a)
#
# #10
# a=input()
# a=int(a)
# print(a)
#
# #11
# a=input()
# a=float(a)
# print(a)
#
# #12
# a=int(input())
# b=int(input())
# print(a)
# print(b)
#
# #13
# a=input()
# b=input()
# print(b)
# print(a)
#
# #14
# f=float(input())
# print(f)
# print(f)
# print(f)
#
# #15
# a,b=map(int, input().split())
# print(a)
# print(b)
#
# #16
# a,b=(input().split())
# print(b,a)
#
# #17
# a=input()
# print(a,a,a)
#
# #18
# a, b = input().split(':')
# print(a, b, sep=':')
#
# #19
# y, m, d = input().split('.')
# print(d,m,y,sep='-')
#
# #20
# a, b = input().split('-')
# print(a+b)
#
# #21
# a=input()
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
#
# #22
# a=input()
# print(a[0:2], a[2:4], a[4:6])
#
#23
# a,b,c=input().split(':')
# print(b)
#
# #24
# a,b=input().split()
# s=a+b
# print(s)
#
# #25
# a,b=map(int,input().split())
# print(a+b)
#
# #26
# a=float(input())
# b=float(input())
# print(a+b)
#
# #27
# a=int(input())
# print('%x'%a)
#
# #28
# a=int(input())
# print('%X'%a)
#
# #29
# a=input()
# n=int(a,16)
# print('%o' %n)
#
# #30
# a=input()
# print(ord(a))
#
# #31
# a=int(input())
# print(chr(a))
#
# #32
# a=int(input())
# print(-a)
#
# #33
# a=input()
# a=ord(a)
# print(chr(a+1))
#
# #34
# a, b = map(int, input().split())
# print(a-b)
#
# #35
# a, b = map(float, input().split())
# print(a*b)

# #36
# a, b = input().split()
# b=int(b)
# for i in range(b):
#     print(a, end='')
#
# #37
# a=int(input())
# b=input()
# for i in range(a):
#     print(b, end='')
#
# #38
# a, b = map(int, input().split())
# print(a**b)
#
# #39
# f1, f2=map(float, input().split())
# print(f1**f2)
#
# #40
# a, b = map(int, input().split())
# print(a//b)
#
##41
# a, b = map(int, input().split())
# print(a%b)
#
# #42
# a=float(input())
# print( format(a, ".2f") )
#
# #43
# f1, f2=map(float, input().split())
# print(format(f1/f2, '.3f'))
#
# #44
# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# print(format(a/b,'.2f'))
#
# #45
# a, b, c = map(int, input().split())
# sum=a+b+c
# print(sum, end=' ')
# print(format(sum/3, '.2f'))
#
# #46
# a=int(input())
# print(a<<1)
#
# #47
# a, b = map(int, input().split())
# print(a<<b)
#
# #48
# a, b =map(int, input().split())
# if a<b:
#     print('True')
# else:
#     print('False')
#
# #49
# a, b = map(int, input().split())
# if a==b:
#     print('True')
# else:
#     print('False')
#
# #50
# a,b=map(int, input().split())
# if b>=a:
#     print('True')
# else:
#     print('False')
#
# #51
# a,b=map(int, input().split())
# if a!=b:
#     print('True')
# else:
#     print('False')
#
# #52
# a=int(input())
# if a==0:
#     print(bool(a))
# else:
#     print(bool(a))
#
# #53
# a=bool(int(input()))
# print(not a)
#
# #54
# a,b=map(int, input().split())
# print(bool(a) and bool(b))
#
# #55
# a,b=map(int, input().split())
# print(bool(a) or bool(b))
#
##56
# a,b=map(int, input().split())
# c = bool(a)
# d = bool(b)
# print((c and (not d)) or ((not c) and d))
#
# #57
# a,b=map(int, input().split())
# c=bool(a)
# d=bool(b)
# print((c and d) or (not c)and(not d))
#
# #58
# a, b = map(int, input().split())
# c=bool(a)
# d=bool(b)
# print((not c)and(not d))
#
# #60
# a=int(input())
# print(~a)
#
# #60
# a, b = map(int, input().split())
# print(a&b)
#
# #61
# a,b = map(int, input().split())
# print(a|b)
#
# #62
# a,b = map(int, input().split())
# print(a^b)
#
# #63
# a, b = map(int, input().split())
# if a>=b:
#     print(a)
# else:
#     print(b)
#
# #64
# a,b,c=map(int, input().split())
# if a<b and a<c:
#     print(a)
# elif b<a and b<c:
#     print(b)
# elif c<a and c<b:
#     print(c)
# elif a==b and a<c:
#     print(a)
# elif a==c and a<b:
#     print(a)
# elif c==b and c<a:
#     print(c)
# else:
#     print(a)
#
# #65
# a,b,c=map(int, input().split())
# if a%2==0:
#     print(a)
# if b%2==0:
#     print(b)
# if c%2==0:
#     print(c)
#
# #66
# a, b, c = map(int, input().split())
# if a%2==0:
#     print('even')
# else:
#     print('odd')
#
# if b%2==0:
#     print('even')
# else:
#     print('odd')
#
# if c%2==0:
#     print('even')
# else:
#     print('odd')
#
# #67
# a=int(input())
# if a<=-1:
#     if a%2==0:
#         print('A')
#     if a%2!=0:
#         print('B')
# if a>=0:
#     if a%2==0:
#         print('C')
#     if a%2!=0:
#         print('D')
#
# #68
# n=int(input())
# if n>=90:
#     print('A')
# elif n>=70:
#     print('B')
# elif n>=40:
#     print('C')
# else:
#     print('D')
#
# #69
# a= input()
# if a=='A':
#     print('best!!!')
# elif a=='B':
#     print('good!!')
# elif a=='C':
#     print('run!')
# elif a=='D':
#     print('slowly~')
# else:
#     print('what?')
#
# #70
# a=int(input())
# if a==12 or a==1 or a==2:
#     print('winter')
# elif a==3 or a==4 or a==5:
#     print('spring')
# elif a==6 or a==7 or a==8:
#     print('summer')
# elif a==9 or a==10 or a==11:
#     print('fall')


# A=int(input())
# B=int(input())
# sum=0
#
# for i in range(1, A+1):
#     if i%B==0:
#         sum+=i
# print(sum)

# a=int(input())
# b=int(input())
# count=0
#
# for i in range(1, a+1):
#     if a%i==0:
#         count+=1
#         if count==b:
#             print(i)
# if count<b:
#     print(-1)

# a=int(input())
# xcount=0
# count=0
# for i in range(1,a+1):
#     b=int(input())
#     if b==0:
#         xcount+=1
#     if b==1:
#         count+=1
# if xcount>count:
#     print('재검토 필요')
# else:
#     print('출시')

# N=int(input())
# sum=0
# count=0
# min=100
# for i in range(1, N+1):
#     a=int(input())
#     if a%2==0:
#         sum+=a
#         count+=1
#         if a<min:
#             min=a
#
# if sum==0:
#     print(-999)
# else:
#     print(sum)
#     print(min)

# a=int(input())
# b=int(input())
# c=int(input())
# count=0
# cafe=a+b
#
# while True:
#     count+=cafe//c
#     cafe=cafe//c+cafe%c
#
#     if cafe<c:
#         break
# print(count)

# count=0
# a=int(input())
#
# while a>=3:
#     if a%50==0:
#         a-=50
#         count+=1
#     elif a%50!=0:
#         a-=30
#         count+=1
#     elif a==0:
#         break
# if a!=0:
#     print(-1)
# else:
#     print(count)

a=int(input())
star=1
space=a-1
for i in range(1,a+1):
    # print('*'*star)
    # star+=1
    print(' '*space+'*'*star)
    star+=1
    space-=1