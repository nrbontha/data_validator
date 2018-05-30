#!/usr/bin/env python2

import validator
import pandas as pd 
from schema import Schema
from schema import RuleError
from validator import Report

if __name__ == "__main__":

    test_file = pd.read_csv('data/test_data.csv')

    test_schema = Schema()
    test_schema.create_rule(col='team', dtype=str, length=3, required=True)
    test_schema.create_rule(col='first_name', dtype=str, length=30, required=True)
    test_schema.create_rule(col='last_name', dtype=str, length=30, required=True)
    test_schema.create_rule(col='age', dtype=int, length=2, required=True)
    test_schema.create_rule(col='salary', dtype=float, length=12)
    test_schema.create_rule(col='exp', dtype=int, length=2, in_range=[0,20])

    validator = Report(df=test_file, schema=test_schema.rules)

    report = validator.get_report()

    print report
