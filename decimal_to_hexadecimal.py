#It is used to convert decimal number to hexa decimal number system
conversion_table={0 : '0', 1 : '1', 2 : '2' ,3 : '3' ,4 : '4' ,5 : '5',6 : '6' ,7 : '7' ,8 : '8' ,
9 : '9' ,10 : 'A' ,11 : 'B' ,12 : 'C' ,13 : 'D' ,14 : 'E' ,15 :'F' }
#This function is used to converter of Hexadecimal
def converterofhexadecimal(decimal):
    hexa = ''
    while(decimal > 0):
        reminder = decimal % 16
        hexa = conversion_table[reminder] + hexa
        decimal = decimal // 16
    return hexa
#Taking input from the user to convert the value 
decimal_num=int(input('Enter your decimal value :'))
#In this we can see the output of the conversional hexa decimal operator
print('The hexa decimal form of',decimal_num,'is',converterofhexadecimal(decimal_num))