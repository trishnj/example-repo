grid = [["-", "-", "-","#", "#",],

                ["-", "#", "-","-", "-",],

                ["-", "-", "#","-", "-",],

                ["-", "#", "#","-", "-",],

                ["-", "-", "-","-", "-",]]

 

def mine_sweeper(grid):

 

    for row in grid:

        for i in range(len(row)):

            if row[i] == "-":

                row[i] = input("Enter a number:")

 

    for row in grid:          

        print("".join(row))

 

mine_sweeper(grid)