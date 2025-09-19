
import re
def check_eligibility():
    print("=== Loan Eligibility Checker ===")
    name = input("Enter your name: ")
    print("Welcome",name,"✅")
    try:
        age = int(input("Enter your age: "))
        if not(18 <= age <= 59):
                    print("❌ Sorry, your age must be between 18 and 59.")
                    return 
        salary = int(input("Enter your salary: "))
        if not(salary>25000):
                    print("❌ Sorry, your salary must be above 25000.") 
                    return
        pincard = input("Do you have a PAN card? (yes/no): ").strip().lower()
        if not(pincard =='yes'):
                    print("❌ Sorry, PAN card is mandatory.")    
                    return
        Aadhar = (input("Do you have a Aadhar card ? (yes/no): ")).strip().lower()
        if not(Aadhar == 'yes'):
                    print("❌ Sorry, Aadhaar card is mandatory.")    
                    return
        ad_no = input("enter your Aadhar number(last 4 digit only): ")
        if not re.fullmatch(r"\d{4}",ad_no):
                    print("❌ Invalid Aadhaar input! Please enter exactly 4 digits.")
                    return       
        print("\nChecking your details...\n")

        print("✅ Congratulations,".upper(), name,"ji")
        print("You are eligible for a loan!".upper())
        print("Our team will contact you soon.".upper())
        print("Thank you so much 🙏😊")
    except:
        print("❌ Invalid input! Please enter numbers only for age/salary.")   
check_eligibility()        
# if not :- agr bas condition galat hone pe message print karana hoto if not ka use kro
# aagar aapko condition true hone pe kuch dusra message print karan h aor condition false hone
#pe kuch aor mssage print karana ho to if not ke sath esle bhi use krna pdega 

#try:- try ke andr code likhne ye hota h ki agr kahi user input krate ho aor vo number ke jgh pe 
# word me likh deta h to vo pura code crash nhi hota vo except me jo aapne messege likha hota h
# vo show kar deta h 


#.strip().lower():- strip ka kam hai start ya end me agr user ne space de diya h to hta dega
# aor lower ka kam h agr user capital leter ya samal letter me input diya h to bhi samaj lega
