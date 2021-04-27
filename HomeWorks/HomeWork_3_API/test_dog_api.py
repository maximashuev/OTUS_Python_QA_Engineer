import pytest
import requests

HOST = 'https://dog.ceo/api'
LIST_ALL_BREEDS_andpoint = '/breeds/list/all'

print(HOST+LIST_ALL_BREEDS_andpoint)
def test_list_all_breeds():
    responce = requests.get(HOST+LIST_ALL_BREEDS_andpoint)
    assert responce.status_code == 200
