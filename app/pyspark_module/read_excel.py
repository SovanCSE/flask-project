from app.pyspark_module.spark_session import PysparkSesssion

def read_excel_v1():
    df = spark.read.format("com.crealytics.spark.excel").option("useHeader", False).load(
        'storage/Operations Forecast 123115.xlsx')
    df.show(10)
    df.printSchema()


if __name__ == "__main__":
    pyspark_session_object = PysparkSesssion()
    spark = pyspark_session_object.spark
    sc = pyspark_session_object.sc
    read_excel_v1()




