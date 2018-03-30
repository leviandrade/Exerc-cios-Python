a=int(input('dia'))
b=int(input('mes'))
c=int(input('ano'))
if a<31 and a>0 and b<13 and b>0 and c>0 and b!=2 and b!=4 and b!=6 and b!=9 and b!=11:
    a=a+1
elif a==31 and b==1 or a==31 and b==3 or a==31 and b==5 or a==31 and  b==7 or a==31 and b==8 or a==31 and b==10:
    a=1
    b=b+1
    c=c
    print(a, b , c)

elif a==31 and b==12:
    a=1
    b=1
    c=c+1
    print(a, b , c)

elif a==30 and b==4 or a==30 and b==6 or a==30 and b==9 or a==30 and b==11:
    a=1
    b=b+1
    c=c
    print(a, b , c)

elif a==28 and b==2 and c%4!=0:
    a=1
    b=b+1
    c=c
    print(a, b , c)

elif a==29 and b==2 and c%4==0 and c%100!=0 or a==28 and b==2 and b%400==0 :
    a=1
    b=b+1
    c=c
    print(a, b , c)
elif a==28 and b==2 and c%4==0 and c%100!=0 or a==28 and b==2 and b%400==0 :
    a=a+1
    b=b
    c=c
    print(a ,b , c )
elif a==31 and b==2 or b==4 or b==6 or b==9 or b==11:
    print ("data inválida")
elif a==29 and b==2 and c%4!=0:
    print("data invalida")
elif a==30 and b==2:
    print("data inválida")
else:
    print("data invalida")

