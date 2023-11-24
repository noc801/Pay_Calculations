from tkinter import *
from tkinter import messagebox

def reset_entry():
    hours_tf.delete(0, "end")
    rate_tf.delete(0, "end")

def calculate_pay():
    try:
        x = float(hours_tf.get())
        y = float(rate_tf.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")
        return

    if x > 40:
        reg = x * y
        ot = (x - 40.0) * (y * 1.5)
        z = reg + ot
        tax = round(z * 0.1, 2)
        after_tax = z - tax
    else:
        z = x * y
        tax = round(z * 0.1, 2)
        after_tax = z - tax
    
    message = (
        f"Pay Before Tax: {z}\n"
        f"Tax: {tax}\n"
        f"Pay After Tax: {after_tax}"
    )

    messagebox.showinfo("Pay Information", message)

ws = Tk()
ws.title("Pay Calculator")
ws.geometry("400x300")
ws.config(bg="#68be70")

var = IntVar()

frame = Frame(
    ws,
    padx = 10,
    pady = 10
)

frame.pack(expand = True)

hours_lb = Label(
    frame,
    text="Enter Hours Worked"
)

hours_lb.grid(row = 1, column = 1)

hours_tf = Entry(
    frame,
)

hours_tf.grid(row = 1, column = 2, pady = 5)

rate_lb = Label(
    frame,
    text = "Enter Hourly Rate",
)

rate_lb.grid(row = 2, column = 1)

rate_tf = Entry(
    frame,
)

rate_tf.grid(row = 2, column = 2, pady = 5)

frame2 = Frame(
    frame
)
frame2.grid(row = 3, column = 3, pady = 10)

cal_rate = Button(
    frame2,
    text = "Calculate",
    command = calculate_pay
)
cal_rate.pack(side=LEFT)

reset_btn = Button(
    frame2,
    text = "Reset",
    command = reset_entry
)
reset_btn.pack(side = LEFT)

exit_btn = Button(
    frame2,
    text = "Exit",
    command = lambda: ws.destroy()
)
exit_btn.pack(side = RIGHT)

ws.mainloop()
