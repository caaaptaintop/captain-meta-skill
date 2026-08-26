PYTHON ?= python3

.PHONY: test

test:
	$(PYTHON) tests/verify_captain_downstream.py
