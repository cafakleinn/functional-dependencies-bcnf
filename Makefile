N = 1

check:
	python -c 'from lambdacheck.cli import Check; Check()'

get:
	cp -R -u -T ~/public/assignment_$(N) ~/work/assignment_$(N)
