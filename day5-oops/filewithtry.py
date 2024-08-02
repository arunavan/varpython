try:
   file = open("example.txt", "w")
   file.write("This is an example with exception handling.")
finally:
   file.close()
   print ("File closed successfully!!")