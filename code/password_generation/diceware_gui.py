import tkinter as tk

import password_generation.diceware_logic as logic


def create_diceware_frame(frame):
    roll_dice_button = tk.Button(frame, text='Roll dice',
                                 command=lambda: display_words(logic.roll_dice(int(input_box.get()))))
    roll_dice_button.grid(row=0, column=0)

    input_box = tk.Entry(frame)
    input_box.grid(row=1, column=0, pady=10)

    pair_widget = tk.Text(frame)
    pair_widget.grid(row=2, column=0)

    def display_words(pair):
        pair_widget.configure(state='normal')
        pair_widget.delete('1.0', 'end')
        pair_widget.insert('1.0', str(pair))
        pair_widget.configure(state='disabled')
