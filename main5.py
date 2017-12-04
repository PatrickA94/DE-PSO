import numpy as np
from Functions import *
from DE import optimize
from PSO3 import opt
from figgen import make_plot, make_table
import cProfile

def main():
    dims = [2,5,10]

    funcs =[griewank]


    for func in funcs:
        tablesmax = []
        tablesmin = []
        tablesmean = []
        tablesstd = []
        tablesmaxp = []
        tablesminp = []
        tablesmeanp = []
        tablesstdp = []
        for dim in dims:
            plot,tablemin,tablemax,tablemean,tablestd = optimize(dim,func)
            plotp,tableminp,tablemaxp,tablemeanp,tablestdp = opt(dim,func)


            make_plot(func,dim,plot,plotp)
            #make_plot(func,dim,plot)
            #DO
            tablesmax.append(tablemax)
            tablesmin.append(tablemin)
            tablesmean.append(tablemean)
            tablesstd.append(tablestd)
            #PSO
            tablesmaxp.append(tablemaxp)
            tablesminp.append(tableminp)
            tablesmeanp.append(tablemeanp)
            tablesstdp.append(tablestdp)
            print('completed ', str(func.func_name), ' ', str(dim) )

        make_table(func,tablesmax,tablesmin,tablesmean,tablesstd,tablesmaxp,tablesminp,tablesmeanp,tablesstdp)

        #make_table(func,tablesmaxp,tablesminp,tablesmeanp,tablesstdp)

# if __name__ == '__main__':
#     main()

cProfile.run('main()',sort="tottime")

