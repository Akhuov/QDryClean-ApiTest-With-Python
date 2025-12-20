# QDryClean-QA-Automation-Framework
A clean and structured Python-based QA automation framework for the QDryCleaning service (Pytest, Playwright, Requests, Allure)
## Installing

Pull the report and create virtual env
```shell
> python3 -m venv venv
> source venv/bin/activate
```

Install required packages
```shell
> pip install playwright pytest pytest-playwright
```

Install Browsers:
```shell
playwright install
```
If you are linux user, install dependencies:
```shell
playwright install-deps
```
Install python-dateutil to work with date formats
```shell
pip install python-dateutil
```

# Running
```shell
pytest
```

# To run multiple tests in parallel, install the pytest-xdist plugin:
```shell
pip install pytest-xdist
```
# Then, use the -n option followed by the number of parallel workers (e.g., 4):
```shell
pytest -n 4
```
# If you want run one test more times download pytest-repeat 
```shell
pip install pytest-repeat
```
and run with --count n
```shell
pytest --count=5
```
# use parallel workers with view details on terminal
```shell
pytest -n 2 -v --tb=short 
```
This will distribute your test suite across 4 parallel processes, reducing execution time.

# install ruff 
```shell
pip install ruff
```
Ruff is a fast Python linter that keeps code clean and consistent

# To run ruff
```shell
ruff check . # to check
ruff check . --fix # to check and fix
```

# To run with report generation
```shell
 pytest --template=html1/index.html  --report=reports/file_name.html
```
Check documentation for pytest options [here](https://playwright.dev/python/docs/test-runners#cli-arguments)
