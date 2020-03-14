from app.pyspark_module.spark_session import PysparkSesssion

def read_csv_v1():
    df = spark.read.option('header', True).csv('storage/weather_v1.csv')
    df.show()
    df.printSchema()


if __name__ == "__main__":
    pyspark_session_object = PysparkSesssion()
    spark = pyspark_session_object.spark
    sc = pyspark_session_object.sc
    read_csv_v1()




