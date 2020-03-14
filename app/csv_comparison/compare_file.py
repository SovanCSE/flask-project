# from pyspark.sql import SparkSession
import pandas as pd

if __name__ == "__main__":
    # spark = SparkSession.builder.appName('compare_csv').enableHiveSupport().getOrCreate()
    read_path1 = 'csv_storage/teradata/inp_master_origin_fe_att_2019_12_01.csv'
    read_path2 = 'csv_storage/teradatamirror/inp_master_origin_fe_att_2019_12_01.csv'
    df = pd.read_csv(read_path1)
    # df = df.agg({'as_of_dt' : ['min','max', 'count']})
    df = df.agg({'as_of_dt' : ['min','max', 'count']})
    df = df.unstack()
    print(df.head(10))
    # df1 = spark.read.format('csv').option('header',True).load(read_path1)
    # df2 = spark.read.format('csv').option('header',True).load(read_path2)
    # columns1 = df1.columns
    # columns2 = df2.columns
    # df2=df2.select(df1.columns)
    # columns1.sort()
    # columns2.sort()
    # # print(columns1)
    # # print(columns2)
    # if columns1.sort() == columns2.sort():
    #     print("same columns")
    # else:
    #     print('diff columns')
    # diff_df1 = df1.subtract(df2)
    # diff_df2 = df2.subtract(df1)
    # #service_dt ,origin ,as_of_dt ==> 2019-12-01, international paid,2019-10-15
    # diff_df1.filter( (diff_df1['service_dt'] == '2019-12-01') & (diff_df1[
    #                                                                                       'origin'] ==
    #                                                              'international paid') & (diff_df1['as_of_dt'] == '2019-10-15')).show(1)
    # diff_df2.filter((diff_df2['service_dt'] == '2019-12-01') & (diff_df2[
    #                                                                                      'origin'] ==
    #                                                              'international paid') & (
    #         diff_df2['as_of_dt'] == '2019-10-15')).show(1)
