'''
Reader.py : supports csv | Parquete
'''
from utils.applogger import get_logger
from schema.schemas import get_order_schema

def read_csv(spark_session,input_file,schema_name=None, app_logger=None):
    if app_logger== None:
        app_logger=get_logger()
    if schema_name == None:
        schema = None
    if schema_name == "order":
        schema = get_order_schema()
    app_logger.debug("Read CSV insvoked")
    app_logger.debug(f"Input file : {input_file}")
    df= spark_session.read.csv(input_file,schema,header=True)
    return df

