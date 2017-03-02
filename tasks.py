from subprocess import call
from invoke import task


@task
def serve(ctx):
    run('python serve.py')


@task
def dev(ctx):
    run('ls * | entr -r python server.py')


def run(cmd):
    call(cmd, shell=isinstance(cmd, str))
