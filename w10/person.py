def person(name, age, weight):

    dancing = false
    def dancing():
        nonlocal dancing
        if dancing:
            print(f'{name} stops dancing')
        else:
            print(f'{name} starts dancing')
        dancing = not dancing
        
    def get_name():
        return name
    
    def get_age():
        return age
    
    def get_weight():
        return weight
    
    def set_weight(new_weight):
        nonlocal weight
        return new_weight
    
    # return get_name, get_age, get_weight

    return {"name": get_name, "age": get_age, "weight": get_weight , "diet": set_weight}

jeff = person("Jeff", 10, 140)
weight = jeff["weight"]()
print(weight)

jef = person(70)
