# Loan Qualification Application

This application allows potential loan borrowers to quickly and easily identify available loan offerings. With a few user inputs the app will return a list of available bank lenders, maximum loan amount, and loan interest rate. The application will prompt the user if no loans are available. If there are available loans the application will ask the user if they'd like a CSV output, if they select yes it will produce a csv file that lists the available lenders and loans in the file path and name they enter. 

---

## Technologies

The application is written in Python and utilizes the Fire and Questionary libraries. The Fire and Questionary libraries enable the user interface and allows for user inputs and on demand execution of the loan qualifaction search. 

---

## Installation Guide

To run this Python code you need to install the `fire` and `questionary` libraries.

*Enter the following commands in your terminal:*

```python
pip install fire
pip install questionary
```

---

## Usage

Open a terminal Git Bash (PC) or Terminal (MacOS) and run the program using the following command:
```python
python app.py
```
![Example of the CLI user input code](https://github.com/rjohnson617/Loan_Qualification_Application/blob/main/Capture.PNG?raw=true)

You will be prompted for the following:
1) Provide file location for the current list of lenders
2) Enter your credit score
3) Monthly debt payments
4) Monthly income amount
5) Your desired loan amount (how much you want to borrow)
6) The estimated home value for the home you want to purchase (recent property tax assessment, Redfin, Zillow, etc.)
7) Select if you would like a CSV ouput of the results (if there are available loans) and choose the file path to save the CSV

---

## Contributors

Code produced by Ryan Johnson

---

## License

Copyright (c) [2022] [Ryan Johnson]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
