from tkinter import Canvas, Scale, Label, Button
# import tkinter as tk

class MyDial(Canvas):
    
    def __init__(self,controller,cw_msgs,ccw_msgs,window,*args,**kwargs):
        
        Canvas.__init__(self, window, *args, **kwargs)
        # Defining message sets
        self.cw_msgs = cw_msgs
        self.ccw_msgs = ccw_msgs
        
        #Setting controller
        self.controller = controller
        
        # Center Button
        self.center_button = Button(self,text="Press")
        self.center_button.config(width=10,height=10)

        # Column Labels
        self.cw_label = Label(self,text="cw")
        self.btn_label = Label(self, text="Button")
        self.ccw_label = Label(self,text="ccw")
        
        # Slider Creation
        self.cw_slider = Scale(self, from_=0, to=3, orient="vertical", command=self.cw_slider_event)
        self.ccw_slider = Scale(self, from_=0, to=3, orient="vertical", command=self.ccw_slider_event)

        # Setting Slider OnRelease Actions
        self.ccw_slider.bind("<ButtonRelease>",self.set_slider)
        self.cw_slider.bind("<ButtonRelease>",self.set_slider)
        
        # Positioning Widgets
        self.ccw_label.grid(row=0,column=0)
        self.btn_label.grid(row=0,column=1)
        self.cw_label.grid(row=0,column=2)
        
        self.ccw_slider.grid(row=1,column=0)
        
        self.cw_slider.grid(row=1,column=2)
        
    def cw_slider_event(self,event):
        if event == '0':
            print("Dial Off")
        elif isinstance(self.cw_msgs, list):
            self.controller.send_msg(self.cw_msgs[int(event)-1])
        else:
            print(self.cw_msgs)
            
        
    def ccw_slider_event(self,event):
        if event == '0':
            print("Dial Off")
        elif isinstance(self.ccw_msgs, list):
            self.controller.get_msg(self.ccw_msgs[int(event)-1])
        else:
            print(self.cw_msgs)
            
        
    def set_slider(self,event):
        self.ccw_slider.set(0)
        self.cw_slider.set(0)
        
    def add_btn(self,btn):
        self.center_button = btn
        self.btn_label = Label(self,text=f"cent_btn {self.center_button.id}")
        self.center_button.grid(row=1,column=1)