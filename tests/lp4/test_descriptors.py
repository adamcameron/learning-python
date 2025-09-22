from learningpython.lp4.descriptors import *

def test_person_values():
	z = Person("zachary", "lynch")

	assert z.first_name == "Zachary"
	assert z.last_name == "Lynch"
	assert z.get_full_name() == "Zachary Lynch"