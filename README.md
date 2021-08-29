# Trump bullet game
> A simple action game written in python.

[![Build Status](https://api.travis-ci.org/vyahello/trump-bullet-game.svg?branch=master)](https://travis-ci.org/vyahello/trump-bullet-game)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/trump-bullet-game/badge.svg?branch=master)](https://coveralls.io/github/vyahello/trump-bullet-game?branch=master)
[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE.md)
[![Hits-of-Code](https://hitsofcode.com/github/vyahello/trump-bullet-game)](https://hitsofcode.com/view/github/vyahello/trump-bullet-game)

**Tools**
> - python3.6+ 
> - pygame
> - pytest
> - travis CI
> - coveralls

## Usage
Run script from the root directory of the project:
```bash
git clone git@github.com:vyahello/trump-bullet-game.git
cd trump-bullet-game
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python game.py
```

### Demo
![Screenshot](images/game.png)

### Run code analysis
From the root directory of your shell run next command:
```bash
./code-analysis.sh
```

### Test report
If you need to run only unittests please execute following command:
```bash
pytest
```
Or run dedicated shell script:
```bash
./run-unittests.sh
```

Both approaches use [pytest.ini](pytest.ini) config file to setup execution.

After please open `test-report.html` to obtain test results.


## Development notes
### Release History

* 0.2.0
    * Add tests coverage
* 0.1.0
    * Distribute first app release

### Meta
Author – Volodymyr Yahello vyahello@gmail.com

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development dependencies

