# Variables
APP = app.py
ENV = venv
PORT = 8501

# Default target
.PHONY: all
all: install run

# Create virtual environment
.PHONY: venv
venv:
	python3 -m venv $(ENV)

# Install dependencies
.PHONY: install
install: venv
	$(ENV)/bin/pip install --upgrade pip
	$(ENV)/bin/pip install -r requirements.txt

# Run the Streamlit app
.PHONY: streamlit
streamlit:
	$(ENV)/bin/streamlit run $(APP) --server.port=$(PORT)

# Run the application
.PHONY: run
run:
	$(ENV)/bin/streamlit run $(APP) --server.port=$(PORT)

# Lint code
.PHONY: lint
lint:
	$(ENV)/bin/pip install pylint
	$(ENV)/bin/pylint $(APP)

# Clean the environment
.PHONY: clean
clean:
	rm -rf $(ENV) __pycache__ .streamlit

# Help target
.PHONY: help
help:
	@echo "Usage:"
	@echo "  make venv        Create a virtual environment"
	@echo "  make install     Install dependencies"
	@echo "  make run         Run the Streamlit app"
	@echo "  make lint        Lint the Python code"
	@echo "  make clean       Remove virtual environment and temporary files"
