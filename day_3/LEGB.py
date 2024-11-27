#  local, Enclosing, Globle,Built _in
x="globle x"
def test():
    global x
    x='local x'
    y="local y"
    print(y)
    print(x)
test()
print(x)



