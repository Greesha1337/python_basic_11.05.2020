import random

class Homo:
    _height = 0.3
    _weight = 3.2
    __age = 0


    def __init__(self, sex, hair_color):
        self.sex = sex
        self.hair_color = hair_color

    def say(self):
        print(f'EUWRHSAASAS {self.__age}')


class Neander:
    def __init__(self, hunt):
        self.hunt = hunt

    def say(self):
        print('AUUUUUUGGGGGHHHH')


class HomoSap(Homo):

    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)

    def say(self):
        print(f'IM HOMO SAPIENCE, my name is {self.name}')


class SapSap(HomoSap, Neander):
    def __init__(self, body_color, hunt, *args, **kwargs):
        self.body_color = body_color
        HomoSap.__init__(self, *args, **kwargs)
        Neander.__init__(self, hunt)
        Neander.say(self)


adam = SapSap('white', True, 'IGOR', 'M', hair_color='RED')
print(1)