#!/usr/bin/env python2

import validator
import pandas as pd 
from schema import Schema
from report import Report
from pprint import pprint

if __name__ == "__main__":

    test_file = pd.read_csv('data/test_data.csv')

    rules = {
        'age': {
            'codes': False,
            'dtype': int,
            'range': False,
            'length': 2,
            'regex': False,
            'required': True
        },
        'exp': {
            'codes': False,
            'dtype': int,
            'range': [0, 20],
            'length': 2,
            'regex': False,
            'required': False
        },
        'first_name': {
            'codes': False,
            'dtype': str,
            'range': False,
            'length': 30,
            'regex': False,
            'required': True
        },
        'last_name': {
            'codes': False,
            'dtype': str,
            'range': False,
            'length': 30,
            'regex': False,
            'required': True
        },
        'salary': {
            'codes': False,
            'dtype': float,
            'range': False,
            'length': 12,
            'regex': False,
            'required': False
        }
    }

    # Test schema builder
    test_schema = Schema(rules=rules)
    test_schema.create_rule(col='team', dtype=str, length=3, required=True)
    test_schema.update_rule(col='first_name', dtype=str, length=50, required=True)
    test_schema.delete_rule(col='first_name')

    report = Report(df=test_file, schema=test_schema())
    print '-----'
    print report()
    print '-----'
