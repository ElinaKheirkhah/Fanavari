"""
10_avarage

yek tabe benevisit ke yek listi az nomarat begire va mianginesh ro hesab kone

ejaze nadarid az tavabe ye dakheli mesle sum() estefade konid.

"""

def average(scores_list : list) -> float:
    '''
    voroodi listi az nomarat migire va mianginesho be onvane khorooji mide
    '''
    tedade_nomarat = 0
    majmoe_nomarat = 0
    for score in scores_list:
        tedade_nomarat = tedade_nomarat + 1
        majmoe_nomarat = majmoe_nomarat + score
    miangin = majmoe_nomarat / tedade_nomarat    
    return miangin

result_1 = average([65,84,76,92])
print(result_1)

result_2 = average([20,20])
print(result_2)   

