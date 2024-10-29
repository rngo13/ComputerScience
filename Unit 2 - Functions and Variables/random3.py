def people_with_age_drink(age):
    if age<14:
        print("drink toddy")
        
    elif age<18 and age>=14:
        print("drink coke")
    
    elif age<21 and age>=18:
        print("drink beer")
        
    elif age>=21:
        print("drink whiskey")


people_with_age_drink(15)