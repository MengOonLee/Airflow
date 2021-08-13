import pymssql
import apache_beam as beam
from .connect import MSSQLConnect

class MSSQLRead(beam.PTransform):
    
    def __init__(self, driver, query):
        super().__init__()
        self._driver = driver
        self._query = query
        conn = pymssql.connect(
            host=self._driver['host'],
            user=self._driver['user'],
            password=self._driver['password'],
            database=self._driver['database']
        )
        cursor = conn.cursor(as_dict=True)
        cursor.execute(
            "SELECT COUNT(1) AS count FROM ({}) AS sub"
            .format(self._query)
        )
        self.count = cursor.fetchone()['count']
        conn.close()
    
    def expand(self, pcoll):
        return (pcoll 
            | 'query, #record' >> beam.Create([{
                'query': self._query,
                'count': self.count
            }])
            | 'MSSQL connection' >> beam.ParDo(
                MSSQLConnect(self._driver)
            )
        )
