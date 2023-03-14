

def roll_call_dwarves( some_list ):
    for count, one_name in enumerate( some_list, start = 1 ):
        print( f"{count}. {one_name}" )
        




def summon_captain_planet( some_list ):
    new_list = []
    for the_word in some_list:
        new_string = f"{the_word.capitalize()}!"
        new_list.append( new_string )
    return new_list







def long_planeteer_calls( some_list ):
    for the_word in some_list:
        if len( the_word ) > 4:
            return True
    return False
    





def find_the_cheese( some_list ):
    the_cheeses = [ "cheddar", "gouda", "camembert" ]
    for the_snack in some_list:
        if the_snack in the_cheeses:
            return the_snack
    return None
   
