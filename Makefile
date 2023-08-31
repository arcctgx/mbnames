.PHONY: all test bdist sdist wheel clean

all: bdist sdist wheel

test:
	python3 -m unittest discover -v -s tests/ -p "*_test.py"

bdist:
	python3 setup.py bdist

sdist:
	python3 setup.py sdist

wheel:
	python3 setup.py bdist_wheel

clean:
	$(RM) -r build dist mbnames.egg-info mbnames/__pycache__ tests/__pycache__
