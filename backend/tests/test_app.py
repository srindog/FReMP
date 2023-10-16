import pytest
from constants import *
from app import greeting, mongo_greeting

@pytest.mark.unit
def test_greeting():
  response = greeting()
  assert 'greeting' in response
  assert response['greeting'] == GREETING


#TODO: Split up into unit and integration
@pytest.mark.unit
def test_mongo_greeting():
  response = mongo_greeting()
  assert 'greeting' in response
  assert response['greeting'] == GREETING_FROM_MONGO