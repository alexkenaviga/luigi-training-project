import luigi

# PYTHONPATH='.' luigi --module examples ParameterTask --local-scheduler
#   raise parameter.MissingParameterException


# PYTHONPATH='.' luigi --module examples ParameterTask --local-scheduler  --date 2024-12-03


# Upstream --- required by ---> Downstream

import os


class UpstreamTask(luigi.Task):

    """Simple task that displays the relation between a dependency and a dependent task

    UpstreamTask ---> required by ---> DownstreamTask

    Run with: `PYTHONPATH='.' luigi --module examples DownstreamTask --local-scheduler  --date 2024-12-03`
    """

    date = luigi.DateParameter()

    def run(self):
        # open the output in write mode and use it to produce some useful content
        with self.output().open('w') as fd:
            fd.write("Upstream Task %s" % self.date)

    def output(self):
        # define the output. i.e. LocalTarget, MysqlTableMarker
        return luigi.LocalTarget('./markers/upstream-out-%s.txt' % self.date)


class DownstreamTask(luigi.Task):
    date = luigi.DateParameter()

    def requires(self):
        return UpstreamTask(self.date)

    def run(self):
        # open the output in write mode and use it to produce some useful content
        with self.output().open('w') as fd:
            with self.input().open('r') as fi:
                for line in fi.readlines():
                    fd.write(line.upper())

    def output(self):
        # define the output. i.e. LocalTarget, MysqlTableMarker
        return luigi.LocalTarget('./markers/downstream-out-%s.txt' % self.date)



