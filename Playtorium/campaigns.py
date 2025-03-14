from tkinter import messagebox
import sys

class Campaigns:
    def __init__(self, amountSummary, amountSummaryClothing, amountSummaryAccessories, amountSummaryElectronic):
        self.amountSummary = amountSummary
        self.amountSummaryClothing = amountSummaryClothing
        self.amountSummaryAccessories = amountSummaryAccessories
        self.amountSummaryElectronic = amountSummaryElectronic
    
    def fixedCoupon(self, amount: int):
        self.amountSummary -= amount

    def percentCoupon(self, percent: int):
        self.amountSummary = self.amountSummary*(1-(percent/100))

    def percentOntop(self, category: str, percent: int, flag):
        if(flag):
            self.amountSummary -= self.amountSummary*(percent/100)
            print("pass")
        else:
            if(category == "Clothing"):
                self.amountSummary -= self.amountSummaryClothing*(percent/100)
            elif(category == "Accessories"):
                self.amountSummary = self.amountSummaryAccessories*(percent/100)
            elif(category == "Electronic"):
                self.amountSummary = self.amountSummaryElectronic*(percent/100)
        
    def pointOntop(self, customerPoint: int):
        checkRule = (customerPoint*100)/self.amountSummary
        if checkRule <= 20 :    
            self.amountSummary -= customerPoint
        else:
            messagebox.showinfo("Info", "Discount over 20% of total.")
            sys.exit()

    def seasonal(self, amountPerRound: int, discount: int):
        round = self.amountSummary//amountPerRound
        if(round>0):
            self.amountSummary -= round * discount
        else:
            messagebox.showinfo("Info", "The spending amount has not been reached.")
            sys.exit()