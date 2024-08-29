from tkinter import *
from tkinter import ttk
from tkinter import messagebox as tmsg
from datetime import datetime

sell_car = [{"company": "Honda", "modal":"Civic", "price": 8659000},{"company": "Toyota", "modal":"Land Cruiser", "price": 12000000}]
years = {2023,2019,2024,2022,2020}

now = datetime.now()
current_time = now.strftime('%H:%M:%S')
dat = now.date()


root = Tk()
root.title("Showroom")
root.geometry("500x400")
nb = ttk.Notebook(root)

def pro_tran():
    selected_com = car_company.get()
    selected_mod = car_modal.get()
    owner = cus_name.get()
    owner_cinc =cus_cinc.get()
    print("work")
    for car in sell_car:
        if car["company"] == selected_com and car["modal"] == selected_mod:
            car_price = car["price"]
            agree = tmsg.askquestion("It's Want to buy?", f"Price of {selected_com} {selected_mod} is {car_price}")
            if agree == "yes":
                tmsg.showinfo("New Owner", f"{selected_com} {selected_mod} Owner is {owner}")
                sell_save = open("Sell.txt","a")
                sell_save.append(f"\nCustomer Details:\n {owner}")
                break
            else:
                tmsg.showwarning("Warning","Oder is cancelled")
                break
        else:
            tmsg.showwarning("Warning","Please Select Correct Car Company or Car Modal")
            break


frame1 = Frame(nb)
frame2 = Frame(nb)
frame3 = Frame(nb)

Label(frame1, text="Selling Car Or Customer Details", font="Arial 12 bold").grid(row=0, column=2)
#Customer Details
Label(frame1, text="Customer Details:", font="Arial 10 bold").grid(row=2, column=0)
Label(frame1, text="Full Name", font="Arial 9 bold").grid(row=3, column=1)
Label(frame1, text="CINC No", font="Arial 9 bold").grid(row=5, column=1)
Label(frame1, text="Phone No", font="Arial 9 bold").grid(row=7, column=1)
Label(frame1, text="Address", font="Arial 9 bold").grid(row=9, column=1)
Label(frame1, text="Payment Way", font="Arial 9 bold").grid(row=11, column=1)
# Customer Entry 
cus_name = StringVar()
cus_cinc = IntVar()
cus_phone = IntVar()
cus_address = StringVar()
cus_payment = StringVar()
cus_payment.set("Select")
cus_phone.set(92)

Entry(frame1, textvariable= cus_name).grid(row=3, column=2)
Entry(frame1, textvariable= cus_cinc).grid(row=5, column=2)
Entry(frame1, textvariable= cus_phone).grid(row=7, column=2)
Entry(frame1, textvariable= cus_address).grid(row=9, column=2)
OptionMenu(frame1, cus_payment,"Cash","Credit Card", "Check", "Online",).grid(row=11, column=2)
# Selling car detils
Label(frame1, text="Car Details:", font="Arial 10 bold").grid(row=13, column=0)
Label(frame1, text="Company Name", font="Arial 9 bold").grid(row=14, column=1)
Label(frame1, text="Modal", font="Arial 9 bold").grid(row=16, column=1)
Label(frame1, text="Modal Year", font="Arial 9 bold").grid(row=18, column=1)

# Car entry
car_company = StringVar()
car_modal = StringVar()
car_year = StringVar()

car_company.set("Select")
car_modal.set("Select")
car_year.set("Select")
OptionMenu(frame1, car_company,*[car["company"] for car in sell_car]).grid(row=14, column=2)
OptionMenu(frame1, car_modal,*[modal["modal"] for modal in sell_car],).grid(row=16, column=2)
OptionMenu(frame1,car_year,*[str(year) for year in years] ).grid(row=18, column=2)


Button(frame1, text="Process Transaction", command=pro_tran).grid()


Label(frame2, text="Rent Car Or Customer Details", font="Arial 12 bold").grid(column=3)
Label(frame3, text="Add New Car Details", font="Arial 12 bold").grid(column=3)


frame1.grid()
frame2.grid()
frame3.grid()


nb.add(frame1, text = "Sell")
nb.add(frame2, text = "Rent")
nb.add(frame3, text = "Add a Car")
nb.grid()

root.mainloop()