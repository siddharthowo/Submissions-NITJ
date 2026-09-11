a,b=13,7

#arithmetic
print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Floor Division:",a//b)
print("Modulus:",a%b)
print("Exponentiation:",a**b)

#relational
print("a>b:",a>b)
print("a==b:",a==b)
print("a!=b:",a!=b)
print("a>=b:",a>=b)
print("a<=b:",a<=b)

#logical
print("(a>5)and(b<10):",(a>5)and(b<10))
print("(a>15)or(b<10):",(a>15)or(b<10))
print("not(a>b):",not(a>b))

#compound assignment
a+=b
print("Aftera+=b:",a)
a-=b
print("Aftera-=b:",a)
a*=b
print("Aftera*=b:",a)
a//=b
print("Aftera//=b:",a)
a**=b
print("Aftera**=b:",a)

#bitwise
x,y=6,3
print("x&y:",x&y)
print("x|y:",x|y)
print("x^y:",x^y)
print("~x:",~x)
print("x<<1:",x<<1)
print("x>>1:",x>>1)

#membership
lst=[1,2,3]
print("2 in list:",2 in lst)
print("5 not in list:",5 not in lst)   