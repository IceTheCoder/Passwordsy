"""
This module deals with remedying certain diacritics. 
"""
import tkinter

REMEDIED_CHARS = {ord(c): c for c in 'ĂăÂâÎîȘșTtȚțEeÉéÈèÊêËëIiÍíÌìÎîOoÓóÒòÔôÖöŐőUuÚúÙùÛûÜüŰűNnÑñÇçSsŚśŠšZzŽž'}


def on_key_press(e: tkinter.Event):
    """
    ...
    """
    char = REMEDIED_CHARS.get(e.keysym_num)
    if char:
        e.widget.insert('insert', e.char[:-1] + char)
        return 'break'

