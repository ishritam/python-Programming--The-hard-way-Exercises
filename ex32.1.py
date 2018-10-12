element = [1,2,3,4,5]
element.append(6)
element.clear()  #empty the list -->[]
element.append(1,2,3,4,4,5)

print(element)


D:\Python>python
Python 3.7.0b3 (v3.7.0b3:4e7efa9c6f, Mar 29 2018, 18:42:04) [MSC v.1913 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> a=["Shritam","Kumar","Mund",19,"Dharamgarh"]
>>> b="Hi,{first} {mid} {last}.  You are {age}. You'r hometown is {city}"
>>> b.format(first = a[0], mid=a[1], last=a[2], age=a[3], city=a[-1])
"Hi,Shritam Kumar Mund.  You are 19. You'r hometown is Dharamgarh"
>>> c=[1,2,3]
>>> c.insert(1,"Hello")
>>> c
[1, 'Hello', 2, 3]
>>> c=[0,1,2,3]
>>> c.insert(1,"Hello")
>>> c
[0, 'Hello', 1, 2, 3]
>>> c.del(1)
  File "<stdin>", line 1
    c.del(1)
        ^
SyntaxError: invalid syntax
>>> del c[1]
>>> c
[0, 1, 2, 3]
>>> c.pop(1)
1
>>> c
[0, 2, 3]
>>> c.pop(1)
2
>>>
>>> d= [1,2,4,5,6]
>>> c.extend(d)
>>> c
[0, 3, 1, 2, 4, 5, 6]
>>> c.sort()
>>> c
[0, 1, 2, 3, 4, 5, 6]
>>> c.reverse()
>>> c
[6, 5, 4, 3, 2, 1, 0]
>>>
