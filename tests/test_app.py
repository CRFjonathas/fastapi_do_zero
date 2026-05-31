from fastapi.testclient import TestClient

from fastapi_do_zero.app import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'Mensagem': 'Olá, Mundo!'} 
