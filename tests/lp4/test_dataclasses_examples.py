from learningpython.lp4.dataclasses_examples import (
    Person,
    ImmutablePerson,
    ComparablePerson,
    KeywordOnlyPerson,
    SlottedPerson,
    LogEntry,
    Guess,
    ComparableLogEntry,
    SharedDefault,
)
from time import sleep
import datetime


def test_person_full_name():
    person = Person("Zachary", "Lynch")
    assert person.get_full_name() == "Zachary Lynch"


def test_person_repr():
    person = Person("Zachary", "Lynch")
    assert repr(person) == "Person(first_name='Zachary', last_name='Lynch')"


def test_person_full_name_with_str_join():
    person = Person("Zachary", "Lynch")
    assert person.get_full_name_via_str_join() == "Zachary Lynch"


def test_person_equality():
    person1 = Person("Zachary", "Lynch")
    person2 = Person("Zachary", "Lynch")
    assert person1 == person2


def test_person_order():
    person1 = Person("Adam", "Cameron")
    person2 = Person("Zachary", "Lynch")
    assert person1 < person2


def test_updating_property():
    person = Person("Zachary", "Lynch")
    person.first_name = "Joe"
    assert person.get_full_name() == "Joe Lynch"


def test_cannot_update_frozen_dataclass():
    person = ImmutablePerson("Zachary", "Lynch")
    try:
        person.first_name = "Joe"
        assert False, "Expected an exception when trying to modify a frozen dataclass"
    except AttributeError:
        pass  # Expected


def test_comparable_person_order():
    person1 = ComparablePerson("Joe", "Lynch", datetime.date(2016, 8, 17))
    person2 = ComparablePerson("Zachary", "Lynch", datetime.date(2011, 3, 24))
    assert person1 < person2


def test_keyword_only_person():
    person = KeywordOnlyPerson(first_name="Zachary", last_name="Lynch")
    assert person.get_full_name() == "Zachary Lynch"


def test_keyword_only_trying_positional():
    try:
        KeywordOnlyPerson("Zachary", "Lynch")
        assert False, (
            "Expected a TypeError when trying to instantiate with positional arguments"
        )
    except TypeError:
        pass  # Expected


def test_person_adding_property():
    person = Person("Zachary", "Lynch")
    dob = datetime.date(2011, 3, 24)
    person.dob = dob

    assert person.dob == dob


def test_slotted_person_adding_property():
    try:
        person = SlottedPerson("Zachary", "Lynch")
        person.dob = datetime.date(2011, 3, 24)
        assert False, "Expected a TypeError when trying to add a property"
    except AttributeError:
        pass  # Expected


def test_field_with_default_factory():
    log_entry = LogEntry("log message")
    now = datetime.datetime.now()
    actual_delta = log_entry.timestamp - now

    permitted_delta = datetime.timedelta(seconds=1)
    assert actual_delta < permitted_delta


def test_init_non_init_field():
    try:
        Guess("cat", "dog")
    except TypeError:
        pass  # Expected


def test_comparable_field_baseline():
    cannot_compare_1 = LogEntry("same")
    sleep(1)
    cannot_compare_2 = LogEntry("same")

    assert cannot_compare_1 != cannot_compare_2


def test_comparable_field_actual():
    cannot_compare_1 = ComparableLogEntry("same")
    sleep(1)
    cannot_compare_2 = ComparableLogEntry("same")

    assert cannot_compare_1 == cannot_compare_2


def test_non_shared_default():
    l1 = SharedDefault()
    l2 = SharedDefault()

    l1.add_to_list("TEST_VALUE")

    assert l2.list_of_things == ["TEST_VALUE"]
    assert l1.list_of_things == l2.list_of_things
