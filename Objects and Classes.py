# Объекты и классы


# Создание пустого класса
class Person:
    pass


# Объект из класса создается с помощью вызова имени класса так, будто он является функцией:
someone = Person()
print(type(someone))
'''
В этом случае Person() создает отдельный объект класса Person и присваивает его имени someone. Но класс Person пуст,
поэтому объект someone просто занимает место и ничего не делает. 
'''


# Добавим в класс специальный метод инициализации __init__
class Person:
    def __init__(self):
        pass


'''
Так выглядят реальные определения классов в Python. __init__() - это особое имя метода, который инициализирует 
отдельный объект с помощью определения его класса. Аргумент self указывает на сам объект.

Когда вы указываете __init__() в определении класса, его первым параметром должен быть объект self. 
Но даже в этом случае второе определение класса Person создает объект, который ничего не делает. 
'''


# Добавим параметр name в метод инициализации
class Person:
    def __init__(self, name):
        self.name = name


# Теперь мы можем создать объект класса Person, передав строку для параметра name:
hunter = Person('Elmer Fudd')
''' Эта строка делает следующее:
1) выполняет поиск определения класса Person;
2) создает новый объект в памяти;
3) вызывает метод объекта __init__, передавая только что созданный объект под именем self и другой аргумент 
('Elmer Fudd') в качестве значения параметра name;
4) сохраняет в объекте значение переменной name;
5) возвращает новый объект;
6) прикрепляет к объекту имя hunter.

Внутри определения класса Person вы получаете доступ к атрибуту name с помощью конструкции self.name
Когда вы создаете реальный объект вроде hunter, то ссылаетесь на этот атрибует как hunter.name

Этот новый объект похож на любой другой объект Python. Вы можете использовать его как элемент списка, словаря или 
множества. Можете передать его в функцию как аргумент или вернуть его в качестве результата.

Не обязательно использовать метод __init__ в описании каждого класса, он используется для того, чтобы различать
объекты одного класса
'''
print('The mighty hunter:', hunter.name)
# ----------------------------------------------------------------------------------------------------------------------


# Наследование
'''
Наследование - создание нового класса из уже существующего, который при этом содержит какие-то дополнения и
изменения. Это отличный способ использовать код повторно. Когда вы применяете наследование, новый класс может
автоматически использовать весь код старого класса и при этом вам не нужно его копировать.

Вы определяете только то, что вам нужно добавить или изменить в новом классе, и этот код переопределяет поведение
старого класса. Оригинальный класс называется предком, суперклассом или базовым классом; новый класс называется
потомком, подклассом или классом-наследником. 
'''

# Определим пустой класс, который называется Car:


class Car:
    pass


# Далее определим подкласс класса Car, который называется Yugo.
# Вы определяете подкласс с помощью того же ключевого слова class, но указывая внутри скобок имя родительского класса:


class Yugo(Car):
    pass


# Создадим объекты каждого класса:
give_me_a_car = Car()
give_me_a_yugo = Yugo()

'''
Класс-потомок является уточненной версией класса-предка: Yugo является Car. 
Объект с имененем give_me_a_yugo является экземпляром класса Yugo, но он также наследует все то, что может делать
класс Car. 
'''


class Car:
    def exclaim(self):
        print("I'm a Car!")


class Yugo(Car):
    pass


# Создадим по одному объекту каждого класса и вызовем их методы exclaim:
give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

'''
Класс Yugo унаследовал метод exclaim() класса Car. Фактически, класс Yugo говорит, что он является классом Car, что 
может привести к кризису самоопределения. Для решения этой проблемы может использоваться перегрузка метода.
'''
# ----------------------------------------------------------------------------------------------------------------------


# Перегрузка метода
'''
Класс Yugo должен как-то отличаться от класса Car, иначе зачем вообще создавать новый класс. 
Изменим способ работы метода exclaim() для класса Yugo:=
'''


class Car:
    def exclaim(self):
        print("I'm a car!")


class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car. but more Yugo-ish.")


