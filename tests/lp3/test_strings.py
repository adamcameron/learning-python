from learningpython.lp3 import strings
from learningpython.lp3.strings import SomeClass


def test_join_strings():
    result = strings.join_strings("Hello", "world")
    assert result == "Hello world"


def test_join_strings_using_numbers():
    result = strings.join_strings(123, 456)  # type: ignore[error-code]
    assert result == "123 456"


def test_join_strings_using_booleans():
    result = strings.join_strings(True, False)  # type: ignore[error-code]
    assert result == "True False"


def test_join_strings_using_none():
    result = strings.join_strings(None, None)  # type: ignore[error-code]
    assert result == "None None"


def test_join_strings_variadic():
    result = strings.join_strings_variadic("Hello", "from", "variadic", "function")
    assert result == "Hello from variadic function"


def test_string_ascii_letters():
    result = strings.returns_ascii_letters()
    assert result == "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def test_iterate_string(capsys):
    strings.iterate_string("abc")
    captured = capsys.readouterr()
    assert captured.out == "a\nb\nc\n"


def test_iterate_string_with_indexes():
    result = strings.iterate_string_with_indexes("abc")
    assert result == "0a1b2c"


def test_returns_compound_string_literal():
    result = strings.returns_compound_string_literal()
    assert result == "tahiruatoruwhā"


def test_char_at_index():
    result = strings.get_char_at_index("test string", 7)
    assert result == "r"


def test_returns_triple_quoted_string():
    with_indentation, without_indentation = strings.returns_triple_quoted_string()

    print("[", with_indentation, " ]")
    print("[", "\n    multi\n    line\n    string\n    ", " ]")
    assert with_indentation == "\n    multi\n    line\n    string\n    "


def test_class___string___method():
    obj = SomeClass()
    result = str(obj)
    assert result == "Some string"


def test_capitalize_string():
    capitalized = strings.messes_up_capitalisation(
        "the Guardian would be proud^h^h^h^h^hdisappointed with you"
    )
    assert (
        capitalized == "The guardian would be proud^h^h^h^h^hdisappointed with you"
    )  # note the lowercase 'g'


def test_expand_tabs():
    s = "tahi\trua\ttoru\twhā"
    expanded = strings.expand_tabs(s, 4)
    assert expanded == "tahi    rua toru    whā"  # note it respects tab stops


def test_using_format_with_datetime():
    from datetime import datetime

    z_day = datetime(2011, 3, 24, 9, 2, 0)
    as_iso_date_time = strings.format_datetime_as_iso_date_time(z_day)

    assert as_iso_date_time == "2011-03-24 09:02:00"


def test_f_string():
    greeting = strings.greet("Zachary", "Lynch")

    assert greeting == "G'day, Zachary Lynch!"


def test_substring_with_array_notation():
    result = strings.substring_with_array_notation(
        "tahi rua toru whā", 9, 13
    )  # python's off-by-one upper bound in action
    assert result == "toru"
