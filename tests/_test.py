import pytest
#from app import app
import app

def test_home():
    #client = app.test_client()
    text = app.home()
    assert 'Home' in text

def test_home_tofail():
    #client = app.test_client()
    text = app.home()
    assert 'abs' in text

#sudo docker-compose exec api  python -m pytest "tests"