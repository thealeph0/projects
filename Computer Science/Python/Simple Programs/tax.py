def main():
    income = int(input('Enter 2024 income:' ))
    print()
    if income <= 11600:
        tax = income * 0.1 #percentage you owe in taxes
        bracket = '10% tax bracket'
        
    elif income <= 47_150:
        tax = 1160 + (income - 11_600)*0.12
        bracket = '12% tax bracket'
        
    elif income <= 100_525:
        tax =  1160+ 4265.88 + (income - 47_150)*0.22
        bracket = '22% tax bracket'
        
    elif income <= 191_950:
        tax = 1160 + 4265.88 + 11_742.28 + (income - 100_525)*0.24
        bracket = '24% tax bracket'
        
    elif income <= 243_725:
        tax = 1160 + 4265.88 + 11_742.28 + 21_941.76 + (income - 191_950)*0.32
        bracket = '32% tax bracket'
        
    elif income <= 609_350:
        tax = 1160 + 4265.88 + 11_742.28 + 21_941.76 + (243_725 - 191_951)*0.32 + 0.35*(income - 243_725)
        bracket = '35% tax bracket'
        
    elif income > 609_351:
        tax = 1160 + 4265.88 + 11_742.28 + 21_941.76 + (243_725 - 191_951)*0.32 + (609_350 - 243_725)*0.35 + 0.37*(income - 609_350)
        bracket = '37% tax bracket'
        
    print("An income of" , format(income, ',d') , 'places you in the', bracket)
    print('The US Federal tax on an income of', income , 'is', tax)
    
main()