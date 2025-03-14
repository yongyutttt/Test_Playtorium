from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from campaigns import Campaigns

root = Tk()
root.title("Shopping cart")

countShirt = IntVar()
countHoodie = IntVar()
countBag = IntVar()
countHat = IntVar()
countBelt = IntVar()
countWatch = IntVar()
choichCoupon = StringVar(value="Choose coupon")
choichOntop= StringVar(value="Choose on top")

clothing = {"T-Shirt": 0, "Hoodie": 0}
accessories = {"Bag": 0, "Hat": 0, "Belt": 0}
electronic = {"Watch": 0}

products = [clothing, accessories, electronic]

def show_summary():
    products.count(1)
    textDiscount = "Discount: "

    amountSummary: int = 0
    amountSummaryClothing: int = 0
    amountSummaryAccessories: int = 0
    amountSummaryElectronic: int = 0

    clothing["T-Shirt"] = countShirt.get()
    clothing["Hoodie"] = countHoodie.get()
    accessories["Bag"] = countBag.get()
    accessories["Belt"] = countBelt.get()
    accessories["Hat"] = countHat.get()
    electronic["Watch"] = countWatch.get()
    
    for key, value in clothing.items():
        if key == "T-Shirt":
            amountSummaryClothing += value*350
        elif key == "Hoodie":
            amountSummaryClothing += value*700
    
    for key, value in accessories.items():
        if key == "Bag":
            amountSummaryAccessories += value*640
        elif key == "Hat":
            amountSummaryAccessories += value*250
        elif key == "Belt":
            amountSummaryAccessories += value*230

    amountSummaryElectronic += electronic["Watch"] * 850    
    amountSummary = amountSummaryAccessories + amountSummaryClothing + amountSummaryElectronic

    num = 0
    flag = False
    for product in products:
        countList = list(product.values())
        for i in countList:
            if i > 0:
                num += 1
    if num == 1 :
        flag = True
        
    campaing = Campaigns(amountSummary, amountSummaryClothing, amountSummaryAccessories, amountSummaryElectronic)

    if couponValue.get() > 0:
        if selectionCoupon.get() == "Fixed amount":
            campaing.fixedCoupon(couponValue.get())
            textDiscount = textDiscount + str(couponValue.get()) + " THB\n"
        elif selectionCoupon.get() == "Percentage discount":
            campaing.percentCoupon(couponValue.get())
            textDiscount = textDiscount + str(couponValue.get()) + "%\n"
    if onTopValue.get() > 0:
        if selectOntop.get() == "Percent on top":
            print(flag)
            campaing.percentOntop(category.get(), onTopValue.get(), flag)
            print(campaing.amountSummary)
            textDiscount = textDiscount + str(onTopValue.get()) + "%" + " Off on " + str(category.get()) +"\n"
        elif selectOntop.get() == "Point on top":
            campaing.pointOntop(onTopValue.get())
            textDiscount = textDiscount + str(onTopValue.get()) + " THB on Points\n"

    if selectCampaign.get() == "Seasonal campaigns":
        print("pass")
        campaing.seasonal(discountPerRound.get(), discount.get())
        textDiscount = textDiscount + str(discount.get()) + " THB at every " +  str(discountPerRound.get()) + " THB\n"

    amountSummary = campaing.amountSummary
    amountSummaryAccessories = campaing.amountSummaryAccessories
    amountSummaryClothing = campaing.amountSummaryClothing
    amountSummaryElectronic = campaing.amountSummaryElectronic

    amountSummary = "{:,}".format(amountSummary)
    summary_window = Toplevel(root)
    summary_window.title("Summary")
    summary_window.geometry("300x300")
    headerLabel = Label(summary_window, text="This is the summary details", font=("Arial", 12))
    headerLabel.pack(pady=20)
    text = ""
    for product in products:
        for key, value in product.items():
            if value > 0:
                if key == "T-Shirt":
                    text = text + str(value) + " " + key + ": " + str(value * 350) + " THB\n"
                elif key == "Hoodie":
                    text = text + str(value) + " " + key + ": " + str(value * 700) + " THB\n"
                elif key == "Bag":
                    text = text + str(value) + " " + key + ": " + str(value * 640) + " THB\n"
                elif key == "Hat":
                    text = text + str(value) + " " + key + ": " + str(value * 250) + " THB\n"  
                elif key == "Belt":
                    text = text + str(value) + " " + key + ": " + str(value * 230) + " THB\n"
                elif key == "watch":
                    text = text + str(value) + " " + key + ": " + str(value * 850) + " THB\n"
  
    label = Label(summary_window, text="Items in cart:\n" + text + "\n" + textDiscount + "\n" + "Total price: " + str(amountSummary) + " THB", font=("Arial", 12))
    label.pack(expand=True)
    
    close_button = Button(summary_window, text="Close", command=summary_window.destroy)
    close_button.pack()

