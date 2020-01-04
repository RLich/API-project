import json


# majac dany dictionary, zwracam wszystkie wartosci dla danego pola, jakie w nim wystepuja, w formie listy
def get_field_values(response, field_name):
    response_dict = json.loads(response.text)
    field_values = []
    for field in response_dict:
        field_values.append(field[field_name])
    return field_values


# majac dany dictionary, zwracam wybrana wartosc w formie string
def get_value_from_response_dict(response, field_name):
    response_dict = json.loads(response.text)
    for record in response_dict:
        return str(record[field_name])


# sprawdzam, czy dana wartosc jest stringiem, po czym sprawdzam, czy sklada sie ona z zerowej ilosci znakow
def check_if_field_is_not_empty(field_value):
    assert isinstance(field_value, str)
    if len(field_value) == 0:
        return False
    else:
        return True
