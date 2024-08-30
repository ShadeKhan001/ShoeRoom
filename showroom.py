from tkinter import *
from tkinter import ttk
from tkinter import messagebox as tmsg
from datetime import datetime

sell_car = [{"company": "Honda", "model":"Civic", "price": 8659000},{"company": "Toyota", "model":"Land Cruiser", "price": 12000000}]
rent_car = [{"company": "Honda", "model":"City","plate no": "sha 6862","rent": 5000},{"company": "Toyota", "model":"Corolla","plate no": "sha 5911","rent": 4000}]


years = {2023,2019,2024,2022,2020}

now = datetime.now()
current_time = now.strftime('%H:%M:%S')
dat = now.date()


root = Tk()
root.title("Showroom")
root.geometry("340x335")
nb = ttk.Notebook(root)

frame1 = Frame(nb)
frame2 = Frame(nb)
frame3 = Frame(nb)


frame1.grid()
frame2.grid()
frame3.grid()



nb.add(frame1, text = "Sell")
nb.add(frame2, text = "Rent")
nb.add(frame3, text = "Add a Car")

nb.grid()

nb1 = ttk.Notebook(frame3)
frame4 = Frame(nb1)
frame5 = Frame(nb1)

frame4.grid()
frame5.grid()

nb1.add(frame4, text = "Sell")
nb1.add(frame5, text = "Rent")

nb1.grid()


# Sell Alogritm
def pro_tran():
    selected_com = car_company.get()
    selected_mod = car_model.get()
    selected_year = car_year.get()
    owner = cus_name.get()
    owner_cinc = cus_cinc.get()
    owner_no = cus_phone.get()
    owner_adrs = cus_address.get()
    owner_pay = cus_payment.get()
    for car in sell_car:
        car_price = car["price"]
        if car["company"] == selected_com and car["model"] == selected_mod:
            car_price = car["price"]
            agree = tmsg.askquestion("It's Want to buy?", f"Price of {selected_com} {selected_mod} is {car_price}")
            if agree == "yes":
                tmsg.showinfo("New Owner", f"{selected_com} {selected_mod} Owner is {owner}")
                sell_save = open(f"Sell/{owner_cinc}.txt",'a')
                sell_save.write(f"\n\nCustomer Details:\n\nDate Or Time: {dat} {current_time}\nName: {owner}\nCINC: {owner_cinc}\nPhone: {owner_no}\nAddress: {owner_adrs}\nPayment Method: {owner_pay}\n\nCar Details:\n\nCompany: {selected_com}\nModel: {selected_mod}\nYear: {selected_year}\nPrice: {car_price}")
                break
            else:
                tmsg.showwarning("Warning","Oder is cancelled")
            break

# Add sell car
def ad_sell():
    add_com = add_sell_com.get()
    add_mod = add_sell_mod.get()
    add_year = add_sell_year.get()
    add_price = add_sell_pri.get()
    sell_car.append({"company": add_com, "model":add_mod, "price": add_price})
    years.add(add_year)
    tmsg.showinfo("Car Added", f"{add_com} {add_mod} added in Sell Car")



# Rent Alogirtm
def rent_tran():
    selected_com = rent_car_company.get()
    selected_mod = rent_car_model.get()
    selected_year = rent_car_year.get()
    selected_plate = rent_plate_no.get()
    owner = rent_cus_name.get()
    owner_cinc = rent_cus_cinc.get()
    owner_no = rent_cus_phone.get()
    owner_adrs = rent_cus_address.get()
    owner_pay = rent_cus_payment.get()
    for car in rent_car:
        rent_price = car["rent"]
        if car["company"] == selected_com and car["model"] == selected_mod and car["plate no"] == selected_plate:
            car_price = car["price"]
            agree = tmsg.askquestion("It's Want on Rent?", f"Rent per day of {selected_com} {selected_mod} is {rent_price}")
            if agree == "yes":
                tmsg.showinfo("Rented Successfully", f"{selected_com} {selected_mod} {selected_plate} Owner is {owner}")
                sell_save = open(f"Rent/{owner_cinc}.txt",'a')
                sell_save.write(f"\n\nCustomer Details:\n\nDate Or Time: {dat} {current_time}\nName: {owner}\nCINC: {owner_cinc}\nPhone: {owner_no}\nAddress: {owner_adrs}\nPayment Method: {owner_pay}\n\nCar Details:\n\nCompany: {selected_com}\nModel: {selected_mod}\n Plate No: {selected_plate}\nYear: {selected_year}\nRent: {rent_price}")
                break
            else:
                tmsg.showwarning("Warning","Oder is cancelled")
            break

# Add Rent car
def ad_rent():
    add_com = add_rent_com.get()
    add_mod = add_rent_mod.get()
    add_year = add_rent_year.get()
    add_plate = add_rent_plate.get()
    add_price = add_rent_pri.get()
    sell_car.append({"company": add_com, "model":add_mod, "plate no":add_plate ,"rent": add_price})
    years.add(add_year)
    tmsg.showinfo("Car Added", f"{add_com} {add_mod} added in Rent Car")



# Label(frame1, text="Selling Car Or Customer Details", font="Arial 12 bold").grid(row=0, column=2)
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
Label(frame1, text="Model", font="Arial 9 bold").grid(row=16, column=1)
Label(frame1, text="Model Year", font="Arial 9 bold").grid(row=18, column=1)


# Car entry
car_company = StringVar()
car_model = StringVar()
car_model = StringVar()
car_year = StringVar()

