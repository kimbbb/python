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

# a=int(input())
# star=1
# space=a-1
# for i in range(1,a+1):
#     # print('*'*star)
#     # star+=1
#     print(' '*space+'*'*star)
#     star+=1
#     space-=1

# #71
# while True:
#     a=int(input())
#
#     if a==0:
#         break
#     else:
#         print(a)

#
# #72
# a=int(input())
# for i in range(1,a+1):
#     print(a)
#     a-=1

# #73
# a=int(input())
# for i in range(1, a+1):
#     print(a-i)


# #74
# a=input()
# a=ord(a)
# count=a-96
# sum=97
# for i in range(count):
#     print(chr(sum), end=' ')
#     sum += 1

# #75
# a=int(input())
# for i in range(a+1):
#     print(i)

#76
# a=int(input())
# for i in range(a+1):
#     print(i)

# #77
# a=int(input())
# sum=0
# for i in range(a+1):
#     if i%2==0:
#         sum+=i
# print(sum)

# #78
# while True:
#     a = input()
#     if a=='q':
#         print(a)
#         break
#     else:
#         print(a)

# #79
# a=int(input())
# sum=0
# count=0
# for i in range(1, a+1):
#     if sum>=a:
#         print(count)
#         break
#     else:
#         sum+=i
#         count+=1

# #80
# n,m=map(int, input().split())
# dice=0
# max=0
# if n>m:
#     max=n
# else:
#     max=m
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print(i, j)

# #1~n까지의 수 중 마지막 수에 1이 몇 개 들어있는지
# n=int(input())
# count=0
# sum=0
# for i in range(1, n+1):
#     count+=1
#     if count%10==1:
#         sum+=1
# print(sum)
#
# #최댓값
# #입력->또입력->최댓값
# a=int(input())
# max=0
# for i in range(a):
#     b=int(input())
#     if b>max:
#         max=b
# print(max)

# #81
# n=input()
# n=int(n,16)
# for i in range(1, 16):
#     print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

# #82
# a=int(input())
# for i in range(1, a+1):
#     if i%10==3 or i%10==6 or i%10==9:
#         print('X', end=' ')
#     else:
#         print(i, end=' ')

# #83
# r,g,b=map(int, input().split())
# count=0
# for i in range(r):
#     for j in range(g):
#         for x in range(b):
#             print(i, end=' ')
#             print(j, end=' ')
#             print(x)
#             count+=1
# print(count)

#84
# h, b, c, s=map(int, input().split())
# sum=h*b*c*s
# mb=sum/8/1024/1024
# print(round(mb, 1),'MB')

#85
# w,h,b=map(int, input().split())
# sum=(w*h*b)/8/1024/1024
# print("{:.2f}".format(sum), 'MB')

#86
# n= int(input())
# i=0
# sum=0
# while True:
#   sum+=i
#   i+=1
#   if(sum>=n):
#      break
# print(sum)


#87
# a=int(input())
# for i in range(1, a+1):
#     if i%3==0:
#         continue
#     print(i, end=' ')

#88
# a,d,n = map(int, input().split())
# print(a+d*(n-1))

#89
# a,r,n = map(int, input().split())
# for i in range(n-1):
#     a = a*r
# print(a)

# #90
# a,m,d,n=map(int, input().split())
# for i in range(n-1):
#     a = a*m+d
# print(a)

# #91
# a,b,c=map(int, input().split())
# d=1
# while True:
#     if d%a!=0 or d%b!=0 or d%c!=0:
#         d+=1
#     else:
#         print(d)
#         break

#1
# A=int(input())
# B=int(input())
# count=0
#
# for i in range(1,A+1):
#     if i%B==0:
#         count+=i
# print(count)

#2
# N=int(input())
# K=int(input())
# count=0
#
# for i in range(1,N+1):
#     if N%i==0:
#         count+=1
#         if count==K:
#             print(i)
# if count<K:
#     print(-1)

#3
# for i in range(3):
#     a, b, c, d = map(int, input().split())
#     sum=a+b+c+d
#     if sum==0:
#         print('D')
#     elif sum==4:
#         print('E')
#     elif sum==1:
#         print('C')
#     elif sum==2:
#         print('B')
#     elif sum==3:
#         print('A')

