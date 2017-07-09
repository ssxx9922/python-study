
# 自定义 cmp
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, s):
        if isinstance(s,Student) == False:
            return -1
        if self.score > s.score:
            return -1
        elif self.score < s.score:
            return 1
        else:
            if self.name < s.name:
                return -1
            elif self.name > s.name:
                return 1
            else:
                return 0

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print sorted(L)

# 自定义 repr
class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '(student:%s,%s,%d)' %(self.name,self.gender,self.score)
        __repr__=__str__

s = Student('Bob', 'male', 88)
print s


# 自定义 len
class Fib(object):

    def __init__(self, num):
        self.fib = []
        for i in range(0,num):
            if len(self.fib) < 2:
                self.fib.append(i)
            else:
                a = self.fib[i-2] + self.fib[i-1]
                self.fib.append(a)
        

    def __str__(self):
        return str(self.fib)
    
    __repr__=__str__

    def __len__(self):
        return len(self.fib)

f = Fib(10)
print(f)
print(len(f))

# 自定义加减乘除方法
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        g = gcd(self.p,self.q)
        return str(self.p/g) + '/' + str(self.q/g)

    __repr__ = __str__

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print(r1 + r2)
print(r1 - r2)
print(r1 * r2)
print(r1 / r2)


# 自定义 set get
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score
        self.__grade = 'c'
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    @property
    def grade(self):
        if self.score > 80:
            grade = 'A'
        elif self.score < 60:
            grade = 'B'
        else:
            grade = 'C'
        return grade

s = Student('Bob', 59)
print(s.grade)

s.score = 60
print(s.grade)

s.score = 99
print(s.grade)

# 限制属性列表
class Person(object):

    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    __slots__ = ('score')

    def __init__(self, name, gender, score):
        self.score = score

s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print(s.score)

# call 方法
class Fib(object):
    def __call__(self,num):
        L = [0,1]
        i = 2
        while i < num:
            L.append(L[i-2]+L[i-1])
            i=i+1     
        return L

f = Fib()
print(f(10))

