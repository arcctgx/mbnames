.PHONY: release test sdist wheel clean

release: sdist wheel

test:
	python3 -m unittest discover -v -s tests/ -p "*_test.py"

sdist:
	python3 -m build --sdist

wheel:
	python3 -m build --wheel

clean:
	$(RM) -r build dist src/mbnames.egg-info src/mbnames/__pycache__ tests/__pycache__