#4
# A=int(input())
# count=0
# nocount=0
#
# for i in range(A):
#     N=int(input())
#     if N==1:
#         count+=1
#     elif N==0:
#         nocount+=1
# if count<nocount:
#     print('신메뉴 재검토 필요')
# else:
#     print('신메뉴 출시')

#5
# N=int(input())
# sum=0
# count=0
# min=100
#
# for i in range(N):
#     a=int(input())
#     if a%2==0:
#         sum+=a
#         if min>a:
#             min=a
#     else:
#         count+=1
#
# if count==N:
#     print(-999)
# else:
#     print(sum)
#     print(min)

#6
# N=int(input())
# acount=0
# bcount=0
# for i in range(N):
#     p=input()
#     if p=='A':
#         acount+=1
#     elif p=='B':
#         bcount+=1
# if acount>bcount:
#     print('A')
# else:
#     print('B')

#7
# sum=0
# count=0
# while True:
#     a=int(input())
#     if a!=-999:
#         sum+=a
#         count+=1
#     else:
#         break
# print(sum//count)

#8
# A=int(input())
# B=int(input())
# C=int(input())
# sum=A+B
# drink=0
#
# while True:
#     drink+=sum//C
#     sum=sum%C+sum//C
#
#     if sum<C:
#         break

# A=int(input())
# B=int(input())
# C=int(input())
# sum=A+B
# drink=0
#
# while True:
#     drink+=sum//C
#     sum=sum%C+sum//C
#
#     if sum<C:
#         break
# print(drink)


# #9
# A=int(input())
# count=0
# while True:
#     if A%50==0:
#         A-=50
#         count+=1
#     elif A%50!=0:
#         A-=30
#         count+=1
#     if A==0:
#         print(count)
#         break
#     elif A>0 and A<30:
#         print(-1)
#         break

#coders

#1
# a=input()
# b=len(a)
# sum=6
# for i in range(b):
#     if a[i%2==0]=='(':
#         sum+=3
#
#     elif a[i%2==0]!='(' or a[i%2==0]=='(':
#         sum+=6
#
# if a[i%2==0] == '(':
#     print(sum-3)
#
# elif a[i%2==0] != '(' or a[i%2==0] == '(':
#     print(sum-6)

#2
# a=input()
# print(a[0:10])
# print(a[10:])

# #3
# q=int(input())
# count=0
# xcount=0
# for i in range(q):
#     a=input()

#coders
#1
# a=input()
# sum=6
# for i in range(1,len(a)):
#     if a[i]==a[i-1]:
#         sum+=3
#     else:
#         sum+=6
# print(sum)

#2
# a=input()
# t=0
# for i in range(0,len(a),10):
#     print(a[i:i+10])

#3
# q=int(input())
# for i in range(q):
#     o = 0
#     x = 0
#     a=input()
#     for j in range(len(a)):
#         if a[j]=='O':
#             o+=1
#         if a[j]=='X':
#             x+=1
#     print(len(a), o, x)

#4
# a=input()
# for i in range(len(a)):
#     if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u':


#5
# A=int(input())
# B=input()
# sum=0
# for i in range(len(B)):
#     sum+=int(B[i])
# print(sum)

#4
# S=input()
# for i in range(len(S)):
#     a=ord(S[i])
#     if a>=88:
#         a-=23
#     else:
#         a += 3
#     print(chr(a), end='')

#5
# a=int(input())
# for i in range(a):
#     T=input()
#     N=int(input())
#     for j in range(len(T)):
#         print(T[j]*N, end='')

#6
# a=input()
# b=input()
# sum=0
# for i in range(len(a)):
#     if a[i]==b:
#         sum+=1
# print(sum)

#7
# a=input()
# for i in range(len(a)):
#     b=a[i].isupper()
#     if b==True:
#         b=a[i].lower()
#     elif b==False:
#         b=a[i].upper()
#     print(b,end='')


#정수 5개 배열에 한 줄에 저장하고 차례대로 출력
# a=list(map(int, input().split()))
# print(a)

#정수 5개 저장하고 출력
# a=[]
# for i in range(5):
#     a.append(int(input()))
#
# print(a)

