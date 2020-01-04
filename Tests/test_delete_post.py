import config
import requests


def test_delete_post():
    # deklaruje adres url postu, ktory zamierzam usunac, wraz z parametrami żądania
    url = str(config.url_posts + '/101')
    payload = {'userId': '10',
               'id': '101',
               'title': 'veni vidi vici',
               'body': 'przybylem, zobaczylem, zwyciezylem'
               }
    # usuwam post 101 i sprawdzam odpowiedź
    response_delete = requests.delete(url, data=payload)
    assert response_delete.status_code == 200 or response_delete.status_code == 204

    # odpytuje serwer o post, ktory zostal usuniety i sprawdzam, czy odpowiedz nie jest rowna 200 (sukces)
    response = requests.get(url)
    assert response.status_code != 200

test_delete_post()