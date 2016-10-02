import random


class Student:
    def __init__(self, name):
        self.name = name
        self.quest = None
        self.seed = 0
        for char in self.name:
            self.seed += ord(char)

        self.seed /= len(self.name)

    def get_seed(self):
        return self.seed

    def get_name(self):
        return self.name

    def set_quest(self, size, number):
        tail = random.randint(2, 100)
        random.seed(self.seed)
        for count in range(1, tail):
            random.sample(range(1, size + 1), number)
        self.quest = random.sample(range(1, size + 1), number)
        random.seed()

    def get_quest(self, size=None, number=None):
        if self.quest is None:
            self.set_quest(size, number)

        string = ''
        for elem in self.quest:
            string += str(elem) + ', '

        string += 'и ' + str(self.quest[-1])

        print('%-11s отвечает на вопросы под номерами %s' % (self.name, string))


names = ['Баньщикова', 'Батухтин', 'Блинкова', 'Галушина', 'Каширин',
         'Королев', 'Кузьминых', 'Майнагашева', 'Сюсина', 'Терехин']

students = []
for obj in names:
    students.append(Student(obj))

print('Введите общее количество вопросов: ')
Size = int(input())
print('Введите количество вопросов в задании: ')
Num = int(input())
for obj in students:
    obj.get_quest(Size, Num)
