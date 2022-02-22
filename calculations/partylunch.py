

croissant = 0.39
baguette = 2.78
discount = -0.50
myOrder ="De feestlunch kost je bij de bakker {} euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!"

TOTAL = 17*croissant+2*baguette+3*discount#3*ENTRANCE+27*VIP_VR

#print(str(TOTAL)+" is het totale bedrag wat u moet betalen")#ANSWER IS 32.34
print(myOrder.format(TOTAL))