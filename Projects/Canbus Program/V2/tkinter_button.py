import tkinter as tk

class MyBtn(tk.Button):
    def __init__(self, button_number, press, release, *args, **kwargs):
        ''' An object that contains a set of valid can messages. 
            Each button mimics a physical switch on a controller board. 
            Added tk button gui init and functions '''
        tk.Button.__init__(self,*args,**kwargs)
        
        self.id = button_number
        self.press = press
        self.release = release
        self.cw_speeds = None
        self.ccw_speeds = None
        self.dial = False
    
    def set_dial(self,cw,ccw):
        self.dial = True
        self.cw_speeds = cw
        self.ccw_speeds = ccw
        
    def set_down(self, fn):
        self.bind('<Button-1>', fn)
    
    def set_up(self, fn):
        self.bind('<ButtonRelease-1>', fn)
        
class MainFrame(tk.Frame):
    
    def __init__(self,master,button_title,*args,**kwargs):
        tk.Frame.__init__(self,master,*args,**kwargs)
        
        self.row_grid = 1
        self.column_grid = 0
        
        for i in range(50):
            self.make_btn(button_title + " " + str(i), i)
            self.btn_num = i
            if self.row_grid==10 and self.column_grid==10:
                break
            
            else: 
                if self.column_grid == 9:
                    self.column_grid = 0
                    self.row_grid += 1
                    
                else:
                    self.column_grid += 1
    
    def make_btn(self, btn_text, index):
        btn = MyBtn(button_number="1", press="Press", release="Release", text=btn_text)
        btn.set_up(self.on_up(index))
        btn.set_down(self.on_down)
        btn.grid(row = self.row_grid, column=self.column_grid)
    
    def on_down(self, x):
        print(f"{x} Button Down")
    
    def on_up(self, x):
        print(f"{x} Button Up")

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title("My Button")
        self.geometry('500x500')
        
        MainFrame(self,button_title="Muh Butane").grid(column=0,row=0)

App().mainloop()