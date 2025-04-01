#APRENDENDO A CRIAR CLASSES

# class Person:
#     nome = ""
#     idade = 0

#     def get_info(self):
#         print(f"Nome: {self.nome}, idade: {self.idade}")

# p = Person()
# p.nome = 'Gio'
# p.idade = 19

# p.get_info()

# class Animais:
#     raca = ''
#     peso = 0.0
#     idade = 0

#     def get_indo(self) :
#         print(f"O cachorro é da raça {self.raca}, tem o peso: {self.peso}, e sua idade é: {self.idade}")

# p= Animais()
# p.raca = "vira-lata"
# p.peso = 2.5
# p.idade = 2

# p.get_indo()

# Criando uma classe Person
class Person:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def get_info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

p = Person("Giovanna", 20)
p.get_info()

# Criando uma classe Animal
class Animal:
    def __init__(self, raca="", peso=0.0):
        self.raca = raca
        self.peso = peso

    def get_tipo(self):
        print(f"Raça: {self.raca}, Peso: {self.peso}")

a = Animal("Cachorro", 5.8)
a.get_tipo()

# Criando uma classe Aluno
class Aluno:
    def __init__(self, nome="", curso="", matricula=""):
        self.nome = nome
        self.curso = curso
        self.matricula = matricula

    def get_matricula(self):
        print(f"Nome: {self.nome}, Curso: {self.curso}, Matrícula: {self.matricula}")

aluno = Aluno("Giovanna", "Eng. Software", "230009888")
aluno.get_matricula()

# Criando uma classe Person com __str__
class Person:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos"

p = Person("Giovanna", 20)
print(p)

# Herança corrigida
class Person:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def display_info(self):
        print(f"Nome: {self.nome}, tem {self.idade} anos")

# Classe Student herdando de Person
class Student(Person):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def display_info(self):  # Corrigindo erro de digitação
        print(f"{self.nome} tem {self.idade} anos e sua matrícula é: {self.matricula}")

p = Person("Giovanna", 20)
p.display_info()

s = Student("Yasmin", 20, "22233445")
s.display_info()
