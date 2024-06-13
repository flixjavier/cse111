from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
  full_name = make_full_name("Sally", "Brown")
  assert isinstance(full_name, str), "Is a string"
  assert make_full_name("Sally", "Brown") == "Brown; Sally"
  assert make_full_name("Felix", "Flores") == "Flores; Felix"
  assert make_full_name("John", "Doe") == "Doe; John"
  assert make_full_name("", "") == "; "
  assert make_full_name("F", "F") == "F; F"
  assert make_full_name("S", "B") == "B; S"

def test_extract_family_name():
  assert extract_family_name("Brown; Sally") == "Brown"
  assert extract_family_name("Flores; Felix") == "Flores"
  assert extract_family_name("Doe; John") == "Doe"
  assert extract_family_name("; ") == ""
  assert extract_family_name("F; F") == "F"
  assert extract_family_name("B; S") == "B"

def test_extract_given_name():
  assert extract_given_name("Brown; Sally") == "Sally"
  assert extract_given_name("Flores; Felix") == "Felix"
  assert extract_given_name("Doe; John") == "John"
  assert extract_given_name("; ") == ""
  assert extract_given_name("F; F") == "F"
  assert extract_given_name("B; S") == "S"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])