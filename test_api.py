import pytest
import json
from api import app

def test_index_route():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Testing, Flask!'

@pytest.mark.get_request
def test_get_all_books():
    response = app.test_client().get('/bookapi/books')

    res = json.loads(response.data.decode('utf-8')).get("Books")
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['author'] == 'Havard'
    assert res[1]['author'] == 'Will'
    assert response.status_code == 201
    assert type(res) is list
    
@pytest.mark.get_request
def test_get_all_books1():
    response = app.test_client().get('/bookapi/books')

    res = json.loads(response.data.decode('utf-8')).get("Books")
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['author'] == 'Havard'
    assert res[1]['author'] == 'Will'
    assert response.status_code == 200
    assert type(res) is list
    
@pytest.mark.get_request
def test_get_all_books2():
    response = app.test_client().get('/bookapi/books')

    res = json.loads(response.data.decode('utf-8')).get("Books")
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['author'] == 'Havard'
    assert res[1]['author'] == 'Will'
    assert response.status_code == 200
    assert type(res) is list

@pytest.mark.get_request
def test_get_all_books3():
    response = app.test_client().get('/bookapi/books')

    res = json.loads(response.data.decode('utf-8')).get("Books")
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['author'] == 'Havard'
    assert res[1]['author'] == 'Will'
    assert response.status_code == 200
    assert type(res) is list

@pytest.mark.get_request
def test_get_all_books4():
    response = app.test_client().get('/bookapi/books')

    res = json.loads(response.data.decode('utf-8')).get("Books")
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['author'] == 'Havard'
    assert res[1]['author'] == 'Will'
    assert response.status_code == 200
    assert type(res) is list

@pytest.mark.get_request
def test_get_all_books5():
    response = app.test_client().get('/bookapi/books')

    res = json.loads(response.data.decode('utf-8')).get("Books")
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['author'] == 'Havard'
    assert res[1]['author'] == 'Will'
    assert response.status_code == 200
    assert type(res) is list

@pytest.mark.get_request
def test_get_all_books6():
    response = app.test_client().get('/bookapi/books')

    res = json.loads(response.data.decode('utf-8')).get("Books")
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['author'] == 'Havard'
    assert res[1]['author'] == 'Will'
    assert response.status_code == 200
    assert type(res) is list
    
@pytest.mark.get_request
def test_get_all_books7():
    response = app.test_client().get('/bookapi/books')

    res = json.loads(response.data.decode('utf-8')).get("Books")
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['author'] == 'Havard'
    assert res[1]['author'] == 'Will'
    assert response.status_code == 200
    assert type(res) is list

@pytest.mark.get_request
def test_get_all_books8():
    response = app.test_client().get('/bookapi/books')

    res = json.loads(response.data.decode('utf-8')).get("Books")
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['author'] == 'Havard'
    assert res[1]['author'] == 'Will'
    assert response.status_code == 200
    assert type(res) is list

@pytest.mark.get_request
def test_get_book_by_id():
    response = app.test_client().get('/bookapi/books/1')
    res = json.loads(response.data.decode('utf-8')).get("Book")
    print(res)
    assert res['id'] == 1
    assert res['author'] == 'Havard'
    assert res['title'] == 'CS50'
    assert response.status_code == 200
