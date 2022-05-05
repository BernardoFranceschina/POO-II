from exercicio1 import Administrativo, Tecnico

class Teste:
    def main():
        tecnico = Tecnico('Bruno2', 1300, 20178080, 500)
        print('Nome:', tecnico.get_nome(), 'Matricula:', tecnico.get_matricula())
        administrativo = Administrativo('Gabriela2', 4000, 508080, 'Dia')
        print('Nome:', administrativo.get_nome(), 'Matricula:', administrativo.get_matricula())

Teste.main()