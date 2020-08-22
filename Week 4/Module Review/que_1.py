def format_address(address_string):
      # Declare variables
  words = address_string.split()
  house_no = 0
  rem_add = ""
  # Separate the address string into parts

  # Traverse through the address parts
  for word in words:
    if word.isdigit():
      house_no = word
    else:
      rem_add += word + " "
    # Determine if the address part is the
    # house number or part of the street name

  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(house_no,rem_add)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