#역순 출력
# a=list(map(int, input().split()))
# a.reverse()
# print(a)

#문자 짝수 출력
# a=list(input().split())
# b=0
# for i in range(len(a)):
#     b+=1
#     if b%2==0:
#         print(a[i], end=' ')

#공백을 기준으로 정수를 입력받아 100이상 수 출력
# a=list(map(int, input().split()))
# for i in range(len(a)):
#     if a[i]>=100:
#         print(a[i], end=' ')

#10개의 정수를 입력받아 리스트에 저장한 후 오름차순으로 정렬하여 출력
# a=list(map(int, input().split()))
# a.sort()
# print(a)

#10개의 정수를 입력받아 리스트에 저장한 후 내림차순으로 정렬하여 출력하는 프로그램
# a=list(map(int, input().split()))
# a.sort()
# a.reverse()
# print(a)

#정수를 입력받아 짝수의 개수를 구하는 프로그램
# a=list(map(int, input().split()))
# b=0
# for i in range(len(a)):
#     if a[i]%2==0:
#         b+=1
# print(b)

#정수를 원하는 만큼 배열에 저장하고 모든 요소의 합을 구하는 프로그램
# a=list(map(int, input().split()))
# b=0
# for i in range(len(a)):
#     b+=a[i]
# print(b)

#10개의 정수를 입력받아 100미만의 수 중 가장 큰 수와 100이상의 큰 수 중 가장 작은 수 출력
# a=list(map(int, input().split()))
# min=1000
# max=0
# for i in range(len(a)):
#     if a[i]>=100 and min>a[i]:
#         min=a[i]
#     elif a[i]<100 and max<a[i]:
#         max=a[i]
# print(max, min)

#정수를 차례대로 입력받다가 0이 입력되면 0을 제외한 요소들을 차례대로 출력하는 프로그램
# a=[]
# while True:
#     b=int(input())
#     if b==0:
#         break
#     else:
#         a.append(b)
#
# print(a)

#정수를 차례대로 입력받다가 0이 입력되면 0을 제외한 요소 거꾸로 출력
# a=[]
# while True:
#     b=int(input())
#     if b==0:
#         break
#     else:
#         a.append(b)
# a.reverse()
# print(a)


#10개의 문자를 입력받아 입력받은 문자를 이어서 출력
# a=list(input().split())
# for i in range(len(a)):
#     print(a[i], end='')

#영문 대문자를 입력받다가 대문자 이외의 문자가 입력되면 입력을 중단하고
#영문 대문자들에 대하여 1번 이상 입력된 각 문자와 그 문자의 개수를 출력하는 프로그램
# a=input().split()
# temp = sorted(set(a))
# for i in temp:
#     print('{} : {}'.format(i,a.count(i)))


#5명의 국어, 수학, 영어, 과학 점수를 받아 평균 80점 이상이면 pass
#그렇지않으면 fail 출력하는 프로그램
# pas = 0
# for i in range(5):
#     sum=0
#     a=list(map(int, input().split()))
#     for j in range(len(a)):
#         sum+=a[j]
#     if sum/4>=80:
#         print('pass')
#         pas+=1
#     else:
#         print('fail')
# print(pas)

#성적 처리 프로그램
#학생들의 성적을 입력받아 리스트에 저장.
#성적의 평균을 구하고 최대, 최소, 80점 이상의 점수를 받은 학생 수를 계산하여 출력하라
# b=[]
# peo=0
# for i in range(5):
#     a=int(input())
#     if a>=80:
#         peo+=1
#     b.append(a)
# sum=sum(b)
# print('성적 평균 :', sum/5)
# print('최대 점수 :', max(b))
# print('최소 점수 :', min(b))
# print('80점 이상 :', peo)

#리스트에서 2번쨰로 큰 수 찾기
# a=[-7,2,3,8,6,6,75,38,3,2]
# a.sort()
# print(a[-2])

#콘테스트
#최소값과 최대값 리스트에서 제거
# a=[10.0,9.0,8.3,7.1,3.0,9.0]
# a.remove(max(a))
# a.remove(min(a))
# print(a)

#stack
# a=[]
# for i in range(3):
#     b=input()
#     a.append(b)
# a.reverse()
# print(a)

