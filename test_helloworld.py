import pytest

from PyQt6 import QtCore

import helloword


@pytest.fixture
def app(qtbot):
    test_hello_app = helloword.MyApp()
    qtbot.addWidget(test_hello_app)

    return test_hello_app


def test_label(app):
    print("helloworld")
    assert app.text_label.text() == "Hello World!"



# def test_label_after_click(app, qtbot):
#     qtbot.mouseClick(app.button, QtCore.Qt.LeftButton)
#     assert app.text_label.text() == "Changed!"
