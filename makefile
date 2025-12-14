# ====== SETTINGS ======
PYTHON := python
SRC := app

# ====== COMMANDS ======
.PHONY: help format check

help:
	@echo ""
	@echo "make format  - format code (autoflake + isort + black)"
	@echo "make check   - check formatting without changes"
	@echo ""

format:
	@echo "▶ Running autoflake..."
	autoflake \
		--remove-all-unused-imports \
		--remove-unused-variables \
		--in-place \
		--recursive \
		$(SRC)

	@echo "▶ Running isort..."
	isort $(SRC)

	@echo "▶ Running black..."
	black $(SRC)

check:
	@echo "▶ Checking isort..."
	isort --check-only $(SRC)

	@echo "▶ Checking black..."
	black --check $(SRC)
