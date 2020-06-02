import pytest

from libpythonpro.libpythonpro.spam.db import Conexao


@pytest.fixture(scope='module')
def conexao():
    conexao_obj = Conexao()
    yield conexao_obj
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_conexao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()
