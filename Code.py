from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self,root):
        self.root=root
        self.root.title('To-Do List')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root,text='To-Do List',
                font='airel, 25 bold',width=10,bd=5, bg='light blue',fg='black' )
        self.label.pack(side='top',fill=BOTH)

        self.label2 = Label(self.root,text='Enter Your Task',font='arial, 18 bold',
                            width=13,bd=4,bg='dark blue',fg='white')
        self.label2.place(x=30,y=60)    

        self.label3 = Label(self.root,text='TASK',font='arial, 18 bold',
                            width=7,bd=4,fg='black')
        self.label3.place(x=400,y=54)

        self.main_text=Listbox(self.root,height=9,bd=5,width=23,font='ariel, 20 italic bold')
        self.main_text.place(x=280,y=95)

        self.text=Text(self.root,bd=5,height=2,width=20,font='arial, 15 bold')
        self.text.place(x=20,y=120)
        
        #===================== Add Task ========================#

        def add():
            content = self.text.get(1.0, END).strip()
            if content:  # Ensure content is not empty
                self.main_text.insert(END, content)
                with open('tasks.txt', 'a') as file:  # Append mode
                    file.write(content + '\n')
                self.text.delete(1.0, END)

        def delete():
            delete_ = self.main_text.curselection()
            if delete_:  # Ensure something is selected
                index = delete_[0]
                look = self.main_text.get(index)
                new_f = []
                with open('tasks.txt', 'r') as f:
                    new_f = f.readlines()
                with open('tasks.txt', 'w') as f:
                    for line in new_f:
                        if line.strip() != look: 
                            f.write(line)
                self.main_text.delete(index)
        
        try:
            with open('tasks.txt', 'r') as file:
                read = file.readlines()
                for line in read:
                    self.main_text.insert(END, line.strip())
        except FileNotFoundError:
            pass  
        
        self.button = Button(self.root,text='ADD',font='sarif, 18 bold italic',
                             width=10,bd=5,bg='light green',fg='black',command=add)
        self.button.place(x=50,y=200)

        self.button2 = Button(self.root,text='DELETE',font='sarif, 18 bold italic',
                              width=10,bd=5,bg='red',fg='black',command=delete)
        self.button2.place(x=50,y=280)


def main():
    root=Tk()
    ui=todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()