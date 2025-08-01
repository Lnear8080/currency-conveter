import tkinter as tk
import requests
import json
from tkinter import messagebox

# Create a GUI window 
root = tk.Tk() 

# create a global variables 
variable1 = tk.StringVar(root) 
variable2 = tk.StringVar(root) 

# initialise the variables 
variable1.set("currency") 
variable2.set("currency") 

# ExchangeRate-API key - Replace with your actual API key
API_KEY = "YOUR_API_KEY"  # Get your free API key from https://www.exchangerate-api.com/

def RealTimeCurrencyConversion(): 
    from_currency = variable1.get() 
    to_currency = variable2.get()
    
    if from_currency == "currency" or to_currency == "currency":
        Amount2_field.delete(0, tk.END)
        Amount2_field.insert(0, "Select currencies")
        return
    
    try:
        amount = float(Amount1_field.get())
        
        # Try to get rates from API
        try:
            url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
            response = requests.get(url)
            data = response.json()
            
            if data["result"] == "success":
                # Get the conversion rate
                conversion_rate = data["conversion_rates"][to_currency]
                new_amount = amount * conversion_rate
                
                # Clear previous value
                Amount2_field.delete(0, tk.END)
                # Format to 2 decimal places and insert
                Amount2_field.insert(0, f"{new_amount:.2f}")
            else:
                # If API request fails, fall back to hardcoded rates
                fallback_to_hardcoded_rates(amount, from_currency, to_currency)
        except Exception as e:
            print(f"API Error: {e}")
            # Fall back to hardcoded rates
            fallback_to_hardcoded_rates(amount, from_currency, to_currency)
            
    except ValueError:
        Amount2_field.delete(0, tk.END)
        Amount2_field.insert(0, "Invalid input")

def fallback_to_hardcoded_rates(amount, from_currency, to_currency):
    # Hardcoded conversion rates as fallback
    conversion_rates = {
        "INR": {"USD": 0.012, "CAD": 0.016, "CNY": 0.087, "DKK": 0.087, "EUR": 0.011, "INR": 1.0},
        "USD": {"INR": 83.24, "CAD": 1.35, "CNY": 7.26, "DKK": 6.91, "EUR": 0.92, "USD": 1.0},
        "CAD": {"INR": 61.58, "USD": 0.74, "CNY": 5.37, "DKK": 5.11, "EUR": 0.68, "CAD": 1.0},
        "CNY": {"INR": 11.46, "USD": 0.14, "CAD": 0.19, "DKK": 0.95, "EUR": 0.13, "CNY": 1.0},
        "DKK": {"INR": 12.05, "USD": 0.14, "CAD": 0.20, "CNY": 1.05, "EUR": 0.13, "DKK": 1.0},
        "EUR": {"INR": 90.39, "USD": 1.09, "CAD": 1.47, "CNY": 7.88, "DKK": 7.50, "EUR": 1.0}
    }
    
    try:
        new_amount = amount * conversion_rates[from_currency][to_currency]
        # Clear previous value
        Amount2_field.delete(0, tk.END)
        # Format to 2 decimal places and insert - removed "(offline)" text
        Amount2_field.insert(0, f"{new_amount:.2f}")
    except KeyError:
        Amount2_field.delete(0, tk.END)
        Amount2_field.insert(0, "Conversion not available")

def clear_all() : 
	Amount1_field.delete(0, tk.END) 
	Amount2_field.delete(0, tk.END)

if __name__ == "__main__" : 

	# Set the background colour of GUI window 
	root.configure(background = '#e6e5e5') 
	
	# Set the configuration of GUI window (WidthxHeight) 
	root.geometry("400x200") 
	
	# Create welcome to Real Time Currency Convertor label 
	headlabel = tk.Label(root, text = 'Pypower Currency Converter', bg= '#663300',fg='white') 

	# Create a "Amount :" label 
	label1 = tk.Label(root, text = "Amount", bg="orange",fg = "white",font=('arial', 10,'bold')) 
	
	# Create a "From Currency :" label 
	label2 = tk.Label(root, text = "From Currency", bg="orange",fg = "white",font=('arial', 10,'bold')) 
	
	# Create a "To Currency: " label 
	label3 = tk.Label(root, text = "To Currency", bg="orange",fg = "white",font=('arial', 10,'bold')) 

	# Create a "Converted Amount :" label 
	label4 = tk.Label(root, text = "Converted Amount",bg="orange",fg = "white",font=('arial', 10,'bold')) 

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
	headlabel.grid(row = 0, column = 1) 
	label1.grid(row = 1, column = 0) 
	label2.grid(row = 2, column = 0) 
	label3.grid(row = 3, column = 0) 
	label4.grid(row = 5, column = 0) 
	
	# Create a text entry box 
	# for filling or typing the information. 
	Amount1_field = tk.Entry(root) 
	Amount2_field = tk.Entry(root) 
	
	# ipadx keyword argument set width of entry space. 
	Amount1_field.grid(row = 1, column = 1, ipadx ="25") 
	Amount2_field.grid(row = 5, column = 1, ipadx ="25") 

	# list of currency codes 
	CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"] 

	# create a drop down menu using OptionMenu function 
	# which takes window name, variable and choices as 
	# an argument. use * befor the name of the list, 
	# to unpack the values 
	FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list) 
	ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list) 
	
	FromCurrency_option.grid(row = 2, column = 1, ipadx = 10) 
	ToCurrency_option.grid(row = 3, column = 1, ipadx = 10) 
	
	# Create a Convert Button and attached 
	# with RealTimeCurrencyExchangeRate function 
	button1 = tk.Button(root, text = "Convert", bg = "Green", fg = "White",command=RealTimeCurrencyConversion) 
	
	button1.grid(row = 4, column = 1) 

	# Create a Clear Button and attached 
	# with delete function 
	button2 = tk.Button(root, text = "Clear", bg = "red",fg = "White", command = clear_all) 
	button2.grid(row = 6, column = 1) 
	
	# Start the GUI 
	root.mainloop()
