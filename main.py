import tkinter

#window
window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=250, height=200)
window.config(padx=20, pady=20)

#weight label
weight_label = tkinter.Label(text="Enter Your Weight(kg)")
weight_label.pack()

#weight entry
weight_entry = tkinter.Entry(width=10)
weight_entry.pack()

#height label
height_label = tkinter.Label(text="Enter Your Height(cm)")
height_label.pack()

#height entry
height_entry = tkinter.Entry(width=10)
height_entry.pack()

#result label
result_label = tkinter.Label()
result_label.pack()


#button
def clicked_button():
    if weight_entry.get() == "" and height_entry.get() == "":
        result_label.config(text="Enter both weight and height!!!")
    elif weight_entry.get() == "":
        result_label.config(text="Enter weight!!!")
    elif height_entry.get() == "":
        result_label.config(text="Enter height!!!")
    else:
        try:
            user_weight = float(weight_entry.get())
            user_height = float(height_entry.get())
            user_bmi = round(user_weight / ((user_height / 100) ** 2), 2)
            if user_bmi < 18.5:
                result_label.config(text=f"Your BMI is {user_bmi} . Underweight")
            elif 18.5 <= user_bmi < 25.0:
                result_label.config(text=f"Your BMI is {user_bmi} . Normal weight")
            elif 25.0 <= user_bmi < 30.0:
                result_label.config(text=f"Your BMI is {user_bmi} . Overweight")
            elif 30.0 <= user_bmi < 35.0:
                result_label.config(text=f"Your BMI is {user_bmi} . Obesity(Class 1)")
            elif 35.0 <= user_bmi < 40.0:
                result_label.config(text=f"Your BMI is {user_bmi} . Obesity(Class 2)")
            elif user_bmi >= 40.0:
                result_label.config(text=f"Your BMI is {user_bmi} . Obesity(Class 3)")
        except:
            result_label.config(text="Enter valid type!!!")


calc_button = tkinter.Button(text="Calculate", command=clicked_button)
calc_button.pack()

window.mainloop()