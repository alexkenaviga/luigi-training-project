import luigi


class HelloTask(luigi.Task):
    """Simple task that prints a "Hello" string to console

    Run with: `PYTHONPATH='.' luigi --module examples HelloTask --local-scheduler`
    """

    def run(self):
        print("Hello")
