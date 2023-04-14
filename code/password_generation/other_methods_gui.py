"""
This module prepares the other_methods_window for the user when they click the 'try other methods...' button.
"""
import tkinter
import tkinter as tk
from tkinter.font import Font
import customtkinter
import webbrowser

from password_generation import diceware_gui as diceware
from password_generation import sentence_input_gui as sentence_input


def open_link(url: str) -> None:
    """
    This function opens a given link through the webbrowser library.

    Parameters
    ----------
    url: str
        The URL to be opened.
    """
    webbrowser.open_new(url)


class CreateToolTip:
    """
    This class creates a tooltip for a given widget and text.

    tk_ToolTip_class101.py
    gives a Tkinter widget a tooltip as the mouse is above the widget
    tested with Python27 and Python34  by  vegaseat  09sep2014
    www.daniweb.com/programming/software-development/code/484591/a-tooltip-class-for-tkinter

    Modified to include a delay time by Victor Zaccardo, 25mar16
    """

    # https://stackoverflow.com/questions/3221956/how-do-i-display-tooltips-in-tkinter
    def __init__(self, widget: customtkinter.CTkLabel, text: str = 'widget info') -> None:
        self.button_hover_color = None
        self.waittime = 250  # milliseconds
        self.wraplength = 180  # pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.winfo_toplevel().bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event: tkinter.Event = None) -> None:
        """
        Called when the user hovers over the given widget,
        this function shows the tooltip.
        """
        self.schedule()

    def leave(self, event: tkinter.Event = None) -> None:
        """
        Called when the user moves out of the given widget,
        this function shows the tooltip.
        """
        self.unschedule()
        self.hidetip()

    def schedule(self) -> None:
        """
        This function cancels any previously shown tooltips,
        and defines a unique ID for a new tooltip.
        """
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self) -> None:
        """
        This function cancels any previously shown tooltips.
        """
        identification = self.id
        self.id = None
        if identification:
            self.widget.after_cancel(identification)

    def showtip(self, event: tkinter.Event = None) -> nONE:
        """
        This function creates a toplevel at the user's cursor's coordinates,
        creates a label within it,
        and removes any other window decorations.
        """
        button_border_width = 2
        button_fg_color = 'blue'
        button_hover_color = 'gray'
        button_border_color = 'black'

        x = y = 0
        x, y, cx, cy = self.widget.bbox('insert')
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = customtkinter.CTkToplevel(self.widget, fg_color=('white', '#474747'))
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = customtkinter.CTkTextbox(self.tw, corner_radius=2, border_width=2, height=65, width=190, wrap='word',
                                         font=customtkinter.CTkFont(family='Roboto', size=14))
        label.insert('1.0', self.text)
        label.configure(state='disabled')
        label.pack(ipadx=1)

        btn = customtkinter.CTkButton(self.tw, border_width=button_border_width, fg_color=button_fg_color,
                                      hover_color=button_hover_color, border_color=button_border_color,
                                      text='Wikipedia', width=50,
                                      command=lambda: open_link('https://en.wikipedia.org/wiki/Diceware'))
        btn.pack(ipadx=1)

    def hidetip(self) -> None:
        """
        This function destroys the toplevel.
        """
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()


class OtherMethodsWindow(customtkinter.CTkToplevel):
    """
    This class contains the creation of the 'other methods' Toplevel window
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.button_border_width = 2
        self.button_fg_color = 'blue'
        self.button_hover_color = 'gray'
        self.button_border_color = 'black'

        self.medium_button_font = customtkinter.CTkFont(family='Roboto', size=24)
        self.title_font = customtkinter.CTkFont(family='Roboto', size=36)

        self.window_title = 'Try other methods...'

        self.iconbitmap('textures/logo.ico')
        self.geometry('700x250')
        self.title(self.window_title)

        self.frame_title = customtkinter.CTkLabel(master=self, text='How to generate a password?',
                                                  font=self.title_font)
        self.frame_title.grid(column=0, row=0, columnspan=3)

        self.question_mark = customtkinter.CTkLabel(master=self, text='❓', font=self.title_font)
        self.question_mark.grid(column=0, row=1, sticky='e', padx=10)
        self.question_mark_ttp = CreateToolTip(self.question_mark, 'Roll 5 dice to form a 5-digit number '
                                                                   'that will be matched to a word on a list.')

        self.diceware_btn = customtkinter.CTkButton(self,
                                                    text='From the diceware wordlist',
                                                    command=self.open_diceware,
                                                    font=self.medium_button_font,
                                                    border_width=self.button_border_width,
                                                    border_color=self.button_border_color,
                                                    fg_color=self.button_fg_color,
                                                    hover_color=self.button_hover_color)
        self.diceware_btn.grid(row=1, column=1, pady=10, sticky='w')

        self.sentence_input_btn = customtkinter.CTkButton(self,
                                                          text='From a sentence',
                                                          command=self.open_sentence_input,
                                                          font=self.medium_button_font,
                                                          border_width=self.button_border_width,
                                                          border_color=self.button_border_color,
                                                          fg_color=self.button_fg_color,
                                                          hover_color=self.button_hover_color)
        self.sentence_input_btn.grid(row=1, column=2, pady=10, sticky='w')

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1, uniform='column')

        self.diceware_window = None
        self.sentence_input_window = None

        self.withdraw()
        self.after(200, self.show_icon)

    def show_icon(self) -> None:
        """
        This function shows the icon of the toplevel window.
        """
        self.deiconify()
        self.iconbitmap('textures/logo.ico')

    def open_diceware(self) -> None:
        """
        Called when the user clicks on the 'From the diceware' button,
        this function opens the diceware Toplevel window.
        """
        self.withdraw()
        if self.diceware_window is None or not self.diceware_window.winfo_exists():
            self.diceware_window = diceware.DicewareToplevel(self)
        else:
            self.diceware_window.focus()

    def open_sentence_input(self) -> None:
        """
        Called when the user clicks on the 'From a sentence' button,
        this function opens the sentence input Toplevel window.
        """
        self.withdraw()
        if self.sentence_input_window is None or not self.sentence_input_window.winfo_exists():
            self.sentence_input_window = sentence_input.SentenceInputToplevel(self)
        else:
            self.sentence_input_window.focus()
