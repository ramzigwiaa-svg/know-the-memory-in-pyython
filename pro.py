import sys
my_program="entrer your favouroute"
text_size=sys.getsizeof(my_program)
print(f"{my_program} byte {text_size}")
del my_program
print(my_program)
