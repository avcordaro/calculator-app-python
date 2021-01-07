# Calculator App (Python)
Built using Python + PyQt5.

An improvement over my previous project, calculator-app-java, this calculator app written in Python can also deal with parantheses and negative numbers. The app also has a different GUI made using PyQt5. 

This project was inspired by the 2nd Kuyu Kata on Codewars for parsing mathematical expressions.(https://www.codewars.com/kata/52a78825cdfc2cfc87000005). I decided to take my Python solution and implement it into a proper program with a nice GUI calculator. 

The app does not use the Python 'eval' function to evaluate the answer, instead it uses my own implementation of Dijkstra's Shunting Yard algorithm to convert the expression to RPN (Reverse Polish Notation), then evaluates the RPN expression using a simple stack method.  

## Running the program
The program can be run using the Calculator.exe file provided, assuming you are on Windows.

Otherwise, with Python3 installed, you can run the following commands:
```
pip install PyQt5
python src/calc_controller.py
```

![screenshot](https://i.imgur.com/KDCLBEP.png)
