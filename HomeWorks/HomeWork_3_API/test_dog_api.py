import pytest
import requests
import random

HOST = 'https://dog.ceo/api'
LIST_ALL_BREEDS_endpoint = '/breeds/list/all'
RANDOM_IMAGE_endpoint = '/breeds/image/random'
IMAGES_BY_BREED_endpoint = '/breed/hound/images'
INCORRECT_endpoint = '/breeds/image/rando'
LIST_OF_BREEDS = list(dict.keys((requests.get(HOST + LIST_ALL_BREEDS_endpoint)).json().get('message')))


@pytest.mark.parametrize("endpoint", [LIST_ALL_BREEDS_endpoint, RANDOM_IMAGE_endpoint])
def test_status_code_200(endpoint):
    response = requests.get(HOST + endpoint)
    assert response.status_code == 200


@pytest.mark.parametrize('breed', LIST_OF_BREEDS)
def test_random_image_by_breeds_list(breed):
    response = requests.get(HOST + '/breed/' + breed + '/images/random')
    assert response.status_code == 200


def test_number_of_multiple_random_dog_images():
    random_number = random.choice(range(1, 51))
    response = requests.get(HOST + '/breed/' + random.choice(LIST_OF_BREEDS) + '/images/random/' + str(random_number))
    number_of_results_in_response = len(response.json().get('message'))
    assert number_of_results_in_response == random_number


def test_incorrect_endpoint_404():
    response = requests.get(HOST + INCORRECT_endpoint)
    assert response.status_code == 404


@pytest.mark.parametrize("endpoint", [LIST_ALL_BREEDS_endpoint, RANDOM_IMAGE_endpoint])
def test_status_success(endpoint):
    response = requests.get(HOST + endpoint)
    status = response.json().get('status')
    assert status == "success"