def checkCampaingCoupon():
    if selectionCoupon.get() != "":
        coupon = Entry(font=10, width=10, textvariable=couponValue).grid(row=4, column=3) 

def checkOnTOp():
    if selectOntop.get() == "Percent on top":
        onTop = Entry(font=10, width=10, textvariable=onTopValue).grid(row=5, column=3)
        categoryCombo.grid(row=5, column=4)
    else:
        onTop = Entry(font=10, width=10, textvariable=onTopValue).grid(row=5, column=3)
        categoryCombo.grid_forget()

def checkCampaign():
    if selectCampaign.get() != "":
        campaignDiscount = Entry(font=10, width=10, textvariable=discount).grid(row=6, column=2)
        everyAmount = Entry(font=10, width=10, textvariable=discountPerRound).grid(row=6, column=3)
    
Label(text="T-Shirt:", padx=10, font=10).grid(row=1)
shrit = Entry(font=10, width=10, textvariable=countShirt).grid(row=1, column=1)

Label(text="Hoodie:", padx=10, font=20).grid(row=1, column=2, sticky=W)
hoodie = Entry(font=10, width=10, textvariable=countHoodie).grid(row=1, column=3)

Label(text="Bag:", padx=10, font=20).grid(row=1, column=4)
bag = Entry(font=10, width=10, textvariable=countBag).grid(row=1, column=5)

Label(text="Hat:", padx=10, font=20).grid(row=2)
hat = Entry(font=10, width=10, textvariable=countHat).grid(row=2, column=1)

Label(text="Belt:", padx=10, font=20).grid(row=2, column=2)
belt = Entry(font=10, width=10, textvariable=countBelt).grid(row=2, column=3)

Label(text="Watch:", padx=10, font=20).grid(row=2, column=4)
watch = Entry(font=10, width=10, textvariable=countWatch).grid(row=2, column=5)

selectionCoupon = StringVar()
couponValue = IntVar()
Radiobutton(root, text="Fixed amount", variable=selectionCoupon, value="Fixed amount", command=checkCampaingCoupon).grid(row=4, column=1)
Radiobutton(root, text="Percentage discount", variable=selectionCoupon, value="Percentage discount", command=checkCampaingCoupon).grid(row=4, column=2)

selectOntop = StringVar()
category = StringVar(value="Select category")
onTopValue = IntVar()
categoryCombo = ttk.Combobox(font=10, width=10, textvariable=category, values=["Clothing","Accessory","Electronic"])
Radiobutton(root, text="Percent on top", variable=selectOntop, value="Percent on top", command=checkOnTOp).grid(row=5, column=1)
Radiobutton(root, text="Point on top", variable=selectOntop, value="Point on top", command=checkOnTOp).grid(row=5, column=2)

selectCampaign = StringVar()
discount = IntVar(value="Discount")
discountPerRound = IntVar(value="Amount")
Radiobutton(root, text="Seasonal campaigns", variable=selectCampaign, value="Seasonal campaigns", command=checkCampaign).grid(row=6, column=1)

Button(root, text="Show Summary", command=show_summary, pady=10).grid(row=7, columnspan=6)
root.mainloop()
## messagebox.showinfo("Summary", "This is the summary details")