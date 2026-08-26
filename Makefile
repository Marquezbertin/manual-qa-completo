.PHONY: scripts test-api test-ui check-mermaid all

scripts:
	python 03/scripts/estimate.py
	python 04/scripts/triage.py
	python 07/scripts/percentile.py
	python 08/scripts/quality_gate.py
	python 09/scripts/kpi.py

test-api:
	cd 06/scripts && pytest -q

test-ui:
	cd 05/scripts && pytest -q

check-mermaid:
	python .github/scripts/check_mermaid.py

all: scripts check-mermaid test-api
