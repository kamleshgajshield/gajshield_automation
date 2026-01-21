# 1 factorial number
a=1
for i in range(1,6):
    a=a*i
print("this is factorial number",a)   


# 2 fibbonacci series
a=5
x=0
y=1
z=0
while a>=z:
    x=y
    y=z
    z=x+y
print("fibbonacci series",z) 

# 3 find where vowel replace "*" remaining consonant should be print as it is ---
a="janvi and gayatri"
n=""
for i in a:
    if i in "aeiou":
        n=n+"*"
    else:
        n+=i
print("all word",n)    

print("hello mr selenium automation")