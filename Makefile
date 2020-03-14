--shell=/usr/bin/env bash
.PHONY: all clean install

clean:
	rm -v -rf ./{build/,dist/,src/*.egg-info}
	find . -name "*.pyc" -type f -o -name "__pycache__" -type d | xargs rm -v -rf

all: clean
