# amazon free shipping eligibility
# prime customers OR purchases of over $25
# under 18, you need parent consent to purchase


def free_shipping(prime,cost,age,consent) :
    if (prime==True or cost >=25) and (age>= 18 or consent == True):
        print("free shipping applied")

    else:
        print("ineligible for free shipping..")
p = True
cos = 18
a = 25
con = False

free_shipping(p, cos, a, con )
