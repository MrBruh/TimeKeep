# see gtk_test.py for sources
# Michael Denissov 2020
#
# playing around with widgets, seeing how to use them.

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.label = Gtk.Label(label="Hello World", angle=25, halign=Gtk.Align.END)

        # OK so there's a tutorial on this later, so imma just leave it here
        self.button = Gtk.Button(label=self.label)
        self.button.connect("clicked", self.on_button_clicked)

        # Wow, this prints a lot
        print(dir(self.button.props))

        # Wasn't in the tutorial, but I think this is a neat way of doing things, if it worked
        #self.button.label = self.label

        self.add(self.button)


    def on_button_clicked(self, widget):
        print("Hello World")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()