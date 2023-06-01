def Regression():
    # print("hello world")
    X=[0 for x in range(10)]
    Y=[0 for x in range(10)]
    SumX=0
    SumX2=0
    SumY=0
    SumXY=0
    a=0
    b=0
    DataPoints=input("Total DataPoints ?  ")
    total=int(DataPoints)
    for i in range(total):
        print("Enter Value x",i+1 ,"-->"  ,end="")
        X[i]=int(input())
        print("Enter Value y",i+1 ,"-->" ,end="")
        Y[i]=int(input())
  
    
    for i in range(total):
        SumX = SumX + X[i]
        SumX2 = SumX2 + X[i]*X[i]
        SumY = SumY + Y[i]
        SumXY = SumXY + X[i]*Y[i]
    b = (total*SumXY-SumX*SumY)/(total*SumX2-SumX*SumX)
    a = (SumY - b*SumX)/total
    
    print("Calculated value of B1-->", round(a,2) ,"and B0-->",round(b,2))
    print("Equation of best fit is: y = ", round(a,2) ," + ", round(b,2),"x")
Regression()
