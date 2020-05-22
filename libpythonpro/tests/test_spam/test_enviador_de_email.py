from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'wache2k@outlook.com',
        'wache2k@gmail.com',
        'Cursos PythonPro',
        'Primeira Turma Guido Von Rossum'
    )
    assert 'wache2k@outlook.com' in resultado
