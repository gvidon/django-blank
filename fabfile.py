from fabric.api import cd, env, execute, hosts, local, run, sudo

env.update({
	'app_path': '/remote/path/to/django/application', # Directory must include manage.py file
	'hosts'   : ['remote.host'],
	'repo'    : '', # ssh URL or file system path to repo directory
})

# Execute local process and grab errors
def popen(str):
	import re
	from subprocess import Popen, PIPE

	output, err = Popen(str, shell=True, stdout=PIPE, stderr=PIPE).communicate()

	# Git hack
	if err and not re.search('FETCH_HEAD|Everything up\-to\-date|master \-> master', err):
		print 'Error happened'
		print err
		exit()

# Run shell code in selected directiry
def run_in_path(path, command):
	with(cd(path)):
		run(command)

# Update application files
def update():
	run_in_path(env.app_path, 'git pull origin master')

def restart_service():
	sudo('nohup service mmm restart')

def collect_static():
	run_in_path(env.app_path, 'python manage.py collectstatic --noinput')

@hosts('')
def push():
	popen('git pull ' + env['repo'])
	popen('git push ' + env['repo'])

# Pull-push, update application dir with repo updates, collect static in
# application dir and restart application service
def deploy():
	push()
	execute(update)
	execute(collect_static)
	execute(restart_service)