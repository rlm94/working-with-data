VIP_VR = 0.37
ENTRANCE = 7.45
myOrder = "Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar {} euro"
TOTAL = round(4*ENTRANCE+36*VIP_VR, 2)

#print(str(TOTAL)+" is het totale bedrag wat u moet betalen")#ANSWER IS 32.34
print(myOrder.format(TOTAL))
print(type(TOTAL))