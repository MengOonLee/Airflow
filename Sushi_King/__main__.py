import json
import logging
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from src.mssql.read import MSSQLRead

class CustomOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_argument('--driver_file', type=str)
        parser.add_argument('--customer_sql_file', type=str)

args = PipelineOptions().view_as(CustomOptions)
with beam.Pipeline(options=PipelineOptions()) as p:
    
    logging.getLogger().setLevel(logging.INFO)
    
    _ = (p 
        | 'customer db' >> MSSQLRead(
            json.load(open(args.driver_file, 'r')),
            open(args.customer_sql_file, 'r').read()
        )
        | beam.Map(print)
    )
