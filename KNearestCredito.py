# %% Imports
# =============================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sklearn

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 150)

# %% Importando arquivo
# =============================================================================

fileColumns = {
    'RowID'						: 'object',
    'Report Date'				: 'object',
    'KeyARInvoiceComposite'		: 'object',
    'KeyShipmentHeader'			: 'object',
    'KeyBillToCustomer'			: 'object',
    'KeyReseller'				: 'object',
    'KeyAROverdueRange'			: 'object',
    'Company Code'				: 'object',
    'Customer Nbr'				: 'object',
    'Reseller Nbr'				: 'object',
    'Currency Code'				: 'object',
    'Customer Order Nbr'		: 'object',
    'Invoice Nbr'				: 'object',
    'Invoice Date'				: 'object',
    'Shipment Invoice Date'		: 'object',
    'AR Invoice Date'			: 'object',
    'Due Date'					: 'object',
    'Payment Date'				: 'object',
    'Pay Sequence Nbr'			: 'object',
    'Terms Code'				: 'object',
    'KeyVendor'					: 'object',
    'Invoice Amount'			: 'object',
    'Invoice Remaining Amount'	: 'object',
    'Payment Interest Amount'	: 'object',
    'Terms Days'				: 'object',
    'Days Open'					: 'object',
    'Days Overdue'				: 'object',
    'Terms Avg Calc'			: 'object',
    'Terms Avg Calc Real'		: 'object',
    'Valid for Terms Calc'		: 'object',
    'Is New Customer In AR'		: 'object',
    'Is New Invoice In AR'		: 'object',
    'Is New Overdue Customer'	: 'object',
    'Is New Overdue Invoice'		: 'object',
    'Is Removed Customer From AR'	: 'object',
    'Is Removed Invoice From AR'	: 'object',
    'Previous Report Date'			: 'object',
    'Payment Status'			: 'object',
    'Year'						: 'object',
    'Month'						: 'object',
    'Current Year Difference'	: 'object',
    'Current Month Difference'	: 'object',
    'Customer City'				: 'object',
    'Customer CNPJ'				: 'object',
    'Customer Group Nbr'		: 'object',
    'Customer Address'			: 'object',
    'Customer ZIP'				: 'object',
    'Customer State'			: 'object'
}


arquivoBase = pd.read_csv("ARData.txt", delimiter = "\t", dtype = fileColumns)
arquivoLastDate = arquivoBase['Report Date'].max()

workFile = arquivoBase[arquivoBase['Report Date'] == arquivoLastDate]

workFile.head(10)


#%% teste
# =============================================================================
aa
