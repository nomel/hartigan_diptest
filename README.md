Based on https://github.com/russelljjarvis/modality, with everything removed but the hartigan diptest.

# modality
Statistical tests for evaluating unimodality, in particular:
- Hartigan's dip test (equivalent to excess mass test).

### References
Hartigan and Hartigan (1985): The dip test of unimodality.
The Annals of Statistics. 13(1).

## Usage
```
import hartigan_diptest
data = np.random.randn(1000)
p_value = hartigan_diptest.dip(data)
```

## Dependencies
The package has the following dependencies:
- Python 2.7 or Python 3.6, as well as packages listed in setup.py.

## Installation
Clone https://github.com/nomel/hartigan_diptest

In the terminal, go to the extracted directory and run
```
pip install .
```
If installation for only one user is wanted, you can add the option
`--user`.
