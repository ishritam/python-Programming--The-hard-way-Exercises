import codecal
import pytest
import sys
@pytest.mark.skipif(sys.version_info > (3,5),reason="I don't wanna test add fun.")
def test_add():
	total= codecal.add(10,20)
	assert total==30
	
def test_sub():
	total= codecal.sub(6,3)
	assert total ==3
	
	
def test_mult():
	total = codecal.mult(5,5)
	assert total==25
	
	
	
# import codecal
# import pytest

# @pytest.mark.simple
# def test_add():
	# total= codecal.add(10,20)
	# assert total==30
# @pytest.mark.simple	
# def test_sub():
	# total= codecal.sub(6,3)
	# assert total ==3
	
# @pytest.mark.product	
# def test_mult():
	# total = codecal.mult(5,5)
	# assert total==25