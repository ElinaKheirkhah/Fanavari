"""
9_find_max

yek tabe benvisid ke yek listi az adad begire va bozorgtarin adad ro peyda kone va khoroji bede.

in tabe dar asl kare tabeye dakhelie max() ro anjam mide , pas ejaze nadarid az max() estefade konid .

"""

def find_max(numbers_list : list) -> float:
    '''
    voroodi list migire va bozorg tarinesho be onvane khorooji mide
    '''
    numbers_list.sort()
    return numbers_list[-1]

result_1 = find_max([10,60,52.36,-96,94,-88,3,-745.2])
print(result_1)

result_2 = find_max([20,96,84,52,14])
print(result_2)   