print("")
give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

# В этом примере мы перегрузили метод exclaim(). Перегрузить можно любые методы, включая __init__().


# Создадим подклассы для класса Person, которые представляют докторов (MDPerson) и адвокатов (JDPerson):
class Person:
    def __init__(self, name):
        self.name = name


class MDPerson(Person):
    def __init__(self, name):
        self.name = 'Doctor ' + name


class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ', Esquire'


print("")
person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
print(person.name)
print(doctor.name)
print(lawyer.name)

''' В этих случаях метод инициализации __init__() принимает те же аргументы, что и родительский класс Person, но 
внутри объекта сохраняет значение переменной name разными способами
'''
# ----------------------------------------------------------------------------------------------------------------------


# Добавление метода
'''
В класс-потомок можно также добавить метод, которого не было в родительском классе. Возвращаясь к классам Car и Yugo,
мы определилим новый метод need_a_push() только для класса Yugo:
'''


class Car:
    def exclaim(self):
        print("I'm a car!")


class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car. but more Yugo-ish.")

    def need_a_push(self):
        print("A little help here?")


print("")
give_me_a_car = Car()
give_me_a_yugo = Yugo()


give_me_a_yugo.need_a_push()
'''
Объект класса Yugo может реагировать на вызов метода need_a_push()
Объект общего класса Car - нет (будет сгенерировано исключение 'Car' object has no attribute 'need_a_push'
К этому моменту класс Yugo может делать что-то, чего не может делать класс Car, и теперь мы точно можем определить
отдельную личность класса Yugo
'''
# ----------------------------------------------------------------------------------------------------------------------


# Просим помощи у предка с помощью ключевого слова super
'''
Класс-потомок может добавить или перегрузить метод класса-предка. Но для того, чтобы использовать оригинальный метод
родительского класса, можно использовать метод super().
'''


class Person:
    def __init__(self, name):
        self.name = name


class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


'''
Когда вы определяете метод __init__() для своего класса, вы заменяете метод __init__() родительского класса, который
больше не вызывается автоматически. В результате вам нужно вызывать его явно. Происходит следующее:
1) Метод super() получает определение родительского класса Person.
2) Метод __init__() вызывает метод Person.__init__(). Последний заботится о том, чтобы передать аргумент self 
согласно суперклассу, поэтому вам нужно лишь передать опциональные аргументы. В нашем случае единственным аргументом
класса Person() будет name.
3) Строка self.email = email - это новый код, который отличает класс EmailPerson от класса Person. '''
print("")
# Теперь создадим одну персону:
bob = EmailPerson('Bob Frapples', 'bob@frapples.com')

# Мы должны иметь доступ к атрибутам name и email (для записи имени использовался метод родительского класса):
print(bob.name, bob.email)

'''
Одно из преимуществ использования метода super() - возможность применять наследование.
Главное преимущество заключается в том, что если определение класса Person в будущем изменится, с помощью метода
super() мы сможем гарантировать, что атрибуты и методы, которые класс EmailPerson наследует от класса Person, 
отреагируют на изменения.

Используйте метод super(), когда потомок делает что-то самостоятельно, но ему все еще нужно что-то от предка
'''
# ----------------------------------------------------------------------------------------------------------------------


# Получаем и устанавливаем значение атрибутов с помощью свойств
class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

    name = property(get_name, set_name)


'''
Новые методы get_name и set_name действуют как обычные геттеры и сеттеры до последней строки, где они указываются
как свойства атрибута name. Первый аргумент функции property() - это геттер, а второй - сеттер. Теперь, когда вы
обращаетесь к атрибуту name любого объекта Duck, вызывается метод get_name(), который возвращает его:
'''
print("")

fow1 = Duck('Howard')
print(fow1.name)

# Можно вызвать метод get_name() непосредственно, как обычный геттер:
print(fow1.get_name())

# Когда вы присваиваете значение атрибуту name, вызывается метод set_name():
fow1.name = 'Daffy'
print(fow1.name)

