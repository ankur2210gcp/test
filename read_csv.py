#!/bin/python
# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession



def read_csv(path):
    df = spark.read.csv(path)


if __name__ == '__main__':
    spark = SparkSession.builder.appName('abc').getOrCreate()
    path = sys.argv[0]
    read_csv(path)
