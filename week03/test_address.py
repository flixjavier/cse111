from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
  assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
  assert extract_city("4504 Main, New York, New York 33700") == "New York"
  assert extract_city("703 Jesus-Urueta, Nuevo Casas Grandes, Chihuahua 31710") == "Nuevo Casas Grandes"
  assert extract_city("202 Corona, Camargo, Chihuahua 33700") == "Camargo"
  

def test_extract_state():
  assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
  assert extract_state("202 Corona, Camargo, Chihuahua 33700") == "Chihuahua"
  assert extract_state("703 Jesus-Urueta, Nuevo Casas Grandes, Chihuahua 31710") == "Chihuahua"
  assert extract_state("4504 Main, New York, New York 33700") == "New York"

def test_extract_zipcode():
  assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
  assert extract_zipcode("202 Corona, Camargo, Chihuahua 33700") == "33700"
  assert extract_zipcode("703 Jesus-Urueta, Nuevo Casas Grandes, Chihuahua 31710") == "31710"
  assert extract_zipcode("4504 Main, New York, New York 45532") == "45532"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])