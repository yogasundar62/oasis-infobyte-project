import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
bmi_history = []
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100 
    return weight / (height_m ** 2)
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
def calculate_bmi_gui():
    try:
        weight = float(entry_weight.get())
        height_cm = float(entry_height.get())
        if weight <= 0 or height_cm <= 0:
            messagebox.showerror("Error", "Enter positive values.")
            return
        bmi = calculate_bmi(weight, height_cm)
        bmi_history.append(bmi)
        category = categorize_bmi(bmi)
        label_result.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers.")
def show_history():
    if not bmi_history:
        messagebox.showinfo("No Data", "No BMI history yet.")
        return
    plt.plot(bmi_history, marker='o')
    plt.title("BMI Trend")
    plt.xlabel("Entry Number")
    plt.ylabel("BMI")
    plt.grid(True)
    plt.show()
gui = tk.Tk()
gui.title("BMI Calculator")
tk.Label(gui, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=5)
entry_weight = tk.Entry(gui)
entry_weight.grid(row=0, column=1, padx=10, pady=5)
tk.Label(gui, text="Height (cm):").grid(row=1, column=0, padx=10, pady=5)
entry_height = tk.Entry(gui)
entry_height.grid(row=1, column=1, padx=10, pady=5)
tk.Button(gui, text="Calculate BMI", command=calculate_bmi_gui).grid(row=2, column=0, columnspan=2, pady=10)
label_result = tk.Label(gui, text="Your BMI will appear here.")
label_result.grid(row=3, column=0, columnspan=2)
tk.Button(gui, text="Show BMI History", command=show_history).grid(row=4, column=0, columnspan=2, pady=10)
gui.mainloop()





