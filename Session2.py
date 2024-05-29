# create a simple calculator
first_num = 6   #first number value assigned
sec_num = 2     # assigned the second number
division = first_num / sec_num
print(division)

multi = first_num * sec_num
subs = first_num - sec_num
add = first_num + sec_num
print(division, multi, subs, add)

divsion = first_num / sec_num
multi = first_num * sec_num
add = first_num + sec_num
subs = first_num + sec_num
print("The calculation is as follows: ",division, multi, add, subs)

divsion = (int(first_num)) / (int(sec_num))
multi = (int(first_num)) * (int(sec_num))
add = (int(first_num)) + (int(sec_num))
subs = (int(first_num)) - (int(sec_num))
print(division, multi, add, subs)

divsion = (int(first_num)) / (int(sec_num))
multi = (int(first_num)) * (int(sec_num))
add = (int(first_num)) + (int(sec_num))
subs = (int(first_num)) - (int(sec_num))
expo = (int(first_num)) ** (int(sec_num))
modu = (int(first_num)) % (int(sec_num))
fdivi = (int(first_num)) // (int(sec_num))
print("============AIH===========")
print("============Student Name==========")
print("Addition: ", add, "Division: ", division, "Multiplication: ", multi, "Substract: ", subs, "Exponential: ", expo, "Modulation: ", modu, "Fdivision: ",fdivi)

# lets bassume some xyz company three products
phone = 1400 #10 initializing frist variable or product
laptop = 2000 #20 initializing second variable or product
watch = 1500 #8 initializing third variable or product
airpods = 200 #13 initializing forth variable or product
tv = 6000 #8 initializing fifth variable or product

st_phones = phone*1.1
st_laptops = laptop*1.2
st_watch = watch*1.08
st_airpods = airpods*1.13
st_tv = tv*1.08
print (st_phones, st_laptops, st_watch, st_airpods, st_tv) 

firstly = input("what is the number?: ")
secondly = input("what is your name?: ")
print(firstly,secondly) 

import statistics

#initializing list
li = [11,22,33,33,22,21,26,15]

#using mode() to calculate average of list
#eleminates
print("The average of list value is : ", end="")  #print statements
print(statistics.mean(li))

print("The average of list value is : ", end="")  #print statements
print(statistics.median(li))

print("The average of list value is : ", end="")  #print statements
print(statistics.mode(li))

#defining a function

def is_palindrome(word):
x = 0
for i in range (len(word)/2):
    if (word[x]) == (word[len(word)-x-1]):
        x+=1
        if x == (len(word)/2):
            result True
            result False 
