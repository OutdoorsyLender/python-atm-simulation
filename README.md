# python-atm-simulation
# ATM Simulation Program

This project is a simple ATM simulation written in Python. It includes PIN validation, balance checking, withdrawal logic, error handling, and basic security behavior such as card lock-out after failed attempts. A UML diagram is included to illustrate the program flow and system structure.

This project was part of my CSC505 course, covering software quality, security, and testing concepts.

## How It Works

The program runs in the terminal and steps through:

1. User enters a PIN
2. User gets three attempts before the card locks
3. If the PIN is correct:
   - The current balance is shown
   - The user enters a withdrawal amount
   - The program checks available funds
   - The withdrawal is processed and the remaining balance is displayed

4. If the withdrawal amount exceeds the balance, the program displays an error.

## Features

- PIN authentication with limited attempts
- Basic security behavior with lockout
- Withdrawal and balance updates
- Error handling for insufficient funds
- Clear terminal interaction
- UML diagram showing system flow

## Files Included

**atm.py**  
Main ATM program that handles PIN validation, balance updates, and withdrawal logic.

**atm.plantuml**  
UML diagram for the ATM system.

## How to Run

1. Install Python 3.
2. Place `atm.py` in a folder.
3. Open a terminal in that folder.
4. Run:

```
python atm.py
```

## Example Run

```
Starting
ATM Ready
PIN: 1234
OK
Balance: $100
Amount: $40
Got: $40
Left: $60
Done
```

## What I Learned

This project helped reinforce:

- The importance of security considerations
- User-input handling
- Error checking and system boundaries
- Why real ATM systems require robust testing and secure processes
- How UML diagrams help clarify flow before coding

## Author

Brandon Everett

