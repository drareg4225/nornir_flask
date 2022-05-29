# from nornir import InitNornir
# from nornir_utils.plugins.functions import print_result

# nr = InitNornir(config_file="config.yaml")
# # filtering objects to simplify output
# # nr = nr.filter(site="B", role="host")

# def hello_world(task: Task ) -> 
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Task, Result

def hello_world(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name} says hello world!"
    )

nr = InitNornir(config_file="config.yml")
result = nr.run(task=hello_world)
print_result(result)