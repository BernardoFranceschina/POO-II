class Gerente:
    pass

class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    def exibeDados(self):
        print('\nNome: ', self.get_nome(), '\nSalário: ', self.get_salario())

    def get_nome(self):
        return self.__nome

    def get_salario(self):
        return self.__salario

class Assistente(Funcionario):
    def  __init__(self, nome, salario, matricula):
        super().__init__(nome, salario)
        self.__matricula = matricula

    def exibeDados(self):
        print('\nNome:', self.get_nome(), '\nSalário:', self.get_salario(), '\nMatrícula:', self.get_matricula())

    def get_matricula(self):
        return self.__matricula

class Tecnico(Assistente):
    def __init__(self, nome, salario, matricula, bonus):
        super().__init__(nome, salario, matricula)
        self.__bonus = bonus

    def exibeDados(self):
        print('\nNome:', self.get_nome(), '\nMatrícula:', self.get_matricula(), '\nSalário:', self.get_salario(), 'Bonus:', self.__bonus, 'Total:', self.get_salario()+self.__bonus)

class Administrativo(Assistente):
    def __init__(self, nome, salario, matricula, turno):
        super().__init__(nome, salario, matricula)
        self.__turno = turno
        self.__turnoAdicional = 'Noturno'

    def exibeDados(self):
        print('\nNome:', self.get_nome(), '\nSalário:', self.get_salario(), '\nMatrícula:', self.get_matricula(), '\nTurno:', self.__turno, '\nTurno adicional:', self.__turnoAdicional)

# funcionario = Funcionario('Bernardo', 1200)
# funcionario.exibeDados()
#
# assistente = Assistente('Fernanda', 1500, 20203080)
# assistente.exibeDados()
#
# tecnico = Tecnico('Bruno', 1300, 20178080, 500)
# tecnico.exibeDados()
#
# administrativo = Administrativo('Gabriela', 4000, 508080, 'Dia')
# administrativo.exibeDados()
