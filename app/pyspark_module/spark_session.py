from pyspark.sql import SparkSession

class PysparkSesssion(object):
    def __init__(self, app_name = 'demo', log_level ='info'):
        self.app_name = app_name
        self.log_level = log_level
        self.spark = self.getSparkSession()
        self.sc = self.spark.sparkContext


    def getSparkSession(self):
        return SparkSession.builder.appName(self.app_name).enableHiveSupport().getOrCreate()



