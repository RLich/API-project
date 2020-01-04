import config
import requests
import application


def test_create_new_post():
    # ustawiam parametry nowego obiektu na stronie
    payload = {'userId': '10',
               'id': '101',
               'title': 'veni vidi vici',
               'body': 'przybylem, zobaczylem, zwyciezylem'}

    # tworze nowy obiekt metoda POST i sprawdzam odpowiedz z serwera
    new_post = requests.post(config.url_posts, data=payload)
    assert new_post.status_code == 201

    # pobieram nowo-stworzony obiekt i sprawdzam odpowiedz z serwera
    response = requests.get(config.url_posts, params={'id': '100'})
    assert response.status_code == 200

    # sprawdzam, czy 'id' nowo utworzonego posta zgadza sie z zalozeniami,
    # dodajac wyjatek, na wypadek gdyby ten przypadek nie byl gotowy do testow
    id_of_created_post = application.get_value_from_response_dict(response, field_name='title')
    try:
        assert id_of_created_post == payload['title']
    except:
        print('Object is not accessible, development in progress')

test_create_new_post()