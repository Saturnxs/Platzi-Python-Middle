def run():
    set_a = {'col', 'mex', 'bol'}
    set_b = {'pe', 'bol'}
    
    
    # UNIONS
    
    # Union with union() method
    set_c = set_a.union(set_b)
    print('Union with union() method:',set_c)
    
    # Union with | operator
    set_d = set_a | set_b
    print('Union with | operator:',set_d)
    
    
    
    # INTERSECTION
    
    # Intersection with intersection() method
    set_c = set_a.intersection(set_b)
    print('Intersection with intersection() method:',set_c)
    
    # Intersection with & operator
    set_d = set_a & set_b
    print('Intersection with & operator:',set_d)
    
    
    
    # DIFFERENCE
    
    # Difference with difference() method
    set_c = set_a.difference(set_b)
    set_d = set_b.difference(set_a)

    print('A difference B with difference() method:',set_c)
    print('B difference A with difference() method:',set_d)
    
    # Difference with - operator
    set_c = set_a - set_b
    set_d = set_b - set_a
    print('A difference B with - operator:',set_c)
    print('B difference A with - operator:',set_d)
    
    
    # Symmetric Difference
    
    # Symmetric difference with symmetric_difference() method
    set_c = set_a.symmetric_difference(set_b)
    set_d = set_b.symmetric_difference(set_a)

    print('A symmetric difference B with symmetric_difference() method:',set_c)
    print('B symmetric difference A with symmetric_difference() method:',set_d)
    
    # Symmetric difference with ^ operator
    set_c = set_a ^ set_b
    set_d = set_b ^ set_a
    print('A symmetric difference B with ^ operator:',set_c)
    print('B symmetric difference A with ^ operator:',set_d)


if __name__ == "__main__":
    run()