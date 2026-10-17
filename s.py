n=int(input("enter the  number of student"))
name=input("name:")
for i in range(0,n):
    print("--"*10)
    mark1=int(input("enter the mark1:"))
    mark2=int(input("enter the mark2:"))
    mark3=int(input("enter the mark3:"))
    total=mark1+mark2+mark3
    avg=(total)/3
    print(f"total={total:f}")
    print(f"avg={avg:2f}")
    print("--"*10)