car_company.set("Select")
car_model.set("Select")
car_model.set("Select")
car_year.set("Select")
OptionMenu(frame1, car_company,*[car["company"] for car in sell_car]).grid(row=14, column=2)
OptionMenu(frame1, car_model,*[car["model"] for car in sell_car],).grid(row=16, column=2)
OptionMenu(frame1,car_year,*[str(year) for year in years] ).grid(row=18, column=2)


Button(frame1, text="Process Transaction", command=pro_tran).grid()

#Rent
# Label(frame2, text="Rent Car Or Customer Details", font="Arial 12 bold").grid(column=3)
#Customer Details
Label(frame2, text="Customer Details:", font="Arial 10 bold").grid(row=2, column=0)
Label(frame2, text="Full Name", font="Arial 9 bold").grid(row=3, column=1)
Label(frame2, text="CINC No", font="Arial 9 bold").grid(row=5, column=1)
Label(frame2, text="Phone No", font="Arial 9 bold").grid(row=7, column=1)
Label(frame2, text="Address", font="Arial 9 bold").grid(row=9, column=1)
Label(frame2, text="Payment Way", font="Arial 9 bold").grid(row=11, column=1)
# Customer Entry 
rent_cus_name = StringVar()
rent_cus_cinc = IntVar()
rent_cus_phone = IntVar()
rent_cus_address = StringVar()
rent_cus_payment = StringVar()
rent_cus_payment.set("Select")
rent_cus_phone.set(92)

Entry(frame2, textvariable= rent_cus_name).grid(row=3, column=2)
Entry(frame2, textvariable= rent_cus_cinc).grid(row=5, column=2)
Entry(frame2, textvariable= rent_cus_phone).grid(row=7, column=2)
Entry(frame2, textvariable= rent_cus_address).grid(row=9, column=2)
OptionMenu(frame2, rent_cus_payment,"Cash","Credit Card", "Check", "Online",).grid(row=11, column=2)
# Rent car detils
Label(frame2, text="Car Details:", font="Arial 10 bold").grid(row=13, column=0)
Label(frame2, text="Company Name", font="Arial 9 bold").grid(row=14, column=1)
Label(frame2, text="Model", font="Arial 9 bold").grid(row=16, column=1)
Label(frame2, text="Plate No", font="Arial 9 bold").grid(row=18, column=1)
Label(frame2, text="Model Year", font="Arial 9 bold").grid(row=20, column=1)


# Car entry
rent_car_company = StringVar()
rent_car_model = StringVar()
rent_car_model = StringVar()
rent_car_year = StringVar()
rent_plate_no = StringVar()

rent_car_company.set("Select")
rent_car_model.set("Select")
rent_car_model.set("Select")
rent_plate_no.set("Select")
rent_car_year.set("Select")
OptionMenu(frame2, rent_car_company,*[rcar["company"] for rcar in rent_car]).grid(row=14, column=2)
OptionMenu(frame2, rent_car_model,*[rcar["model"] for rcar in rent_car],).grid(row=16, column=2)
OptionMenu(frame2, rent_plate_no,*[rcar["plate no"] for rcar in rent_car],).grid(row=18, column=2)
OptionMenu(frame2,rent_car_year,*[str(year) for year in years] ).grid(row=20, column=2)


Button(frame2, text="Process Transaction", command=rent_tran).grid()

# Add sell car
Label(frame4, text="Car Details:", font="Arial 10 bold").grid(row=2, column=0)
Label(frame4, text="Company Name", font="Arial 9 bold").grid(row=3, column=1)
Label(frame4, text="Model", font="Arial 9 bold").grid(row=5, column=1)
Label(frame4, text="Model Year", font="Arial 9 bold").grid(row=7, column=1)
Label(frame4, text="Price", font="Arial 9 bold").grid(row=9, column=1)

# sell add entry

add_sell_com = StringVar()
add_sell_mod = StringVar()
add_sell_year = IntVar()
add_sell_pri = IntVar()

Entry(frame4, textvariable= add_sell_com).grid(row=3, column=2)
Entry(frame4, textvariable= add_sell_mod).grid(row=5, column=2)
Entry(frame4, textvariable= add_sell_year).grid(row=7, column=2)
Entry(frame4, textvariable= add_sell_pri).grid(row=9, column=2)

Button(frame4, text="Add",command=ad_sell).grid()


# Add rent car
Label(frame5, text="Car Details:", font="Arial 10 bold").grid(row=2, column=0)
Label(frame5, text="Company Name", font="Arial 9 bold").grid(row=3, column=1)
Label(frame5, text="Model", font="Arial 9 bold").grid(row=5, column=1)
Label(frame5, text="Model Year", font="Arial 9 bold").grid(row=7, column=1)
Label(frame5, text="Plate No", font="Arial 9 bold").grid(row=9, column=1)
Label(frame5, text="Per Day Rent", font="Arial 9 bold").grid(row=11, column=1)

# sell add entry

add_rent_com = StringVar()
add_rent_mod = StringVar()
add_rent_year = IntVar()
add_rent_plate = StringVar()
add_rent_pri = IntVar()

Entry(frame5, textvariable= add_rent_com).grid(row=3, column=2)
Entry(frame5, textvariable= add_rent_mod).grid(row=5, column=2)
Entry(frame5, textvariable= add_rent_year).grid(row=7, column=2)
Entry(frame5, textvariable= add_rent_plate).grid(row=9, column=2)
Entry(frame5, textvariable= add_rent_pri).grid(row=11, column=2)

Button(frame5, text="Add",command=ad_rent).grid()

root.mainloop()