import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

empDf = glueContext.create_dynamic_frame.from_catalog(
    database="etl_project_glue_database",
    table_name="etl_project",
    transformation_ctx="etl_project_ctx"
)

empDf.printSchema()
sparkEmpDf = empDf.toDF()
sparkEmpDf.show()
print(sparkEmpDf.count())

sparkEmpDf = sparkEmpDf.withColumn("salary", col("salary") * 2)

glueContext.write_dynamic_frame.from_options(frame = sparkEmpDf,
                                             connection_type = "s3",
                                             connection_options = {"path": "s3://etl-project/"},
                                             format = "csv")


# job = Job(glueContext)
# job.init(args['JOB_NAME'], args)
# job.commit()
