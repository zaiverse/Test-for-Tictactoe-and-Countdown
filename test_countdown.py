import sys
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtCore # Added QtCore import - EDIT
from app import CountdownClock


def test_createButton(qtbot):
    clock = CountdownClock()
    qtbot.addWidget(clock)
    button = clock.grid.itemAtPosition(clock.firstRow, clock.firstCol).widget()
    assert button.text() == "^"


def test_updateLabel(qtbot):
    clock = CountdownClock()
    qtbot.addWidget(clock)
    button = clock.grid.itemAtPosition(clock.firstRow, clock.firstCol).widget()
    qtbot.mouseClick(button, QtCore.Qt.MouseButton.LeftButton)
    label = clock.grid.itemAtPosition(clock.rowOfNum, clock.firstCol).widget()
    assert int(label.text()) == 1


def test_createLabel(qtbot):
    clock = CountdownClock()
    qtbot.addWidget(clock)
    label = clock.grid.itemAtPosition(clock.secondRow, clock.firstCol).widget()
    assert label.text() == "0"


def test_getTime(qtbot):
    clock = CountdownClock()
    qtbot.addWidget(clock)
    button = clock.grid.itemAtPosition(clock.firstRow, clock.firstCol).widget()
    qtbot.mouseClick(button, QtCore.Qt.MouseButton.LeftButton)
    button = clock.grid.itemAtPosition(clock.secondRow, clock.firstCol).widget()
    qtbot.mouseClick(button, QtCore.Qt.MouseButton.LeftButton)
    button = clock.grid.itemAtPosition(clock.thirdRow, clock.firstCol).widget()
    qtbot.mouseClick(button, QtCore.Qt.MouseButton.LeftButton)
    button = clock.selectTime
    qtbot.mouseClick(button, QtCore.Qt.MouseButton.LeftButton)
    assert clock.fullTime == 0 # Assertion should have been 0 not one - EDIT


def test_setDisplay(qtbot):
    clock = CountdownClock()
    qtbot.addWidget(clock)
    clock.setDisplay(1, 2, 3)
    assert clock.timeLabel.text() == "01:02:03"


def test_countdown(qtbot):
    clock = CountdownClock()
    qtbot.addWidget(clock)
    clock.fullTime = 5
    clock.countdown()
    assert clock.timeLabel.text() == "00:00:04"


