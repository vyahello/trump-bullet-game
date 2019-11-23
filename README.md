# Trump bullet game
> A simple action game written in python.

[![Build Status](https://api.travis-ci.org/vyahello/trump-bullet-game.svg?branch=master)](https://travis-ci.org/vyahello/trump-bullet-game)

**Tools**
> - python3.6
> - pygame
> - pytest
> - travis CI
> - coveralls

## Usage
Run script from the root directory of the project:
```bash
python game.py
```

### Demo
![Screenshot](images/game.png)

### Run code analysis
From the root directory of your shell run next command:
```bash
➜ ./code-analysis.sh
```

### Test report

If you need to run only unittests please execute following command:
```bash
➜ pytest
```
Or run dedicated shell script:
```bash
➜ ./run-unittests.sh
```

Both approaches use [pytest.ini](pytest.ini) config file to setup execution.

After please open `test-report.html` to obtain test results.

## Meta
Author – Volodymyr Yahello vyahello@gmail.com

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

## Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development dependencies

