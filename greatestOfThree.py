def greatestOfThree(n1, n2, n3):
    if n1>n2>n3:
        return n1
    elif n2>n3>n1:
        return n2
    
    elif n3>n1>n2:
        return n3
    elif n1>n2==n3:
        return n1
    elif n2>n1==n3:
        return n2
    elif n3>n1==n2:
        return n3
    elif n1==n2==n3:
        return n1
    elif -n1<-n2<-n3:
        return -n3
    elif -n2<-n3<-n1:
        return -n1
    
    elif -n3<-n1<-n2:
        return n2

print(greatestOfThree(6,2,9))


