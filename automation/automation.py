from os import replace
import shutil
import re

with open('assetes/potential-contacts.txt', 'r') as file:
    data = file.read().replace('\n', '')
phonePattern = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
emailPattern = r'[a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+'


def emailfind():
    mydata = re.findall(emailPattern , data)
    mydata.sort()
    desiredData = []
    for ele in mydata:
        if ele not in desiredData:
            desiredData.append(ele)

    with open("email.txt","w+") as file:
        for item in desiredData:
            file.write(f"{item}\n")

def splitAt(w,n):
    for i in range(0,len(w),n):
        yield w[i:i+n]

def phonefind():
    match_phone_number = re.findall( r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', data )
    
    phoneNums = []

    for num in match_phone_number:
        
        num = num.replace( "(", "" )
        num = num.replace( ")", "-" )
        num = num.replace( ".", "-" )

        if len( num ) == 10:
            num = f"{num[:3]}-{num[3:6]}-{num[6:]}"
        if not num in phoneNums:
            phoneNums.append( num )

    phoneNums = sorted(phoneNums)

    with open("phone.txt","w+") as file:
        for item in phoneNums:
            file.write(f"{item}\n")
#strip() method in-built function of Python is used to remove all the leading and trailing spaces from a string

emailfind()
phonefind()