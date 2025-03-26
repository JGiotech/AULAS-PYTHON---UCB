class Person:
    nome = ""
    idade = 0

    def get_info(self):
        print(f"Nome: {self.nome}, idade: {self.idade}")

p = Person()
p.nome = 'Gio'
p.idade = 19

p.get_info()

