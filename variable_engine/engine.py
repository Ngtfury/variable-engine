
class VariableEngine:
    """A simple package for handling variables in string."""

    def __init__(self, prefix: str = None, suffix: str = None):
        self.variables = {}
        self.prefix = str(prefix) if prefix else '' #If prefix is none prefix defaults to ''
        self.suffix = str(suffix) if suffix else self.prefix #If suffix is none suffix defaults to prefix

    def add_variable(self, variable: str, value: str):
        """Adds a new variable with a value to the engine."""

        if str(variable) in self.variables:
            #to avoid duplicate entities
            raise NameError(f'Variable "{variable}" already exists.')

        self.variables[str(variable)] = str(value)
    #aliase, add_var corresponds to add_variable
    add_var = add_variable 


    def clear_variables(self):
        """Removes all variables from the engine."""

        del self.variables
        self.variables = {}
    #aliase, clear_vars corresponds to clear_variables
    clear_vars = clear_variables


    def remove_variable(self, variable: str):
        """Removes a variable from the engine."""
        _variable = str(variable)

        if not _variable in self.variables:
            raise TypeError(f'There is no such variable: "{variable}".')

        del self.variables[_variable]
    #aliase, remove_var corresponds to remove_variable
    remove_var = remove_variable


    def process(self, string: str):
        """Processes a string, replaces variables with its values."""

        result = None
        for variable, value in self.variables.items():
            if not result:
                result = str(string)

            _variable = f'{self.prefix}{variable}{self.suffix}'
            result = result.replace(_variable, value)
        
        return result
