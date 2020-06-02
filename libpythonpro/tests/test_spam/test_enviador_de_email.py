import pytest

from libpythonpro.libpythonpro.spam.enviador_de_email import EmailInvalid, Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['wache2k@outlook.com', 'foo@bar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'wache2k@gmail.com',
        'Cursos PythonPro',
        'Primeira Turma Guido Von Rossum'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'foo']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalid):
        enviador.enviar(
            remetente,
            'wache2k@gmail.com',
            'Cursos PythonPro',
            'Primeira Turma Guido Von Rossum'
        )
