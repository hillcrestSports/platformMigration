# -*- coding: utf-8 -*-

import pandas as pd
df = pd.read_pickle('optionDf')


data = pd.read_csv('uploadTemplateOriginal.csv')
cols = list(data.columns)
out = pd.DataFrame(columns = cols)

"""
styleSID
sku
UPC
itemSID
CAT
BRAND
name
year
weight
qty
cost
pSale
pMSRP
pMAP
pAmazon
pSWAP
fRcvd
lRcvd
lSold
lEdit
image_1
image_2
image_3
image_4
image_5
image_6
image
description
short_description
color
size
"""

"""
Item Type
Product ID
Product Name
Product Type
Product Code/SKU
Bin Picking Number
Brand Name
Option Set
Option Set Align
Product Description
Price
Cost Price
Retail Price
Sale Price
Fixed Shipping Cost
Free Shipping
Product Warranty
Product Weight
Product Width
Product Height
Product Depth
Allow Purchases?
Product Visible?
Product Availability
Track Inventory
Current Stock Level
Low Stock Level
Category
Product Image ID - 1
Product Image File - 1
Product Image Description - 1
Product Image Is Thumbnail - 1
Product Image Sort - 1
Product Image ID - 2
Product Image File - 2
Product Image Description - 2
Product Image Is Thumbnail - 2
Product Image Sort - 2
Search Keywords
Page Title
Meta Keywords
Meta Description
MYOB Asset Acct
MYOB Income Acct
MYOB Expense Acct
Product Condition
Show Product Condition?
Event Date Required?
Event Date Name
Event Date Is Limited?
Event Date Start Date
Event Date End Date
Sort Order
Product Tax Class
Product UPC/EAN
Stop Processing Rules
Product URL
Redirect Old URL?
GPS Global Trade Item Number
GPS Manufacturer Part Number
GPS Gender
GPS Age Group
GPS Color
GPS Size
GPS Material
GPS Pattern
GPS Item Group ID
GPS Category
GPS Enabled
"""

#monies
out["Cost Price"] = df["cost"]
out["Retail Price"] = df["pMSRP"]
out["Sale Price"] = df["pSale"]

#name
out["Product Name"] = df.webName

#images
    #needs descriptions
out["Product Image File - 1"] = df.image
out[[f'Product Image File - {i+2}' for i in range(5)]]\
    = df[[f'image_{i}' for i in range(5)]]
out = out.reindex(out.columns.to_list()\
                  +[f"Product Image ID - {i}" for i in range(2,6)]\
                  +[f'Product Image Description - {i}' for i in range(2,6)],\
                      axis=1)

#descriptions
out['Product Description'] = df.desc

out["Brand Name"] = df.BRAND
out["Category"] = df.CAT
out["Current Stock Level"] = df.qty
out["Product Code/SKU"] = df.sku
out["Product UPC/EAN"] = df.UPC
# out["Product Custom Fields"] = df.PCF

out["Product Weight"] = df.weight
# out["Product URL"] = df.url_path


#defaults

out["Allow Purchases?"] = 'Y'
out["Item Type"] = df.itemType
out["Product Type"] = 'P'
out["Track Inventory"] = 'by product'


#drop na








######################
#
#       UPLOAD
#
#########################

#so far
"""
Item Type
Product Name
Product Type
Product Code/SKU
Brand Name
Product Description
Cost Price
Retail Price
Sale Price
Allow Purchases?
Track Inventory
Current Stock Level
Category
Product UPC/EAN
Product Image File - 1
Product Image File - 2
Product Image File - 3
Product Image File - 4
Product Image File - 5
Product Image File - 6
"""

"""uncomment to run outside of main"""
# out.to_csv('upload.csv', quotechar="\"")

#dulplicates, not imported (dupicate sku):
"""
Line 6860 Gore-Tex Linear Mitt 18-19 L Black
Line 4876 Base 2.0 Legging 19-20 L Black
Line 1846 Minimalist Pant 19-20 L Black
Line 4874 Base 2.0 Legging 19-20 S Black
Line 5700 PreCip Eco Pant 19-20 M Black
Line 2684 Warden 11 MNC 20-21 90mm Black
Line 2319 Warden 11 MNC 20-21 90mm Black
Line 1218 Legendary Pant 18-19 L Black
Line 4877 Base 2.0 Legging 19-20 XL Black
Line 5279 Gore-tex Linear Glove 18-19 M Black
Line 3917 Gore Glove 19-20 M TruBlk
Line 6160 Gore Glove 18-19 XL BogHea
Line 5701 PreCip Eco Pant 19-20 L Black
Line 5280 Gore-tex Linear Glove 18-19 L Black
Line 6159 Gore Glove 18-19 L BogHea
Line 6859 Gore-Tex Linear Mitt 18-19 M Black
Line 6157 Gore Glove 18-19 S BogHea
Line 2683 Warden 11 MNC 20-21 100mm Black
Line 3916 Gore Glove 19-20 S TruBlk
Line 6158 Gore Glove 18-19 M BogHea
Line 4875 Base 2.0 Legging 19-20 M Black
Line 6552 Randonnee Glove 19-20 M Black
Line 6553 Randonnee Glove 19-20 L Black
Line 1217 Legendary Pant 18-19 M Black
Line 3915 Gore Glove 19-20 XS TruBlk
Line 2320 Warden 11 MNC 20-21 100mm Black
Line 1845 Minimalist Pant 19-20 M Black
Line 2893 Z 12 19-20 90mm Black/ White
Line 4130 Vandal Boot 19-20 7 Black
"""
