# CButton.py

from graphics import *
from math import sqrt


class CButton:

    """A button is a labeled circle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods respectively. The clicked(p)
    method returns True if the button is active and p is
    inside it."""

    def __init__(self, win, center, radius, label):
        """ Creates a circle button, eg:
        cb = CButton(myWin, center, radius, 'Quit') """

        self.center = center
        self.radius = radius
        self.circle = Circle(self.center, self.radius)
        self.circle.setFill('lightgrey')
        self.circle.draw(win)
        self.label = Text(self.center, label)
        self.label.draw(win)
        self.deactivate()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.circle.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.circle.setWidth(1)
        self.active = False

    def clicked(self, p):
        "Returns True if button is active and p is inside."
        x = self.center.getX()
        y = self.center.getY()
        distance = sqrt((x+p.getX())**2 + (y+p.getY())**2)
        return (self.active and (distance<=self.radius))

win = GraphWin()
cir = CButton(win, Point(100,100), 20, "SHIT!")
cir.activate()
pt = win.getMouse()

print(cir.clicked(pt))

