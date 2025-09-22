from learningpython.lp4.getattr import *

def test_full_name():
	z = Person("zachary", "lynch")

	assert z.full_name == "Zachary Lynch"

def test_unhandled_attribute():
	z = Person("zachary", "lynch")
	try:
		z.not_an_attribute
		assert False, "Expected an AttributeException"
	except AttributeError:
		pass  # Expected	
