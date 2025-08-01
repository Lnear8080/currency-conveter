# Currency Converter
A simple GUI application to convert currencies in real time using ExchangeRate-API, built with Python and Tkinter.

Features
Convert between 6 major currencies: INR, USD, CAD, CNY, DKK, EUR.

Real-time exchange rates via ExchangeRate-API.

Offline fallback with hardcoded rates if the API is unavailable.

User-friendly Tkinter GUI.

Clear input/output fields easily.

Installation
Clone this repository:

bash
git clone https://github.com/Lnear8080/currency-conveter.git
cd currency-conveter
Install the requirements:

bash
pip install requests
Get a free API key from ExchangeRate-API and replace YOUR_API_KEY in currency_converter.py with your actual key.

Usage
Run the application:

bash
python currency_converter.py
Enter the amount, select "From Currency" and "To Currency", then click Convert.

To clear entries, click Clear.

Supported Currencies
INR (Indian Rupee)

USD (US Dollar)

CAD (Canadian Dollar)

CNY (Chinese Yuan)

DKK (Danish Krone)

EUR (Euro)

Screenshot
(Add a screenshot of the application here if available)

Notes
Requires an active internet connection for real-time rates.

If the API is unreachable, fallback rates are used for conversion.

Only supports conversion between the listed currencies.

License
This project is open source. See the LICENSE file for details.
