from tkinter import Tk, StringVar, ttk, Button
import tkinter as tk
from turtle import onkeypress


def make_button(win_obj, btn_obj):
    title = f"Button {btn_obj.id}"
    
    if btn_obj.dial:
        canvas_name = "canvas" + title
        cw_title = f"CW {btn_obj.id}"
        ccw_title = f"CCW {btn_obj.id}"
        
        btn_canvas = tk.Canvas(win_obj, width=50, height=50, background='black', name=canvas_name)
        prs_rls_btn = tk.Button(btn_canvas, width=50, height=25, text=title, command=btn_obj.press)
        ccw_btn = tk.Button(btn_canvas, height=25, width=25, text=ccw_title, command=btn_obj.ccw)
        cw_btn = tk.Button(btn_canvas,height=25,width=25,text=cw_title, command=btn_obj.cw)
        prs_rls_btn.grid(column=0,row=0)
        ccw_btn.grid(column=0,row=1)
        cw_btn.grid(column=1, row=1)
        
        return btn_canvas
        
    # else:
    #     return tk.Button(win_obj,height=50, width=50, text=title, onkeypress())

    
main = tk.Tk()
main.title("Button Set")

window = tk.Frame(main, padding="10 10 10 10")
window.grid(column=0,row=0)

btn_set = {}
for btn in list(btn_set.keys()):
    make_button(window, btn_set[btn])

feet = StringVar()
feet_entry = tk.Entry(window, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1)

meters = StringVar()
tk.Label(window, textvariable=meters).grid(column=2, row=2)

# tk.Button(window, text="Calculate", command=make_button).grid(column=3, row=3)

main.mainloop()