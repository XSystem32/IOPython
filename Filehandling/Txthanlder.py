
stars = 'star.txt'
with open(stars, mode='r+') as my_file:
    #text = my_file.write('VY Canis Majoris is a stellar goliath, a red hypergiant, one of the largest known stars in the Milky Way. It is 30–40 times the mass of the Sun and 300,000 times more luminous. In its current state, the star would encompass the orbit of Jupiter, having expanded tremendously as it enters the final stages of its life.')
    print(my_file.read())



with open('star.txt', 'r') as searchfile:
    for line in searchfile:
        if 'goliath' in line:
            print (line)