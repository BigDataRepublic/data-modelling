include ./env.local

.PHONY: install run clean drop-db

install:
	python3 -m venv ${PATH_TO_VIRTUAL_ENV}
	. ${PATH_TO_VIRTUAL_ENV}/bin/activate && pip install -r requirements.txt

run:
	set -a && . ./env.local && . ${PATH_TO_VIRTUAL_ENV}/bin/activate && python ./run.py

clean:
	rm -rf ./logs
	rm -rf ./__pycache__
	rm -rf ./target
	rm -rf ./dbt_packages
	rm -rf ./.user.yml
	rm ./pipeline.log || true

drop-db:
	rm /tmp/datamodelling.db || true
