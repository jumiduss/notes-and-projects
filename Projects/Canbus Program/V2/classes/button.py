from tkinter import Button

class MyButton(Button):
    def __init__(self, controller, button_number, press, release, root, *args, **kwargs):
        ''' An object that contains a set of valid can messages. 
            Each button mimics a physical switch on a controller board. '''
        
        self.id = button_number
        self.press = press
        self.release = release
        
        #Setting controller
        self.controller = controller
        
        # Tkinter Button Setup
        Button.__init__(self,root,*args,**kwargs)
        if isinstance(self.press,str) and isinstance(self.release,str):
            self.config(bg="black")
        elif isinstance(self.release,str):
            self.config(bg="silver")
        
        self.config(text=self.id,width=5,height=5)
        self.bind("<ButtonPress>",self.send_msg)
        self.bind("<ButtonRelease>",self.send_msg)

    def send_msg(self,event):
        if event.state < 100:
            msg = self.press
            on_off = True
        else:
            msg = self.release
            on_off = False
        
        if isinstance(msg,str):
            print(msg)
            print(on_off)
        else:    
            can_msg = self.controller.send_msg(msg)
        
        return can_msg