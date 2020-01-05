import requests
import config
import random
import application


def test_load_one_comment_in_post_13():
    # podaje parametry do strzalu majacego zwrocic liste wszystkich 'id' komentarzy na stronie
    # po czym wybieram losowy 'id', wedle ktorego laduje jeden komentarz
    entry_payload = {'postId': '13'}
    entry_response = requests.get(config.url_comments, params=entry_payload)
    field_name = 'id'
    random_comment_id = random.choice(application.get_field_values(entry_response, field_name))

    # laduje komentarz wedle wybranego losowo 'id', sprawdzam odpowiedz z serwera
    payload = {'id': random_comment_id}
    response = requests.get(config.url_comments, params=payload)
    assert response.status_code == 200

    # tworze liste pol do asercji
    list_of_fields_to_check = ['postId', 'id', 'email', 'body']

    # iteruje liste po polach, dla ktorych zwracam wartosc i sprawdzam, czy na pewno jest niepusta
    for field in list_of_fields_to_check:
        field_value = application.get_value_from_response_dict(response, field)
        print(field_value)
        assert application.check_if_field_is_not_empty(field_value)


test_load_one_comment_in_post_13()