'''
Reader.py : supports csv | Parquete
'''
from utils.applogger import get_logger
from schema.schemas import get_order_schema
from utils.exceptions import IngestionError

def read_csv(spark_session,input_file,file_format,schema_name=None, app_logger=None):
    if app_logger== None:
        app_logger=get_logger()
    if schema_name == None:
        schema = None
    if schema_name == "order":
        schema = get_order_schema()
    app_logger.debug("Read CSV insvoked")
    app_logger.debug(f"Input file : {input_file}")
    if file_format == "csv":
        df= spark_session.read.csv(input_file,schema,header=True)
    elif file_format=="parquet" :
        df = spark_session.read.parquet(input_file)
    else:
        raise IngestionError(f"Unsupported file format: {file_format}")
    return df

