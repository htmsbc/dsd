from prefect import flow, task
from prefect.deployments import Deployment
from prefect.filesystems import GitHub

github_block = GitHub.load("gitb")

@task()
def test():
    for i in range(1,50):
        # time.sleep(3)
        print("Iteration completed {}".format(i))


@flow(name="My Flow",
      description="My flow using SequentialTaskRunner",)
def api_flow():
    test()


# api_flow("https://catfact.ninja/fact")


deployment = Deployment.build_from_flow(
        flow=api_flow,
        name="msbc-test",
        work_pool_name="v",
    storage = github_block

    )
if __name__ == "__main__":
    deployment.apply()
