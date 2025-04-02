class Person:
    def __init__(self, name, idade):
        self.name = name
        self.idade = idade


    def  pegar_nome(self):
        return self.name

    def pegar_idade(self):
        return self.idade

    def full_info(self):
        return f"{self.name} tem {self.idade} anos de idade"
