# TransactionsToExcel
This is a program we use to sort a CSV file of transactions in an excel file to ease the overview of the finances.


## Excel finance document Format

The template required to use this program is provided "Finances.xlsx". This name can be changed.

### Worksheet Algemeen

In this worksheet the main balance of all the worksheets is made. You can change things as you want except for cell E4. This is used to track the last time the transactions were checked.

### Worksheet Sjabloon

This worksheet is a template for other worksheets you want to sort transactions into. In cell E4 you need to put an abreviation like EG: "PNK" for the pannekoeken worksheet. when some one puts "PNK john doe" into the discription of their transaction it will automaticly be filled in to the pannekoeken worksheet.

### Worksheet Transacties

In this worksheet all of the transactions are kept in order in case of mistakes in the 
accountancy.

### Worksheet Pannekoeken

This worksheet is just made up as an example to show how to use the program

## CSV transaction document format

The template required to use this program is provided "Transactions.xlsx". This name can be changed. This is the standard output when downloading CSV file from KBC bank transactions so if you have KBC youre transactions will have the right format.

## Compiling the python program to an executable

The module PyInstaller is used, after installing the module run the following code:

```
python -m PyInstaller --onefile FinanceAuto.py
```