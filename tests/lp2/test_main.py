from learningpython.lp2.main import greet


def test_greet(capsys):
    greet()
    captured = capsys.readouterr()
    assert captured.out == "Hello from learning-python!\n"
