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

#반복
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

#60
a, b = map(int, input().split())
print(a&b)