## A simple package for handling string variables.
### Welcome!
This is a simple package for handling variables in string, You can add or remove variables with prefix and suffix!

This project is open source ⭐.

### Install
```
pip install -U git+https://github.com/Ngtfury/variable-engine
```

### Usage

## Without prefix and suffix
```py
import variable_engine
from variable_engine import VariableEngine

engine = VariableEngine() #Calls the __init__
engine.add_variable(variable = 'foo', value = 'bar') #Aliase "add_var"
engine.add_var(variable = 'baz', value = 'qux')

string = engine.process('foo bar baz quz')
print(string)

#To remove a variable
engine.remove_variable('baz')

#To clear all variables
engine.clear_variables()
```
# Output
```py
bar bar qux qux # foo replaced with bar and baz replaced with qux
```

## With prefix and suffix
```py
import variable_engine
from variable_engine import VariableEngine

engine = VariableEngine(prefix = '[', suffix = ']') # If suffix is None, suffix defaults to prefix.
engine.add_var(variable = 'foo',  value = 'bar')

string = engine.process('This is foo -> [foo]. wait what?')
print(string)
```
# Output
```
This is foo -> bar. wait what?
```