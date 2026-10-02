from app import app

def test_inicio_status_code():
    cliente = app.test_client()
    resposta = cliente.get("/")

    assert resposta.status_code == 200

def test_inicio_message():
    cliente = app.test_client()
    resposta = cliente.get("/")

    assert resposta.get_data(as_text=True) == "Sistema de Gerenciamento Escolar"
