import os
import luigi
from luigi.util import requires
from .d_dependents import UpstreamTask


@requires(UpstreamTask)
class DecoratedDownstreamTask(luigi.Task):
    """Simple task that displays the relation between a dependency and a dependent task, using `@requires`

    Run with: `PYTHONPATH='.' luigi --module examples DecoratedDownstreamTask --local-scheduler  --date 2024-12-03`

    NOTE: there is no need to declare parameters, are inherited automatically
    """

    def run(self):
        # open the output in write mode and use it to produce some useful content
        with self.output().open('w') as fd:
            with self.input().open('r') as fi:
                for line in fi.readlines():
                    fd.write(line.upper())

    def output(self):
        # define the output. i.e. LocalTarget, MysqlTableMarker
        return luigi.LocalTarget('./markers/decorated-downstream-out-%s.txt' % self.date)
