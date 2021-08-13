import pymssql
import apache_beam as beam

class MSSQLConnect(beam.DoFn):
    
    def __init__(self, driver):
        super().__init__()
        self._driver = driver
        
    def setup(self):
        self.conn = pymssql.connect(
            host=self._driver['host'],
            user=self._driver['user'],
            password=self._driver['password'],
            database=self._driver['database']
        )
        self.cursor = self.conn.cursor(as_dict=True)
        
    def process(self, element):
        self.cursor.execute(element['query'])
        for row in self.cursor:
            yield row
        
    def teardown(self):
        self.conn.close()
