def encoder(ch):
# Function used to attach values to elements of a list for advanced sorting
# Priority: 1) lowercase letters, 2) Uppercase, 3) Odd numbers, 4) Even numbers
   if ch.isalpha():
       if ch.isupper():
       	   return ord(ch)-ord('A')+26
        else:
            return ord(ch)-ord('a')
    else: 
        if int(ch) % 2 == 0:
            return int(ch)+78
        else:
            return int(ch)+52


list_in = ''
while True:
    try:
        lis = str(input())
	list_in += lis
    except EOFError:
        break

unique_line = list_in.split('\n')

for line in unique_line:
    sorted_list = sorted(line, key=encoder)
    print (*sorted_list, sep='')