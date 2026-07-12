build:
	poetry build

test:
	poetry run pytest tests/

run: build
	poetry run audit-agent

clean:
	rm -rf dist/ build/ audit_agent.egg-info/

lint:
	poetry run flake8 audit_agent tests/

fmt:
	poetry run black audit_agent tests/

shell:
	poetry shell