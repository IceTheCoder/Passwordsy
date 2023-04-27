"""
..
"""
REMEDIED_CHARS = {ord(c): c for c in 'ĂăÂâÎîȘșTtȚțEeÉéÈèÊêËëIiÍíÌìÎîOoÓóÒòÔôÖöŐőUuÚúÙùÛûÜüŰűNnÑñÇçSsŚśŠšZzŽž'}


def on_key_press(e):
    """
    ...
    """
    char = REMEDIED_CHARS.get(e.keysym_num)
    if char:
        e.widget.insert('insert', e.char[:-1] + char)
        return 'break'

