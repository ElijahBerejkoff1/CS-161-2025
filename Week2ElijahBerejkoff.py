#Step 1, print a variable into binary and hex form
x = 10
print ("Part 1")
print (x, bin(x), hex(x))

#Step 2, identify error
#y = 1.25
#print ("/nPart 2")
#print (y, bin(y), hex(y))
#error is: 'float' object cannot be interprated as an integer.
#This is happaning becuase decimles cannot be represented in standerd binary and hex.
#A float is a number with decimal

#Step 3, assign a var hex or binary value
a = 0b1100100
b = 0xAA
print ("Part 3")
print (a, b)

#Step 4, mess around with it
w = x + b * a - (a * b + x) + 1
print ("Part 4")
print (w)
print (f"The answer to  x + b * a - (a * b + x) + 1 ... is: {w}")

#Part 2 compression
#Step 1, Choose meaningful variable names
original_size = 255
dictionary_size = 2
compressed_text_size = 8

#step 2, calculate
xa = 1 - ((compressed_text_size + dictionary_size) / original_size)
print ("Part 1")
print(f"You get {xa} or {xa * 100}%")
#answer is 0.9607843137254902
#if my dictionary size is higher, say 155:
dictionary_size1 = 155
xb = 1 - ((compressed_text_size + dictionary_size1) / original_size)
print ("Part 1 1/2")
print (f" If dictionary size is 155 you get: {xb}. So {xb * 100}%")
#Step 3, final print
print("Step 3")
print (f"Compressed text size: {compressed_text_size} characters")
print (f"     Dictionary size: {dictionary_size} characters")
print (f"       Original size: {original_size} characters")
print (f"         Compression: {xa * 100}%")