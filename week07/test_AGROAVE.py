import pytest
from datetime import datetime
from AGROAVE import is_empty, get_formatted_date, calculate_weigth, qr_code

def test_is_empty():
    assert is_empty('') is True
    assert is_empty('not empty') is False

def test_get_formatted_date():
    assert get_formatted_date() == datetime.now().strftime('%d/%m/%Y')
    assert get_formatted_date() == datetime.now().strftime('%d/%m/%Y')

def test_calculate_weight():
    assert calculate_weigth(10, 425) == 4250
    assert calculate_weigth(38, 425) == 16150


def test_qr_code_exception(): #I ask Chat GPT help with this test. 
    json_data = {"name": "John Doe", "email": "john@example.com"}
    file_name = "test_qr_code"

    try:
        qr_code(json_data, file_name)
    except Exception as e:
        assert str(e) == "expected error message"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])