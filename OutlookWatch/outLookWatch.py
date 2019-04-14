# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 18:04:39 2019

@author: 212744433
"""
import tkinter as tk
from tkcalendar import Calendar, DateEntry
class ExampleApp(tk.Frame):
    ''' An example application for TkInter.  Instantiate
        and call the run method to run. '''
    def __init__(self, master):
        
        tk.Frame.__init__(self,
                          master,
                          width=300,
                          height=200)
        self.master.title('Outlook Watcher')
 
        # This allows the size specification to take effect
        self.pack_propagate(0)
 
        # We'll use the flexible pack layout manager
        self.pack()
        root = tk.Tk()
        top = tk.Toplevel(root)
        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=2018, month=2, day=5)
        cal.pack(fill="both", expand=True)
        # The greeting selector
        # Use a StringVar to access the selector's value
        self.greeting_var = tk.StringVar()
        self.greeting = tk.OptionMenu(self,
                                      self.greeting_var,
                                      'hello',
                                      'goodbye',
                                      'heyo')
        self.greeting_var.set('hello')
 
        # The recipient text entry control and its StringVar
        self.recipient_var = tk.StringVar()
        self.recipient = tk.Entry(self,
                                  textvariable=self.recipient_var)
        self.recipient_var.set('world')
 
        # The go button
        self.go_button = tk.Button(self,
                                   text='Go',
                                   command=self.print_out)
 
        # Put the controls on the form
        self.go_button.pack(fill=tk.X, side=tk.BOTTOM)
        self.greeting.pack(fill=tk.X, side=tk.TOP)
        self.recipient.pack(fill=tk.X, side=tk.TOP)
 
    def print_out(self):
        ''' Print a greeting constructed
            from the selections made by
            the user. '''
        print('%s, %s!' % (self.greeting_var.get().title(),
                           self.recipient_var.get()))
    def run(self):
        ''' Run the app '''
        self.mainloop()
 
app = ExampleApp(tk.Tk())
app.run()