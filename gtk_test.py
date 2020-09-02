# Yes, I am copying and pasting code from somewhere else, I'm learning, deal with it
# https://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html
# ^ Source
#
# Michael Denissov 2020
#
# All this does is tests that everything is working

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()