#Optional 1

'''
Tabe ei besazid bename even_numbers ke vorodi yek adad bename n daryaft kone
va ba estefade az dastoore yield , adade zoj ro az 2 ta n yeki yeki tolid kone

sepas yek generator besazido dakhele yek moteghayer gahrar dahid va ba next() 3 meghdare aval ro namayesh dahid

'''

def even_numbers(n):
    for even_num in range(2,n,2):
        yield even_num


test_even_number = even_numbers(9)

print(test_even_number) #<generator object even_numbers at 0x0000018EE9325A80>

next(test_even_number) #2

next(test_even_number) #4

next(test_even_number) #6

next(test_even_number) #8

next(test_even_number) #StopIteration









