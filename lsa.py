#!/usr/bin/python

#implementation of the Latent Semantic Analysis technique for analysis of a Medieval European recipe corpus

import xlrd
import numpy

filename = 'ingredients.xls'
sheet_name = 'ingredients'

'''LOAD THE DATASET'''

#create a vocabulary dictionary, a term list to save all terms, and a document list to save all recipes

wb = xlrd.open_workbook(filename)
ws = wb.sheet_by_name(sheet_name)
vocab = dict()
doct_list = []
term_list = []
num_vocab = 0

#read first cell of each row as num_words (number of ingredients in this row)
#read from first term of last term
#continue if read term is empty or term==None

'''CREATE TERM-DOCUMENT OCCURRENCE MATRIX'''

'''DO SVD DECOMPOSITION OF TERM-DOCUMENT MATRIX'''

'''SET FEATURE DIM TO LATENT SEMANTIC MATRICES'''

'''CREATE LATENT SEMANTIC MATRICES FOR TERMS AND DOCS'''

'''RET INDICES OF MOST SIMILAR TERMS/DOCS to A SELECTED TERM/DOC (COSINE SIMILARITY)'''

'''FIND MOST SIMILAR TOP K TERMS FOR A CHOSEN TERM'''

'''FIND MOST SIMILAR TOP K DOCS FOR CHOSEN DOC'''


