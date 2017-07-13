from pyquery import PyQuery as pq

doc = pq(filename = 'hello.html')
print(doc.html())
print(type(doc))
lis = doc('li')
print(type(lis))
print(lis.text())


p = pq('<p id="hello" class="hello"></p>')('p')
print(p.attr("id"))
print(p.attr("id", "plop"))
print(p.attr("id", "hello"))

print('==========')

print(p.addClass('beauty'))
print(p.removeClass('hello'))
print(p.css('font-size', '16px'))
print(p.css({'background-color': 'yellow'}))

print('==========')

print(p.append(' check out <a href="http://reddit.com/r/python"><span>reddit</span></a>'))
print(p.prepend('Oh yes!'))
d =(pq('<div class="wrap"><div id="test"><a href="http://cuiqingcai.com">Germy</a></div></div>'))
p.prependTo(d('#test'))
print(p)
print(d)
d.empty()
print(d)

print('=======')

from pyquery import PyQuery as pq
doc = pq(filename='hello.html')
lis = doc('li')
for li in lis.items():
    print(li.html())
 
print(lis.each(lambda e: e))