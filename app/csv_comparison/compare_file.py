from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName('compare_csv').enableHiveSupport().getOrCreate()
    read_path1 = 'csv_storage/teradata/inp_master_origin_fe_att_2019_12_01.csv'
    read_path2 = 'csv_storage/teradatamirror/inp_master_origin_fe_att_2019_12_01.csv'

    df1 = spark.read.format('csv').option('header',True).load(read_path1)
    df2 = spark.read.format('csv').option('header',True).load(read_path2)

    df2=df2.select(df1.columns)

    columns1 = df1.columns
    columns2 = df2.columns

    if columns1.sort() == columns2.sort():
        print("same columns")
    else:
        print('diff columns')

    diff_df1 = df1.subtract(df2)
    diff_df1.show()

    diff_df2 = df2.subtract(df1)
    diff_df2.show()