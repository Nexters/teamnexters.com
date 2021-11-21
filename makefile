GREEN=\n\033[1;32;40m
RED=\n\033[1;31;40m
NC=\033[0m # No Color
# 마지막 tag로부터 현재까지의 changelog 및 버전 확인 용
current_changelog:
	@/bin/sh -c "echo \"${GREEN}[release version] $(shell npx standard-version --dry-run | grep tagging | cut -d ' ' -f4)${NC}\""
	@/bin/sh -c "echo \"${GREEN}[description] ${NC}\""
	@npx standard-version --dry-run --silent | grep -v Done | grep -v "\-\-\-" | grep -v standard-version
.PHONY: current_changelog

ref:
	@/bin/sh -c "echo \"${GREEN}pipenv install${NC}\""
	@export PIPENV_VENV_IN_PROJECT=${PWD} && pipenv install --dev
	@pipenv graph
.PHONY: ref

requirements:
	@/bin/sh -c "echo \"${GREEN}[requirements.txt를 추출합니다]${NC}\""
	@pipenv lock -r > requirements.txt
.PHONY: requirements
