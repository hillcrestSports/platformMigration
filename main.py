# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:41:43 2020

@author: Web
"""
from spydercustomize import runfile
import numpy as np

#run 
if __name__ == '__main__':
        
    
    print('loading brand and category dicts from excel files')
    runfile('C:/Users/robbi/CODE/bigCommerceUpload/dicts.py', \
            wdir='C:/Users/robbi/CODE/bigCommerceUpload')
    
    print('running from Retail Pro ~BRIDGE')
    runfile('C:/Users/robbi/CODE/bigCommerceUpload/dataPrep.py', \
            wdir='C:/Users/robbi/CODE/bigCommerceUpload')
    print('running from Magento CSV Export')
    runfile('C:/Users/robbi/CODE/bigCommerceUpload/magento.py', \
            wdir='C:/Users/robbi/CODE/bigCommerceUpload')
    print('running from RDi INVEN/IMAGES')
    runfile('C:/Users/robbi/CODE/bigCommerceUpload/fromRpro.py', \
            wdir='C:/Users/robbi/CODE/bigCommerceUpload')
    print('running from Octoparse scraping data')
    runfile('C:/Users/robbi/CODE/bigCommerceUpload/scrape.py', \
            wdir='C:/Users/robbi/CODE/bigCommerceUpload')
    
        
    print('merging dataframes')
    
    # runfile('C:/Users/robbi/CODE/bigCommerceUpload/merge.py', \
    #         wdir='C:/Users/robbi/CODE/bigCommerceUpload')
        
    from merge import webDf
    """filtering and tuning descriptions"""
    #MAKE IT TODAY MINUS A YEAR FOR GOD'S SAKE    
    
    df = webDf.loc[(webDf.qty>0) | (webDf.lSold > '04-14-2019')]
    df.desc = np.where(df.desc.isnull(),df.desc_short,df.desc)
    df.desc = np.where(df.desc.isnull(),df.descriptionA,df.desc)

    df.to_pickle('mergedDf')

    print('***********configuring product options, please hold************'\
          .upper())
    runfile('C:/Users/robbi/CODE/bigCommerceUpload/options.py', \
            wdir='C:/Users/robbi/CODE/bigCommerceUpload')
    
    print('preparing bigCommerce upload file df as "out"')
    
    # runfile('C:/Users/robbi/CODE/bigCommerceUpload/excelPrep.py', \
    #         wdir='C:/Users/robbi/CODE/bigCommerceUpload')
    
    from excelPrep import out
    out.to_csv('upload.csv', quotechar="\"")
