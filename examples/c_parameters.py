import luigi


class ParamsTask(luigi.Task):
    """Simple task that writes a passed parameter (a date in this case) to an output file

    Defined parameters can be passed using the 'kebab case' version of the variable name:
    i.e.: `string_to_write` becomes `--string-to-write`

    Run with: `PYTHONPATH='.' luigi --module examples ParamsTask --local-scheduler
            --string-to-write "my complex content" --output-filename "complex-content"`
    """

    string_to_write = luigi.Parameter()
    output_filename = luigi.Parameter(default='parameter-output')

    def run(self):
        # create file marker opening the output() in write mode
        with self.output().open('w') as fd:
            fd.write('%s' % self.string_to_write)

    # defines the target to verify if the task was already executed successfully
    def output(self):
        return luigi.LocalTarget('./markers/%s.txt' % self.output_filename)
