import requests
import config


def test_load_comments_in_post_13():
    # laduje wszystkie komentarze pod postem nr 13 i sprawdzam odpowiedz z serwera
    payload = {'postId': '13'}
    response = requests.get(config.url_comments, params=payload)
    assert response.status_code == 200

    # ustawiam licznik komentarzy
    comments_counter = 0

    # iteruje wszystkie komentarze, zliczajac je po wystapieniu pola 'id'
    for record in response.json():
        if 'id' in record:
            comments_counter = comments_counter + 1

    # sprawdzam, czy liczba komentarzy rowna jest 5
    assert comments_counter == 5


test_load_comments_in_post_13()