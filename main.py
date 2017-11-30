import numpy as np
from Functions import *
from DE import optimize
from figgen import make_plot, make_table

def main():
    dims = [2,5,10]

    funcs =[highCond,bentCig,discus,rosen]

    tables = []
    for func in funcs:
        for dim in dims:
            plot,table = optimize(dim,func)
            make_plot(func,dim,plot)
            tables.append(table)
            print('completed ', str(func.func_name), ' ', str(dim) )

        make_table(func,tables)

if __name__ == '__main__':
    main()
