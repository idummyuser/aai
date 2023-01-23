#Joint Probability

cardnumber = input("Enter number of Card ")
cardcolor = input("Enter color of Card ")

pofA = 4/52
pofB = 26/52

print("p(A)=>Probability of drawing card with number ",cardnumber," = ",round(pofA,2))
print("p(B)=>Probability of drawing card with color ",cardnumber," = ",round(pofB,2))

print("Joint Probability of A and B = P(A) * P(B)")

pAandB = round(pofA * pofB, 2)
print("P(A and B)=",pAandB)

print("There are ",pAandB*100," % chances that of getting",cardcolor," card with number",cardnumber)
