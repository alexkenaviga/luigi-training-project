setup: requirements.txt
	test -d .venv || python3 -m venv .venv
	.venv/bin/python -m pip install -U pip
	.venv/bin/python -m pip install -r requirements.txt

clean:
	rm -r .venv