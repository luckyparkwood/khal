#number = str(846)
number = input("Enter a number 1 - 999: ")
num_len = len(number)

ones_place = 0
tens_place = 0
hundreds_place = 0

if num_len >= 1:
    ones_place = number[-1]
if num_len >= 2:
    tens_place = number[-2]
if num_len >= 3:
    hundreds_place = number[-3]

#spelling
#ones
ones_spell = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#tens
tens_spell = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
#zeroflags
ten_flag = ["", "-"]
hundred_flag = ["", "-hundred and "]

#spell checks
#teen exceptions
if 11 <= int(number) <= 19:
    tens_spell = ["", "", "", "", "", "", "", "", "", ""]
    ones_spell = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    ten_flag = ["", ""]

if int(hundreds_place) == 0:
    hundred_flag = ["", ""]
if int(tens_place) == 0 or int(ones_place) == 0:
    ten_flag = ["", ""]

#full_spell
full_spell = str(ones_spell[int(hundreds_place)]) + str(hundred_flag[1]) + str(tens_spell[int(tens_place)]) + str(ten_flag[1]) + str(ones_spell[int(ones_place)])

if int(number) == 69:
    full_spell = "nice"
if int(number) == 420:
    full_spell = "blaze it"
if int(number) == 666:
    full_spell = "the number of the beast"

print(str(full_spell))
