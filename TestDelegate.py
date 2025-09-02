class Task:
    def __init__(self, value: str = "a_value"):
        self.value = value
        print(f"Task({self.value}) built")

    def run(self):
        print(f"Running Task({self.value})")


class WrappedTask:

    def __init__(self, task: Task):
        self.task = task

    def run(self):
        print("Running in wrapper...")
        self.task.run()

    def value(self):
        return self.task.value


class Caller:
    group = "group"

    def requires(self):
        yield Task(f"{self.group}_1")
        yield Task(f"{self.group}_2")

    def run(self):
        for r in self.requires():
            r.run()


def caller_decorator(cls):
    print("Decorating...")
    original_requires = cls.requires

    def wrapped_requires(_self):
        for v in original_requires(_self):
            yield WrappedTask(v)

    cls.requires = wrapped_requires
    return cls


@caller_decorator
class CallerDecorated(Caller):
    pass


if __name__ == '__main__':
    print("# INIT")
    d = CallerDecorated()
    print("# REQUIRES")
    rl = d.requires()
    print("# ITERATE\n")
    for r in rl:
        print(f"# RUN {r.value()}")
        r.run()

