PROJECT_NAME=cloudquant
CDK_APP=infra.app
PYTHON=python

.PHONY: init synth deploy destroy test lint docker-shell

init:
	$(PYTHON) -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

synth:
	cdk synth -a "$(PYTHON) -m $(CDK_APP)"

deploy:
	cdk deploy -a "$(PYTHON) -m $(CDK_APP)"

destroy:
	cdk destroy -a "$(PYTHON) -m $(CDK_APP)"

test:
	pytest tests/ acceptance/

lint:
	flake8 app/ infra/ tests/

docker-shell:
	docker exec -it cloudquant-dev bash
