def is_factor(number, possible_factor):
    if number % possible_factor == 0:
        return 1
    else:
        return 0

print is_factor(100, 10)

def evenly_divisible(number, possible_factor1, possible_factor2, possible_factor3, possible_factor4, possible_factor5, possible_factor6, possible_factor7, possible_factor8, possible_factor9, possible_factor10, possible_factor11, possible_factor12, possible_factor13, possible_factor14, possible_factor15, possible_factor16, possible_factor17, possible_factor18, possible_factor19, possible_factor20):
    count_factors = is_factor(number, possible_factor1) + is_factor(number, possible_factor2)+ is_factor(number, possible_factor3)+ is_factor(number, possible_factor4)+ is_factor(number, possible_factor5)+ is_factor(number, possible_factor6)+ is_factor(number, possible_factor7)+ is_factor(number, possible_factor8)+ is_factor(number, possible_factor9)+ is_factor(number, possible_factor10)+ is_factor(number, possible_factor11)+ is_factor(number, possible_factor12)+ is_factor(number, possible_factor13)+ is_factor(number, possible_factor14)+ is_factor(number, possible_factor15)+ is_factor(number, possible_factor16)+ is_factor(number, possible_factor17)+ is_factor(number, possible_factor18)+ is_factor(number, possible_factor19)+ is_factor(number, possible_factor20)
    if count_factors == 20:
        return 1
