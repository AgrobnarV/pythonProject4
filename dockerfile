from python
workdir /tests_project/
copy requirments.txt .
run pip install -r requirments.txt
env ENV=dev
cmd python -m pytest -s --alluredir=test_results/ /./OpenUserApi2/tests/

