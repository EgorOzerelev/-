import os
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    test_client = app.test_client()

    # Удалим responses.txt перед тестом (если есть)
    #if os.path.exists("responses.txt"):
    #   os.remove("responses.txt")

    yield test_client

    # Очистим после теста
    if os.path.exists("responses.txt"):
        os.remove("responses.txt")


def test_get_form(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "Пожалуйста, заполните анкету" in response.get_data(as_text=True)


def test_post_form(client):
    data = {
        "name": "Иван",
        "age": "30",
        "favorite_color": "синий"
    }
    response = client.post('/', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert "Спасибо за заполнение анкеты" in response.get_data(as_text=True)

    with open('responses.txt', encoding='utf-8') as f:
        content = f.read()
        assert "Иван" in content
        assert "30" in content
        assert "синий" in content