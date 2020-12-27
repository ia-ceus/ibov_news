# -*- coding: utf-8 -*-
"""
IBOV News

Grupo de Estudos de Inteligência Artificial - CEUS

"""

import pandas as pd
import numpy as np

import yfinance as yf

DELTA = 0.01
DATA_INI = '2000-01-01'
DATA_FIM = '2020-11-01'
TICKER = '^BVSP'

# Funções para criar target

def target_close_maior_open(row, delta):
  if row['Close'] > (1+delta) * row['Open']:
    target = 1
  else:
    target = 0
  return target

def target_high_maior_open(row, delta):
  if row['High'] > (1+delta) * row['Open']:
    target = 1
  else:
    target = 0
  return target

def target_high_igual_open(row, delta):
  if row['High'] == row['Open']:
    target = 1
  else:
    target = 0
  return target

def target_high_menor_open(row, delta):
  if row['High'] <= (1+delta) * row['Open']:
    target = 1
  else:
    target = 0
  return target

# aplicar target

def criar_target(df, tipo=target_close_maior_open, delta=0.01):

    return df.apply(lambda linha: tipo(linha, delta), axis=1)


# baixar dataset yfinance

def download_yf(tkr='^BVSP', dti='2000-01-01', dtf='2020-11-01'):
    
    return yf.download(ticker, start=dti, end=dtf)

