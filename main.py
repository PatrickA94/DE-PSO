import numpy as np
from Functions import *
from DE2 import optimize
from figgen import make_plot, make_table

def main():
    dims = [2,5,10]

    funcs =[highCond,]

    tablesmax = []
    tablesmin = []
    tablesmean = []
    tablesstd = []
    for func in funcs:
        for dim in dims:
            plot,tablemax,tablemin,tablemean,tablestd = optimize(dim,func)
            make_plot(func,dim,plot)
            tablesmax.append(tablemax)
            tablesmin.append(tablemin)
            tablesmean.append(tablemean)
            tablesstd.append(tablestd)
            print('completed ', str(func.func_name), ' ', str(dim) )

        make_table(func,tablesmax,tablesmin,tablesmean,tablesstd)

if __name__ == '__main__':
    main()
