# class One:
#     def __init__(self,marka,model,god_v,price):
#         self.marka = marka
#         self.model = model
#         self.god_v = god_v
#         self.price = price
#     def result(self):
#         print(f'this is mark of the car:,{self.marka}'
#         f'Model:{self.god_v}'
#         f'God vipusk:{self.god_v}'
#         f'Tsena:{self.price}')
# class Second(One):
#     def __init__(self, marka, model, god_v, price):
#         super().__init__(marka, model, god_v, price)        
# car = Second("mers","gt63","2020","150000$")
# class Third(One):
#     def __init__(self, marka, model, god_v, price):
#         super().__init__(marka, model, god_v, price)
# car1 = Third('tracks','ford','2023','15000$')
# car.result()
# car1.result()








# class Animal:
#     def __init__(self):
#         self.name = ''
#         self.sound = ''
#         self.__species = ''
#     def set_name(self,name):
#         self.name = name
    
#     def set_sound(self,sound):
#         self.sound = sound
    
#     def set_species(self,species):
#         self.__species = species
        
#     def get_name(self):
#         return self.name
    
#     def get_sound(self):
#         return self.sound
    
#     def get_species(self):
#         return self.__species
        
# dog = Animal()
# dog.set_name('Messi')
# dog.set_sound('Громкий')
# dog.set_species('Низкий но белый')

# print(f'Name: {dog.get_name()}'
#       f'Sound: {dog.get_sound()}'
#       f'Species: {dog.get_species()}')






input('Здраствуйте вы попали на телешоу угадай палиндром или нет, представтесь пожалуйста: ')
input('Хорошо вы готовы ответить на вопросы?: ')
a = input('Первый вопрос цифра 123321 будет полиндромом?: ')
if a == 'да':
    print('Хорошо у вас первый балл.')
else:
    print('Не правильно без баллов дальше.')
    pass
b = input('Имя азиза является полиндромом?: ')
if b == 'да':
    print('Правильно вы победили.')
else:
    print('К сожелению вы проиграл.')