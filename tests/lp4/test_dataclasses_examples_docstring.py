from learningpython.lp4.dataclasses_examples import Person
import pydoc


def get_test_person():
    return Person("Zachary", "Lynch")


def test_class_doc_string():
    z = get_test_person()

    help_text = z.__doc__

    assert "A person with a first and last name." in help_text


def test_method_doc_string():
    z = get_test_person()

    help_text = z.get_full_name.__doc__

    assert "Returns the full name of the person." in help_text


def test_doc_string_straight_from_class():
    help_text = pydoc.render_doc(Person)

    assert "A person with a first and last name." in help_text
    assert "Returns the full name of the person." in help_text


def test_doc_string_straight_from_class_method():
    help_text = pydoc.render_doc(Person.get_full_name)

    assert "Returns the full name of the person." in help_text