# Метод set_name() также можно вызвать непосредственно:
fow1.set_name('Daffy')
print(fow1.name)

''' Еще один способ определить свойства - это декораторы. В следующем примере мы определим два разных метода с именем
name(), предшествовать которым будут разные декораторы '''


class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


# Вы все еще можете получить доступ к атрибуту name, но в этом случае не сущствует видимых методов геттер и сеттер
print("")
fow1 = Duck('Howard')
print(fow1.name)
print("-----------")
fow1.name = 'Donald'
print(fow1.name)


# Свойство может ссылаться не только к отдельному аттрибуту, но и к вычисляемому значению:
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


# Создаем объект класса Circle, задав значение его аттрибута radius
print()
c = Circle(5)
print(c.radius)

# Можно обратиться к свойству diameter точно также, как к атрибуту вроде radius:
print(c.diameter)

# Можно изменить значение атрибута radius и свойство diameter будет рассчитано на основе текущего значения radius:
c.radius = 7
print(c.diameter)

''' Если не указать сеттер для атрибутов, то не получится устанавливать его значение. Это удобно для атрибутов, 
которые должны быть доступны только для чтения: при попытке c.diameter = 20 будет ошибка can't set attribute '''

''' У использования свойств вместо непосредственного доступа к атрибутам имеется еще одно преимущество: если вы 
измените определение атрибута, вам нужно будет поправить только код внутри определения класса вместо того, чтобы
править все вызовы '''
# ----------------------------------------------------------------------------------------------------------------------

# Искажение имен для безопасности
''' Python предлагает соглашения по именованию для аттрибутов, которые не должны быть видимы за пределами определения
их классов: имена начинаются с двух нижних подчеркиваний (__) '''


class Duck:
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name


print()
fow1 = Duck('Howard')
print(fow1.name)
fow1.name = 'Donald'
print(fow1.name)

# При попытке fowl.__name будет выдана ошибка 'Duck' object has no attribute '__name'
# Это согласование не делает код закрытым, но Python искажает имя для того, чтобы внешний код не наткнулся на него

# Как будет выглядить атрибут на самом деле:
print(fow1._Duck__name)
''' В консоли не появилась надпись "inside the getter". Хотя эта защита не идеальна, искаженное имя отказывется 
случайно или намеренно получать доступ к объекту.
'''
# ----------------------------------------------------------------------------------------------------------------------

# Типы методов
''' Когда вы видите начальный аргумент self в методах внутри определения класса, этот метод является методом экземпляра.
Такие методы обычно пишутся при создании собственного класса. Первый параметр метода экземпляра - это self, и Python
передает объект методу, когда вы его вызываете.

В противоположность ему, метод класса влияет на весь класс целиком. Любое изменение, которое происходит с классом, 
влияет на все его объекты. Внутри определения класса декоратор @classmethod показывает, что следующая функция 
является методом класса. Первым параметром метода также является сам класс. Согласно традиции этот параметр называется
cls, поскольку слово class является зарезервированным и не может быть использовано здесь. '''


# Определим метод класса для A, который будет подсчитывать количество созданных объектов:
class A:
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")


print()
easy_a = A()
breezy_a = A()
wheezy_a = A()
print(A.kids())

''' Мы вызвали метод A.count (атрибут класса) вместо self.count (который является атрибутом объекта). В методе kids()
мы использовали вызов cls.count, но с тем же успехом могли бы применять вызов A.count '''

''' Третий тип методов не влияет ни на классы, на ни объекты: он находится внутри класса только для удобства, вместо
того чтобы располагаться где-то отдельно. Это статический метод, перед которым располагается декоратор @staticmethod,
не имеющий в качестве начального параметра ни self, ни класс class. 
'''


class CoyoteWeapon:
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')


CoyoteWeapon.commercial()
# Не нужно создавать объект класса, чтобы получить доступ к методу
# ----------------------------------------------------------------------------------------------------------------------

# Утиная типизация (реализация полиморфизма)
# Одна операция может быть произведена над разными объектами независимо от их класса


