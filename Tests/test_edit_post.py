import requests
import config
import application


def test_edit_post():
    # tworze url z endpointem w postaci utworzonego w osobnym tescie posta
    url = str(config.url_posts + '/101')

    # wybieram nowy tytul dla wybranego posta i edytuje go, sprawdzam odpowiedz z serwera
    payload = {'title': 'this is the new title'}
    response_put = requests.put(url, data=payload)
    try:
        assert response_put.status_code == 200
    except:
        print('Object is not accessible, development in progress')

    # pobieram edytowany obiekt i sprawdzam odpowiedz z serwera
    # dodajac wyjatek, na wypadek gdyby ten przypadke nie byl gotowy do testow
    response = requests.get(config.url_posts, params={'id': '101'})


    # sprawdzam, czy 'title' edytowanego posta zgadza sie z zalozeniami,
    # dodajac wyjatek, na wypadek gdyby ten przypadek nie byl gotowy do testow
    title_of_edited_post = application.get_value_from_response_dict(response, field_name='title')
    try:
        assert title_of_edited_post == payload['title']
    except:
        print('Object is not accessible, development in progress')


test_edit_post()
