import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pdfkit


#def make_plot(func,dim,deplot,psoplot):
def make_plot(func,dim,deplot):
    title = str(func.func_name)+' '+str(dim) + ' dimensions'
    dexvals = np.linspace(0,3000*dim,len(deplot))
    deyvals = deplot
    #psoyvals = psoplot

    plt.plot(dexvals,deyvals,'b',label='DE')
    #plt.plot(dexvals, deyvals, 'b',dexvals,psoyvals,'r')
    plt.ylabel('Best fitness error so far')
    plt.xlabel('NFC')
    plt.title(title)
    plt.legend(loc='best', ncol=1, mode="expand", shadow=True, fancybox=True)


    plt.savefig('performanceplots/'+title.replace(' ','')+'.png')
    plt.close()

def make_table(func,detable):
    title = str(func.func_name)

    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
    }

    data = prep_table_data(detable)
    data.to_html('table/'+title.replace(' ','')+'.html')
    pdfkit.from_url('table/'+title.replace(' ','')+'.html', 'table/'+title.replace(' ','')+'.pdf',options=options)



def prep_table_data(detables):
    dedatas={}
    for count,detable in enumerate(detables):
        dedata={}
        if count == 0: dim = '2'
        elif count == 1: dim = '5'
        else: dim = '10'
        mean = np.mean(detable)
        worst = np.max(detable)
        best = np.min(detable)
        std = np.std(detable)
        dedata['mean'] = mean
        dedata['worst'] = worst
        dedata['best'] = best
        dedata['std'] = std
        dedatas[dim]=dedata


    psodatas = {}
    for count,psotable in enumerate(detables):
        psodata = {}
        if count == 0: dim = '2'
        elif count == 1: dim = '5'
        else: dim = '10'
        mean = np.mean(psotable)
        worst = np.max(psotable)
        best = np.min(psotable)
        std = np.std(psotable)
        psodata['mean'] = mean
        psodata['worst'] = worst
        psodata['best'] = best
        psodata['std'] = std
        psodatas[dim] =psodata


    dedim2 = pd.DataFrame.from_dict({'val':dedatas['2']},)
    dedim5 = pd.DataFrame.from_dict({'val':dedatas['5']},)
    dedim10 = pd.DataFrame.from_dict({'val':dedatas['10']},)

    psodim2 = pd.DataFrame.from_dict({'val': psodatas['2']}, )
    psodim5 = pd.DataFrame.from_dict({'val': psodatas['5']}, )
    psodim10 = pd.DataFrame.from_dict({'val': psodatas['10']}, )

    df1 = pd.concat([dedim2,dedim5,dedim10],axis=0,keys=['2','5','10'],)
    df2 = pd.concat([psodim2,psodim5,psodim10],axis=0,keys=['2','5','10'],)
    df = pd.concat([df1,df2], axis=1, keys=['DE', 'PSO'])

    return df












