from tkinter import Text
from idlelib.redirector import WidgetRedirector


class ReadOnlyText(Text):
    def __init__(self, *args, **kwargs):
        Text.__init__(self, *args, **kwargs)
        self.redirector = WidgetRedirector(self)
        self.insert = self.redirector.register("insert", lambda *args, **kwargs: "break")
        self.delete = self.redirector.register("delete", lambda *args, **kwargs: "break")
