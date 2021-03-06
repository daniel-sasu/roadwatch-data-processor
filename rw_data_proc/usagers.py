#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
.. module:: usagers
   :platform: Unix, Windows
   :synopsis: A list of modifiers for 'usagers' files

.. moduleauthor:: Daniel SASU <daniel.sasu@mail.com>

"""
import pandas as pd
import numpy as np
import datetime
from rw_data_proc.core import process_generic_file

U_DTYPE = {
           'Num_Acc': int, 'place': pd.Int64Dtype(), 'num_veh': str,
           'catu': pd.Int64Dtype(), 'grav': pd.Int64Dtype(),'sexe': pd.Int64Dtype(),
           'an_nais': pd.Int64Dtype(), 'trajet': pd.Int64Dtype(), 'secu': pd.Int64Dtype(),
           'locp': pd.Int64Dtype(), 'actp': pd.Int64Dtype(), 'etatp': pd.Int64Dtype()
}

U_PYTYPE = {
           'accident_id': int, 'place': int, 'num_veh': str,
           'catu': int, 'grav': int,'sexe': int,
           'an_nais': int, 'trajet': int, 'secu': int,
           'locp': int, 'actp': int, 'etatp': int
}

COL_RENAME = [
    {'Num_Acc': 'accident_id'}
]

COLS_FORMATTED = []
U_MODIFIERS = {}
COLS_DROP = []

def process(path, index=None, encoding='latin-1', sep=',', dtype=U_DTYPE,
            col_rename=COL_RENAME, cols_formatted=COLS_FORMATTED, modifiers=U_MODIFIERS, drop_cols=COLS_DROP):
    """
    Process a caractristics file.

    :param path: csv file path
    :type path: str
    :param index: index column
    :type index: str
    :param encoding: file encoding
    :type encoding: string
    :param sep: column separator
    :type sep: str
    :param dtype: data types for columns, the same structure as for pandas
    :type dtype: dict
    :param col_rename: a list of dict of the form { <old name>: <new name> }
    :type col_rename: list
    :param cols_formatted: column order
    :type cols_formatted: list
    :param modifiers: a set of modifier functions
    :type modifiers: dict
    :param drop_cols: a list of columns to be dropped
    :type drop_cols: list
    :returns: a processed dataFrame
    :rtype: pandas.DataFrame
    """
    df = process_generic_file(path, index, encoding, sep, dtype, col_rename,
                                cols_formatted, modifiers, drop_cols)

    df.fillna(0, inplace=True)
    df = df.astype(U_PYTYPE)
    df.replace({0: None}, inplace=True)

    return df
