from nose.tools import *
from app import app # import the application from app.py


app.config['TESTING'] = True
web = app.test_client() # creates a test client for the app application

def test_index():
    # URL result testing, what you will get from the server
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 404)

    # URL result testing, what you will get from the server
    rv = web.get('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Fill Out This Form", rv.data)
    
    data = {'name': 'Zed', 'greet': 'Hola'}
    # sent a POST request using the post() method. Then give it the form data as a dict
    rv = web.post('/hello', follow_redirects=True, data=data)
    # assure that the input will be the same as the output which is the data in the list
    assert_in(b"Zed", rv.data)
    assert_in(b"Hola", rv.data)