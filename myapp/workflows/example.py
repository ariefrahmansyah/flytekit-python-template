from flytekit import task, workflow


@task
def greet(name: str) -> str:
    return f"Hello, {first_name} {last_name}"


@workflow
def hello_world(name: str = "world") -> str:
    greeting = greet(name=name)
    return greeting
