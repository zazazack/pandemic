from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.getOrCreate()


def run():
    df = spark.read.csv(
        "/tmp/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/*.csv",
        header=True,
        # inferSchema=True
    )
    df = df.withColumn('input_file_path', input_file_name())
    df.write.csv(f"{__name__}.csv", header=True, mode="overwrite")


if __name__ == "__main__":

    run()
