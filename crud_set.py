def run():
    set_countries = {'col', 'mex', 'bol'}

    size = len(set_countries)
    print('Set size:',size)

    print('col' in set_countries)
    print('pe' in set_countries)


    # ADD

    set_countries.add('pe')
    print('Add set_countries',set_countries)
    print('pe' in set_countries)


    # UPDATE

    set_countries.update({'ar', 'ecua', 'pe'})
    print('Update set_countries',set_countries)
    
    
    # REMOVE
    
    set_countries.remove('col')
    print('Remove set_countries',set_countries)
    
    # DISCRD
    
    set_countries.discard('arg')
    print('Discard set_countries', set_countries)
    
    
    # CLEAR
    
    set_countries.clear()
    print('Set clear() len', len(set_countries))
    
        
        
        
if __name__ == "__main__":
    run()