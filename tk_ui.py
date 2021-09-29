import tkinter
from tkinter import font, messagebox
from gettext import gettext as _

from generator import generate
from utility import LoggerTimer, _config

LANG = _config["config"]["language"]["available"]
HEIGHT, WIDTH, HEAD_HEIGHT = (
    _config["config"]["window"]["height"],
    _config["config"]["window"]["width"],
    _config["config"]["window"]["head_width"],
)
CONFIG_FILE = "config/config.json"


class GeneratorUI:
    """ """

    def __init__(self):
        # position
        self.x, self.y, self.length = 5, 20, 10
        # config root window
        self.window = tkinter.Tk()
        self.window.option_add("*tearOff", tkinter.FALSE)
        self.window.resizable(False, False)
        self.window.title(_("Password Generator"))
        self.window.wm_title(_("Password Generator"))
        self.window.minsize(WIDTH, HEIGHT)
        self.window.protocol("WM_DELETE_WINDOW", self.window.destroy)
        self.window.iconphoto(
            True, tkinter.PhotoImage(name="icon", file="./favicon.png")
        )
        # config font
        self.highlightFont = font.Font(
            family="Times", name="appHighlightFont", size=15, weight="bold"
        )
        self.textFont = font.Font(family="Times", name="textFont", size=13)
        # config menu
        self.menubar = tkinter.Menu(self.window)
        self.window["menu"] = self.menubar
        self.menu_file = tkinter.Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_file, label=_("File"))
        self.menu_file.add_command(command=self.exit, label=_("Quit"))
        # first frame
        self.frame_1 = tkinter.Frame(
            self.window, width=WIDTH, height=HEAD_HEIGHT, bg="lightblue"
        )
        self.frame_1.pack(side=tkinter.TOP, expand=True, fill=tkinter.BOTH)
        tkinter.Label(
            self.frame_1,
            text=_("Enter the password length"),
            font=self.highlightFont,
            bg="lightblue",
        ).grid(row=0, column=0, columnspan=4, pady=10)
        self.text_field = tkinter.Entry(self.frame_1, width=20)
        self.text_field.focus_get()
        self.text_field.grid(row=1, column=0, padx=10)
        self.valid_btn = tkinter.Button(
            self.frame_1, text=_("OK"), command=self.generate, width=5
        )
        self.valid_btn.grid(row=1, column=1, padx=10)
        # text on canvas
        # second frame
        self.frame_2 = tkinter.Frame(
            self.window, width=WIDTH, height=HEIGHT - HEAD_HEIGHT
        )
        self.frame_2.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)
        self.canvas = tkinter.Canvas(
            self.frame_2,
            width=WIDTH,
            height=HEIGHT - HEAD_HEIGHT,
            bg="white",
            scrollregion=(0, 0, 0, 0),
        )
        self.text = tkinter.Text(self.canvas, width=10, height=5, font=self.textFont)

        self.text.pack(fill=tkinter.BOTH, side=tkinter.TOP, expand=True)
        self.scroll_h = tkinter.Scrollbar(
            self.frame_2, command=self.canvas.xview, orient=tkinter.HORIZONTAL
        )
        self.scroll_h.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.scroll_h["command"] = self.canvas.xview
        self.canvas.pack(fill=tkinter.BOTH, side=tkinter.TOP, expand=True)
        # command
        self.valid_btn.bind("<Return>", self.generate)
        self.window.bind_all("<Cancel>", self.exit)
        # launch window
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.mainloop()

    def exit(self):
        """ """
        self.window.quit()

    def generate(self):
        """ """
        self.clear_content()
        self.length = self.text_field.get() or 10
        try:
            self.length = int(self.length)
            password = generate(self.length)
            # self.config_scroll(line=10 * len(password), column=20)
            self.text.insert("end", password)
        except Exception as ex:
            self.text.insert("end", ex.__str__())

    def clear_content(self):
        """
        Clear the canvas (the white)
        """
        self.canvas.delete(tkinter.ALL)
        self.text.delete(1.0, 2.0)
        self._y = 17

    def config_scroll(self, line=0, column=0):
        """
        Configure the scrollbar
        """
        self._caneva.config(scrollregion=(0, 0, column, line))

    def _show_license(self):
        """ """
        messagebox.showinfo(title=_("Licence"), message=_("Licence M.I.T"))


if __name__ == "__main__":
    GeneratorUI()
