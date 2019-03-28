# Trump bullet game
A simple action game written in python.

# Run a program
Run script from the root directory of the project:
```bash
python game.py
```

## Demo
![Screenshot](game.png)

## Run unittests
From the root directory of your shell run next command
```bash
➜ ./run-unittests.sh
```
### Unittests report
```bash
======================================================================================= test session starts ========================================================================================
platform darwin -- Python 3.6.5, pytest-4.3.1, py-1.8.0, pluggy-0.9.0 -- /Users/vyah/.pyenv/versions/3.6.5/envs/trump-bullet/bin/python
cachedir: .pytest_cache
rootdir: /Users/vyah/files/myprojects/trump-bullet, inifile: pytest.ini
collected 25 items

tests/model/test_navigation.py::test_count_navigation_options PASSED                                                                                                                         [  4%]
tests/model/test_navigation.py::test_navigation_option PASSED                                                                                                                                [  8%]
tests/model/test_navigation.py::test_contains_navigation[Navigation.up] PASSED                                                                                                               [ 12%]
tests/model/test_navigation.py::test_contains_navigation[Navigation.down] PASSED                                                                                                             [ 16%]
tests/model/test_navigation.py::test_contains_navigation[Navigation.left] PASSED                                                                                                             [ 20%]
tests/model/test_navigation.py::test_contains_navigation[Navigation.right] PASSED                                                                                                            [ 24%]
tests/model/test_navigation.py::test_contains_navigation[Navigation.quit] PASSED                                                                                                             [ 28%]
tests/model/test_properties.py::test_property_coordinates PASSED                                                                                                                             [ 32%]
tests/model/test_properties.py::test_color_as_rgba PASSED                                                                                                                                    [ 36%]
tests/model/test_properties.py::test_resolution_as_sequence PASSED                                                                                                                           [ 40%]
tests/model/test_properties.py::test_resolution_top_height PASSED                                                                                                                            [ 44%]
tests/model/test_properties.py::test_resolution_top_width PASSED                                                                                                                             [ 48%]
tests/model/test_properties.py::test_resolution_bottom_height PASSED                                                                                                                         [ 52%]
tests/model/test_properties.py::test_resolution_bottom_width PASSED                                                                                                                          [ 56%]
tests/model/test_properties.py::test_border_is_top_left PASSED                                                                                                                               [ 60%]
tests/model/test_properties.py::test_border_is_top_right PASSED                                                                                                                              [ 64%]
tests/model/test_properties.py::test_border_is_top_upper PASSED                                                                                                                              [ 68%]
tests/model/test_properties.py::test_border_is_top_lower PASSED                                                                                                                              [ 72%]
tests/model/test_properties.py::test_border_is_not_top_left PASSED                                                                                                                           [ 76%]
tests/model/test_properties.py::test_border_is_not_top_right PASSED                                                                                                                          [ 80%]
tests/model/test_properties.py::test_border_is_not_top_upper PASSED                                                                                                                          [ 84%]
tests/model/test_properties.py::test_border_is_not_top_lower PASSED                                                                                                                          [ 88%]
tests/model/test_shapes.py::test_get_rectangle_location PASSED                                                                                                                               [ 92%]
tests/model/test_shapes.py::test_set_rectangle_location PASSED                                                                                                                               [ 96%]
tests/model/test_visual.py::test_display_resolution PASSED                                                                                                                                   [100%]

==================================================================================== 25 passed in 0.50 seconds =====================================================================================
```

# Contributing

- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.6` is required to run the code