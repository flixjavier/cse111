from sample import water_column_height
from pytest import approx
import pytest

def test_water_column_height():
  assert water_column_height(0.0, 0.0) == approx(0.0)
  assert water_column_height(0.0, 10.0) == approx(7.5)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])