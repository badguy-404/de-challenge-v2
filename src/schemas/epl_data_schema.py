from pyspark.sql.types import StructType, StructField, StringType, IntegerType

class EPLProperties():
    schema = StructType([
      StructField("HomeTeam",StringType(),False),
      StructField("AwayTeam",StringType(),False),
      StructField("HS",IntegerType(),False),
      StructField("AS",IntegerType(),False),
      StructField("FTHG",IntegerType(),False),
      StructField("FTAG",IntegerType(),False),
      StructField("FTR",StringType(),False)
  ])
