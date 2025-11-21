def atm():
    pin = "1234"
    bal = 100
    tries = 0
    max_try = 3
    
    print("ATM Ready")
    
    while tries < max_try:
        user_pin = input("PIN: ")
        
        if user_pin == pin:
            print("OK")
            break
        else:
            tries += 1
            left = max_try - tries
            print(f"Wrong PIN. {left} tries left")
    
    if tries == max_try:
        print("Card locked")
        return
    
    print(f"Balance: ${bal}")
    cash = float(input("Amount: $"))
    
    if cash <= bal:
        bal -= cash
        print(f"Got: ${cash}")
        print(f"Left: ${bal}")
        
        if bal == 0:
            print("Account empty - closing")
    else:
        print("Not enough money")

print("Starting")
atm()
print("Done")