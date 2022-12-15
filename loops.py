lin = int(input("Ile linijek wariacie? "))
x = 1
s = int(lin)
while x<=int(lin)*2:
    print(" "*s  + ('*'*x))
    x+=2
    s-=1
else:
    print(lin*' '+'*')
