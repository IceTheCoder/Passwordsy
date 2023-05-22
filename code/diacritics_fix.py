"""
This module deals with remedying certain diacritics. 
"""
import tkinter

REMEDIED_CHARS = {ord(c): c for c in 'ĂăÂâÎîȘșTtȚțEeÉéÈèÊêËëIiÍíÌìÎîOoÓóÒòÔôÖöŐőUuÚúÙùÛûÜüŰűNnÑñÇçSsŚśŠšZzŽž'}


# https://stackoverflow.com/questions/75846986/certain-characters-like-%c8%9b-and-%c8%99-become-question-marks-as-i-type-them-in-a-tkin
def on_key_press(e: tkinter.Event) -> str:
    """
    This function remedies a bug that made it impossible to type certain diacritics by finding those characters in the
    input and replacing them properly.

    Returns
    -------
    str
        'break'.
    """
    char = REMEDIED_CHARS.get(e.keysym_num)
    if char:
        e.widget.insert('insert', e.char[:-1] + char)
        return 'break'
