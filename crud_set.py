def run():
    set_countries = {'col', 'mex', 'bol'}

    size = len(set_countries)
    print('Set size:',size)

    print('col' in set_countries)
    print('pe' in set_countries)


    # ADD

    # Adding the country Peru to the set.
    set_countries.add('pe')
    print('Add set_countries',set_countries)
    print('pe' in set_countries)


    # UPDATE

    # Adding the elements in the set to the set_countries set.
    set_countries.update({'ar', 'ecua', 'pe'})
    print('Update set_countries',set_countries)
    
    
    # REMOVE
    
    # Removing the element 'col' from the set.
    set_countries.remove('col')
    print('Remove set_countries',set_countries)
    
    # DISCARD
    
    # Removing the element 'arg' from the set.
    set_countries.discard('arg')
    print('Discard set_countries', set_countries)
    
    
    # CLEAR
    
    # Clearing the set.
    set_countries.clear()
    print('Set clear() len', len(set_countries))
    
        
        
        
if __name__ == "__main__":
    run()