import tkinter as tk
def buttonClick():
    a = e1.get()
    print(a)

screen1 = tk.Tk()
screen1.title('Score Filter')
l1 = tk.Label(screen1, text = "Enter the minimum grade to filter:")
l1.pack()
e1= tk.Entry(screen1)
e1.pack()
b1 = tk.Button(text= "ENTER", width= 10, bg = "white", fg = "red", font= "Arial 20 bold", command= buttonClick )
b1.pack()
screen1.mainloop()