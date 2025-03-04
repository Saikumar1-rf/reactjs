# from tkinter import *

# root = Tk()
# root.title("Login")
# root.geometry("500x300")

# def getvals():
#     print("Accepted")
#     print(f"Name: {namevalue.get()}")
#     print(f"Phone: {phonevalue.get()}")
#     print(f"Gender: {gendervalue.get()}")
#     print(f"Emergency Contact: {emergencyvalue.get()}")
#     print(f"Payment Mode: {paymentmoodvalue.get()}")
#     print(f"Remember Me: {'Yes' if checkvalue.get() else 'No'}")

# Label(root, text="Login form", font="Arial 15 bold").grid(row=0, column=3)

# # Labels
# name = Label(root, text="Name")
# phone = Label(root, text="Phone")
# gender = Label(root, text="Gender")
# emergency = Label(root, text="Emergency")
# paymentmood = Label(root, text="Payment Mode")

# name.grid(row=1, column=2)
# phone.grid(row=2, column=2)
# gender.grid(row=3, column=2)
# emergency.grid(row=4, column=2)
# paymentmood.grid(row=5, column=2)

# # Entry variables
# namevalue = StringVar()
# phonevalue = StringVar()
# gendervalue = StringVar()
# emergencyvalue = StringVar()
# paymentmoodvalue = StringVar()
# checkvalue = IntVar()

# # Entry fields
# nameentry = Entry(root, textvariable=namevalue)
# phoneentry = Entry(root, textvariable=phonevalue)
# genderentry = Entry(root, textvariable=gendervalue)
# emergencyentry = Entry(root, textvariable=emergencyvalue)
# paymentmoodentry = Entry(root, textvariable=paymentmoodvalue)

# nameentry.grid(row=1, column=3)
# phoneentry.grid(row=2, column=3)
# genderentry.grid(row=3, column=3)
# emergencyentry.grid(row=4, column=3)
# paymentmoodentry.grid(row=5, column=3)

# # Checkbox
# checkbtn = Checkbutton(root, text="Remember me?", variable=checkvalue)
# checkbtn.grid(row=6, column=3)

# # Submit Button
# Button(root, text="Submit", command=getvals).grid(row=7, column=3)

# root.mainloop()


from tkinter import *

# Initialize window
root = Tk()
root.title("Login Form")
root.geometry("500x350")
root.configure(bg="#f4f4f4")  # Set background color

def getvals():
    print("Accepted")
    print(f"Name: {namevalue.get()}")
    print(f"Phone: {phonevalue.get()}")
    print(f"Gender: {gendervalue.get()}")
    print(f"Emergency Contact: {emergencyvalue.get()}")
    print(f"Payment Mode: {paymentmoodvalue.get()}")
    print(f"Remember Me: {'Yes' if checkvalue.get() else 'No'}")

# Title Label
Label(root, text="Login Form", font=("Arial", 18, "bold"), bg="#f4f4f4", fg="#333").grid(row=0, column=1, pady=15)

# Labels Styling
labels = ["Name:", "Phone:", "Gender:", "Emergency Contact:", "Payment Mode:"]
for i, text in enumerate(labels):
    Label(root, text=text, font=("Arial", 12), bg="#f4f4f4", fg="#333").grid(row=i+1, column=0, padx=20, pady=5, sticky=W)

# Entry Variables
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmoodvalue = StringVar()
checkvalue = IntVar()

# Entry Fields Styling
entries = [namevalue, phonevalue, gendervalue, emergencyvalue, paymentmoodvalue]
for i, var in enumerate(entries):
    Entry(root, textvariable=var, font=("Arial", 12), width=25, bd=2, relief=GROOVE).grid(row=i+1, column=1, padx=10, pady=5)

# Checkbox
Checkbutton(root, text="Remember me?", variable=checkvalue, font=("Arial", 11), bg="#f4f4f4").grid(row=6, column=1, pady=10)

# Submit Button Styling
Button(root, text="Submit", command=getvals, font=("Arial", 12, "bold"), bg="#28a745", fg="white", width=15, bd=2, relief=RAISED).grid(row=7, column=1, pady=15)

# Run the main loop
root.mainloop()