# entry = input('I\'m waiting for text...\n').lower()
# num_a=0; num_e=0; num_y=0; num_u=0; num_o=0; num_i=0;
# for i in entry:
#     if i=='a': num_a+=1
#     elif i=='e': num_e+=1
#     elif i=='y': num_y+=1
#     elif i=='u': num_u+=1
#     elif i=='i': num_i+=1
#     elif i=='o': num_o+=1
# print (f'a={num_a}, e={num_e}, y={num_y}, u={num_u}, i={num_i}, o={num_o}')

letters = {'a':0, 'e':0,'y':0,'u':0,'i':0,'o':0}
entry = input('I\'m waiting for text...\n').lower()
for i in entry:
    if i in letters.keys():
        letters[f'{i}']+=1
print (letters)
