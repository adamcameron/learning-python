import datetime
import textwrap


class SomeClass:
    def __str__(self):
        return "Some string"


def join_strings(s1: str, s2: str):
    return f"{s1} {s2}"


def join_strings_variadic(*args: str):
    return " ".join(args)


def returns_ascii_letters():
    import string

    return string.ascii_letters


def iterate_string(s: str):
    for char in s:
        print(char)


def iterate_string_with_indexes(s: str):
    result = ""
    for index, char in enumerate(s):
        result += f"{index}{char}"
    return result


def returns_compound_string_literal():
    return "tahi" "rua" "toru" "whā"  # fmt: skip


def get_char_at_index(s: str, index: int):
    return s[index]


def returns_triple_quoted_string():
    with_indentation = """
    multi
    line
    string
    """

    without_indentation = textwrap.dedent(with_indentation)

    return with_indentation, without_indentation


def messes_up_capitalisation(s: str):
    return s.capitalize()


def expand_tabs(s: str, tabsize: int):
    return s.expandtabs(tabsize)


def format_datetime_as_iso_date_time(d: "datetime.datetime"):
    return "{:%Y-%m-%d %H:%M:%S}".format(d)


def greet(first_name: str, last_name: str) -> str:
    return f"G'day, {first_name} {last_name}!"


def substring_with_array_notation(s: str, start: int, end: int) -> str:
    return s[start:end]
