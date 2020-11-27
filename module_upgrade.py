import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
call("python -m pip install --upgrade --user " + ' '.join(packages), shell=True)