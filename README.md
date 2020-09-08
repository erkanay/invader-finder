# invader-finder

This repository simply search given invader in radar pattern. 

First of all it converts two patterns(invader & radar) into list objects.
Then try to match first row of invader in radar rows and if that found so 
it goes to look for next rows in same indexes and collects 
matched invader pattern.

Finally it allows us to return invader locations on radar pattern 
via `invader_locations` method in following structure.

```python
[(row, start_index, end_index), ...]
``` 

## Test

```python
python test.py

..
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK

```