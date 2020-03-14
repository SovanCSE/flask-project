from app.pyspark_module.spark_session import PysparkSesssion
from pyspark.sql.functions import isnan, when, count

if __name__ == "__main__":
    pyspark_session_object = PysparkSesssion()
    spark = pyspark_session_object.spark
    sc = spark.sparkContext

    df = spark.createDataFrame(data=[('lll',1,20,30,4),('lll', None, 20,30,4)],
                               schema=['COLUMN NAME', 'MAX VALUE(D3T)', 'MIN VALUE(D3T)',
                                       'SUM VALUE(D3T)', 'NULL COUNT(D3T)'])
    null_count = df.select(count(when(isnan('MAX VALUE(D3T)'), 'MAX VALUE(D3T)'))).head()[0]
    print(null_count)
    df.show()
    # # print(df.show())
    # new_df = spark.createDataFrame(data=[[15.111111111,20.00000],[30.9999,40.777777]],
    #                                schema=['AA','BB'])
    # joinall = df.unionAll(new_df)
    # joinall.show()

    # total_count1 = df.select(count(when(isnan('B'),'B'))).head()[0]
    # total_count2 = df.select(count(when(isnan('A'),'A'))).head()[0]
    # print(total_count1, total_count2)
    # null_count = df.filter(col('A') == np.NAN).agg({'A':'count'}).head()[0]
    # max_count = df.filter(col('A') != np.NAN).agg({'A':'max'}).head()[0]
    # min_count = df.filter(col('A') != np.NAN).agg({'A':'min'}).head()[0]
    # sum_count = df.filter(col('A') != np.NAN).agg({'A':'sum'}).head()[0]
    # print(max_count,min_count, sum_count, null_count)'
    # ["DecimalType",
    #  "DoubleType",
    #  "FloatType",
    #  "IntegerType",
    #  "LongType",
    #  "ShortType",
    #  "ByteType",
    #  "BinaryType"]
    # numeric_columns = [f.name for f in df.schema.fields if str(f.dataType) in ["DecimalType",
    #  "DoubleType",
    #  "FloatType",
    #  "IntegerType",
    #  "LongType",
    #  "ShortType",
    #  "ByteType",
    #  "BinaryType"]]
    # print(numeric_columns)
    # df.show()
    # dict1 = {"A_12": [1.1, 5, 3, None], "B_13": [4, None, 6.2, None], 'C_14': ['lll', 'ooo', '99',
    #                                                                      'yooo']}
    # pandas_df = pd.DataFrame(dict1)
    # empty_dataframe = spark.createDataFrame(pandas_df)
    # # empty_dataframe.show()
    # new_dataframe = empty_dataframe.unionAll(df)
    # # new_dataframe.columns = new_dataframe.columns.str.lower()
    # # new_dataframe.show()
    # for column in new_dataframe.columns:
    #     new_dataframe = new_dataframe.withColumnRenamed(column, column.lower())
    #     new_dataframe = new_dataframe.withColumnRenamed(column, column.replace("_"," "))
    # new_dataframe.coalesce(1).write.option('delimiter', ',').option("header","true").mode(
    #     'overwrite').csv()
