s=input("Enter the sentence ")
i=0
st=""
l=len(s)
for i in range(0,l):
    ch=s[i]
    if ch!=' ':
        d=ord(ch)
        if ((d>=89 and d<=90) or (d>=120 and d<=122)):
            d=d-23
        else:
            d=d+3
        ch=chr(d)
        st=st+ch
    i+=1
print("The caeser cipher is ",st)
