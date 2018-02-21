#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MHD
#
# Created:     20/02/2018
# Copyright:   (c) MHD 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#*********************************************************** Variable Types
x_int = 10              # integer
y_flt = 10.0            # float
z_cmplx = 1.5+3.4j      # complex
s_str = "Hello World"   # string

# multiple assignments. a is hex and b is floating number
a, b, c = 0x123, -2.3e12, "Great Pythonn!"

print(s_str)
print(s_str[6])
print(s_str[6:])
print(s_str*3)
print(s_str + "-TESTED")
print("**************************************")

#******************************************************************* List
# similar to arrays in C
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print(list[-1])       # Prints the last element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists
print("**************************************")

#******************************************************************* Tuples
# tuples are similar to list, but tuple's elements and size can't be
# updated. thus, read-only list

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)           # Prints complete tuple
print (tuple[0])        # Prints first element of the tuple
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints tuple two times
print (tuple + tinytuple) # Prints concatenated tuple
print("**************************************")

#*************************************************************** Dictionary
# key-value pairs like hashes and and associative arrays

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values
