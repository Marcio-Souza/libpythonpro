from libpythonpro.libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.libpythonpro.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'wache2k@gmail.com',
        'Curso Python Pro',
        'Confira os módulos dos cursos'
    )
