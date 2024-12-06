import luigi


class FileTask(luigi.Task):
    """Simple task that writes a marker file as an output.

    The existence of the content referenced by `output()` determines if the task will be run or considered already done

    Run with: `PYTHONPATH='.' luigi --module examples FileTask --local-scheduler`
    """

    def run(self):
        # create file marker opening the output() in write mode
        with self.output().open('w') as fd:
            fd.write("done") # can be empty, only the existence is needed

    # defines the target to verify if the task was already executed successfully
    def output(self):
        return luigi.LocalTarget('./markers/idempotent.txt')