#친구관리
# b=[]
# while True:
#     print('-'*30)
#     print('1. 친구 리스트 출력')
#     print('2. 친구 추가')
#     print('3. 친구 삭제')
#     print('4. 이름 변경')
#     print('9. 종료')
#     print('-' * 30)
#
#     a=int(input('메뉴를 선택하시오 : '))
#     if a==1:
#         print(b)
#     elif a==2:
#         c=input('추가할 친구의 이름을 입력해주세요 : ')
#         b.append(c)
#     elif a==3:
#         d=input('삭제할 친구의 이름을 입력해주세요 : ')
#         b.remove(d)
#     elif a==4:
#         e=input('기존 이름을 입력해주세요 : ')
#         b.remove(e)
#         f=input('새로운 이름을 입력해주세요 : ')
#         b.append(f)
#     elif a==9:
#         break
#     else:
#         continue

#리스트 합병
# a=[1,2,3,4]
# b=[2,2,2,2]
# print(a+b)
#
# print(a)
# print(b)

#리스트 비교
# list1=[1,2,3]
# list2=[1,2,3]
# print(list1==list2)
# print(list1>list2)

#리스트 얕은 복사
# temp=[1,2,3,4,5]
# a=temp
# print(temp)
# a[3]=39
# print(temp)

#리스트 깊은 복사
# temp=[1,2,3,4,5]
# a=list(temp) #lsit()는 객체의 생성자. 객체를 생성하고 초기화한다. 다른 객체를 받아서 리스트로 변환함

#슬라이싱
# a=[1,2,3,4,5,6,7,8,9,10]
# print(a[:]) #전체
# print(a[1:4]) #선택 1~3까지 출력
# print(a[::-1]) #역순
#시작과 끝 인덱스는 생략이 가능하다.

#고급 슬라이싱
# a=[1,2,3,4,5,6,7,8,9,10]
# print(a[2:7:2])
#    시작 끝 간격

#리스트 변경
# list = [1,2,3,4,5,6,8]
# list[0:3]=['하이', '헬로', '바이'] //리스트 일부 변경
#
# list[::2]=[99,99,99,99] #중간에 요소 추가
#
# list[:]=[] #모든 요소 삭제
# print(list)

#리스트 변경
# num=list(range(0,10)) #0~9
# print(num)
# del num[-1] #특정 요소 삭제
# print(num)


# N=int(input())
#
# def big(a, b):
#     max=0
#     if a>b:
#         max=a
#     elif b>a:
#         max=b
#     elif a==b:
#         max=123456789
#     return max
#
# for i in range(N):
#     A,B=map(int,input().split())
#     c=big(A,B)
#     print(c)

def sum(A,B):
    sum=A+B
    return sum
def sub(A,B):
    sub=A-B
    return sub
def mul(A,B):
    sub=A*B
    return sub
def div(A,B):
    sub=A//B
    return sub


# while True:
#     a=int(input())
#     if a==0:
#         break
#     elif a==1:
#         A,B=map(int,input().split())
#         c=sum(A,B)
#         print(c)
#     elif a==2:
#         A,B=map(int,input().split())
#         c=sub(A,B)
#         print(c)
#     elif a==3:
#         A,B=map(int,input().split())
#         c=mul(A,B)
#         print(c)
#     elif a==4:
#         A,B=map(int,input().split())
#         c=div(A,B)
#         print(c)

# a=list(map(int,input().split()))
#
# def sum(a):
#     plus=0
#     for i in range(len(a)):
#         plus+=a[i]
#     return plus
#
# b=sum(a)
# print(b)

# T=int(input())
#
# long = []
# def lenght(a):
#     long.append(len(a))
#     return long
#
# for i in range(T):
#     N=input()
#     c=lenght(N)
#
# for j in range(len(c)):
#     print(c[j], end=' ')

T=int(input())
b=[]
c=[]
for i in range(T):
    a,n=map(int, input().split())
    max = n
    while True:
        if n == 1:
            break

        if n%2==0:
            n//=2
        elif n%2!=0:
            n*=3
            n+=1
        if max<n:
            max=n
    b.append(a)
    c.append(max)

for x in range(len(b)):
    print(b[x], c[x])





