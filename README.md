# python ci 
## yeardream 2nd - mlops lecture 실습

how to run github action
- create .github/workflows / .github/workflows 생성
- create file - lint.yml in workflows directory / wrokflows 폴더 안에 lint.yml 파일 작성
    indentation 주의 

when lint failed
- use black to change the format of your codes
- or you can use codeclimate, check maintainability and test coverate

about github
- after PR of other branch
- you have to pull at local shell from main branch 

on VSC
- test: automatically test files (on initial setting, unitttest - *_test.py is selected)
- you can test files when you click test above the list of files

on code climate
- code in bewlo means unittest skip
```python
if __name__ == "__main__":  # pragma: no cover " 
``` 
    

## python-ci-example

[![Maintainability](https://api.codeclimate.com/v1/badges/86d84e5077181b241ef9/maintainability)](https://codeclimate.com/github/Rum-j/python_ci_example/maintainability)[![Test Coverage](https://api.codeclimate.com/v1/badges/86d84e5077181b241ef9/test_coverage)](https://codeclimate.com/github/Rum-j/python_ci_example/test_coverage)



## How to run?

```sh
$ python main.py
```

## How to run test code?

```sh
$ python -m unittest discover -p "*_test.py"
```