class Quote:
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + '.'


class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'


class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'


''' Мы не меняли способ инициализации классов QuestionQuote и ExclamationQuote, поэтому не перегружали их методы 
__init__(). Далее Python автоматически вызывает метод __init__() родительского класса Quote, чтобы сохранить
переменные объекта person и words. Поэтому мы можем получить доступ к атрибуту self.words в объектах, созданных
с помощью подклассов QuestionQuote и ExclamationQuote
'''

print()
hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())

hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())

hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())

''' Три разные версии метода says() обеспечивают разное поведение трех классов. Так выглядит традиционный полиморфизм
в ООП языках. Python пошел немного дальше и позволяет вам вызывать методы who() и says() для любых объектов, 
включающих эти методы. 
'''


# Определим класс BabblingBook, который не имеет никакого отношения к охотнику и его жертвам (наследникам класса Quote):
class BabblingBook:
    def who(self):
        return 'Brook'

    def says(self):
        return 'Babble'


brook = BabblingBook()
#  Теперь запустим методы разных объектов, один из которых (brook) совершенно не связан с остальными:


def who_says(obj):
    print(obj.who(), 'says', obj.says())


print()
who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook)

''' Такое поведение иногда называется утиной типизацией благодаря старой поговорке "Если нечто выглядит как утка, 
плавает как утка и крякает как утка, то это, вероятно, утка и есть" '''
# ----------------------------------------------------------------------------------------------------------------------

# Особые методы (их имена начинаются с двойных подчеркиваний (__) и заканчиваются ими


class Word:
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.text.lower()


first = Word('ha')
second = Word('HA')
third = Word('eh')
print()

# Когда строки 'ha' и 'HA' сравниваются в нижнем регистре, они должны быть равными:
print(first.equals(second))

# Но строка 'eh' не совпадает со строкой 'ha':
print(first.equals(third))

''' Мы определили метод equals(), который выполняет преобразоване строки в нижний регистр и сравнивание. Однако было бы
здорово, если бы могли просто сказать first == second, как в случае встроенных типов Python. Реализуем такую 
возможность. Мы изменим имя метода equals() на особе имя __eq__() '''


class Word:
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()


first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first == second)
print(first == third)
# Все что было нужно - указать особое имя метода для проверки на равенство __eq__()

# Особые методы для сравнения:
'''
__eq__(self, other) ---> self == other
__ne__(self, other) ---> self != other
__lt__(self, other) ---> self < other
__gt__(self, other) ---> self > other
__le__(self, other) ---> self <= other
__ge__(self, other) ---> self >= other
'''

# Особые методы для вычислений:
'''
__add__(self, other) ---> self + other
__sub__(self, other) ---> self - other
__mul__(self, other) ---> self * other
__floordiv__(self, other) ---> self // other
__truediv__(self, other) ---> self / other
__mod__(self, other) ---> self % other
__pow__(self, other) ---> self ** other
'''

''' Не обязательно использовать математические операторы вроде * только для работы с числами. Например, строковые
объекты используют + для конкатенации и * для дуплицирования. Существует множество других методов, задокументированных
онлайн по адресу:
http://bit.ly/pydocs-smn
'''
# ----------------------------------------------------------------------------------------------------------------------

# Композиция

'''
Наследование может сослужить хорошую службу, если вам нужно создать класс-потомок, который ведет себя как родительский
класс большую часть времени (когда потом является предком). Возможность создавать иерархии наследования довольно 
заманчива, но иногда композиция или агрегирование (когда X имеет Y) имеет больше смысла.
Утка является птицей, но имеет хвост. Хвост не похож на утку, но он является частью утки. В следующем примере создадим
объекты bill и tail и предоставим их новому объекту duck
'''


class Bill:
    def __init__(self, description):
        self.description = description


class Tail:
    def __init__(self, length):
        self.length = length


class Duck:
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print('This duck has a', bill.description, 'bill and a', tail.length, 'tail')


tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()
