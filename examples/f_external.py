import luigi


class External(luigi.ExternalTask):
    """Simple task that verifies an external event: the creation of a file `./markers/wait-for-it.txt` by an external
    entity
    """

    def output(self):
        # define the output. i.e. LocalTarget, MysqlTableMarker
        return luigi.LocalTarget('./markers/wait-for-it.txt')


class DependsFromExternal(luigi.Task):
    """Simple task that has a dependency from External. It will run only if the marker file `./markers/wait-for-it.txt`
    is created manually

    Run with: `PYTHONPATH='.' luigi --module examples DependsFromExternal --local-scheduler`
    """

    def requires(self):
        return External()

    def run(self):
        # open the output in write mode and use it to produce some useful content
        with self.output().open('w') as fd:
            fd.write("done")

    def output(self):
        # define the output. i.e. LocalTarget, MysqlTableMarker
        return luigi.LocalTarget('./markers/after-waiting.txt')
