import luigi
import datetime
from luigi.contrib.mysqldb import MySqlTarget


class InsertDataIntoMySQL(luigi.Task):

    """
    Simple task that executes some code and creates a marker entry on the default `marker_table` on MySql
    """

    date = luigi.DateParameter()

    # Defaults are referred to MySql instance runnable via docker-compose using compose/mysql/docker-compose.yaml
    host = luigi.Parameter(default='localhost')
    database = luigi.Parameter(default='luigi-db')
    user = luigi.Parameter(default='root')
    password = luigi.Parameter(default='password')

    table = 'orders_stats'

    def requires(self):
        return []

    def output(self):
        return MySqlTarget(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            table=self.table,
            update_id=f'{self.table}_{self.date.isoformat()}'
        )

    def run(self):
        # Only necessary if marker table is not provided by infrastructure
        self.output().create_marker_table()

        # SELECT * FROM orders WHERE order_date BETWEEN '2024-12-16 14:00:00' AND '2024-12-16 15:00:00'
        query = f"""SELECT * 
        FROM orders
        WHERE order_date BETWEEN '{self.date.isoformat()}' 
            AND '{(self.date + datetime.timedelta(days=1)).isoformat()}'"""
        print(f'### query: {query}')

        with self.output().connect() as connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query)

            rows = cursor.fetchall()

            orders = len(rows)
            amount = 0
            items = 0
            for row in rows:
                amount += row['total']
                items += row['items']
            amount_avg = round(amount / orders, 2) if orders > 0 else 0
            items_avg = round(items / orders, 2) if orders > 0 else 0

            print(f'### date: {self.date.isoformat()} orders: {orders} total: {amount} items: {items}')

            query = f"""INSERT INTO {self.table} (order_date, total_avg, items_avg)
                VALUES('{self.date.isoformat()}', '{amount_avg}', '{items_avg}')"""
            print(f'### query: {query}')

            cursor.execute(query)
            connection.commit()

        # Creates marker entry
        self.output().touch()

