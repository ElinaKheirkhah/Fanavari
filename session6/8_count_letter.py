"""
8_count_letter

yek tabe benevisid ke do voroodi begire, yek kalame va yek horof , var bere beshmore chand ta oon harf dakhele oon kalame hast va oon adad ro khoroji bede.

do bar tabe ro benevisid

a) faghat az for estefade konid

b) az for esteafde nakonid

"""
#a

def count_letter(word: str, chosen_letter: str) -> int:
    '''
    mishmore chantda az un harf tu un kalame hast
    '''
    count = 0
    for letter in word:
        if letter == chosen_letter:
            count = count + 1
    return count

result_1 = count_letter("elina","i")
print(result_1)

result_2 = count_letter("sara","a")
print(result_2)         

#------------------------------------------------------------------------------
#b

#1
def count_letter(word: str, chosen_letter: str) -> int:
    '''
    mishmore chantda az un harf tu un kalame hast
    '''
    splited_word = list(word)
    counted = splited_word.count(chosen_letter)
    return counted

result_1 = count_letter("elina","i")
print(result_1)

result_2 = count_letter("sara","a")
print(result_2)         


#2
def count_letter(word: str, chosen_letter: str) -> int:
    '''
    mishmore chantda az un harf tu un kalame hast
    '''
    counted = word.count(chosen_letter)
    return counted

result_1 = count_letter("elina","i")
print(result_1)

result_2 = count_letter("sara","a")
print(result_2)    

















