contacts={}
while True:
    print("\n__Contact Book__")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Total Contact")
    print("7. EXIT")

    choice = input("Enter Choice: ")

    if choice=="1":
        name=input("Enter Name: ")
        phone=input("Enter Phone Number: ")
        email=input("Enter Email: ")

        contacts[name]={
            "Phone":phone,
            "Email":email
        }
        print("Contact Added Successfully")

    elif choice=="2":
        if len(choice)==0:
            print("No contact available")
        else:
            print("\n__Contact List__")
            for name,details in contacts.items():
                print("\nName:",name)
                print("Phone:",details["Phone"])
                print("Email:",details["Email"])
    elif choice=="3":
        name=input("Enter Name to Search: ")
        if name in contacts:
            print("\nContact Found")
            print("Phone:",contacts[name]["Phone"])
            print("Email:",contacts[name]["Email"])
        else:
            print("Contact not found")
    elif choice=="4":
        name=input("Enter Name to Update: ")
        if name in contacts:
            phone=input("Enter new phone number:")
            email=input("Enter new Email:")

            contacts[name]["Phone"]=phone
            contacts[name]["Email"]=email

            print("Contact updated successfully")
        else:
            print("Contact not found")
    elif choice=="5":
        name=input("Enter name to delete:")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully")
        else:
            print("Contact not found")
    elif choice=="6":
        print("Total Contacts:",len(contacts))
    elif choice=="7":
        print("Thank You")
        break
    else:
        print("Invalid Choice")
            
    

            
    

