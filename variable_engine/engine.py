from .exceptions import DuplicateVariable, VariableNotFound

class VariableEngine:

    def __init__(self, prefix: str = None, suffix: str = None):
        self.variables = {}
        self.prefix = str(prefix) if prefix else ''
        self.suffix = str(suffix) if suffix else self.prefix

    def add_variable(self, variable: str, value: str):
        if str(variable) in self.variables:
            raise DuplicateVariable(f'Variable "{variable}" already exists.')

        self.variables[str(variable)] = str(value)
    add_var = add_variable

    def clear_variables(self):

        del self.variables
        self.variables = {}
    clear_vars = clear_variables

    def remove_variable(self, variable: str):
        _variable = str(variable)

        if not _variable in self.variables:
            raise VariableNotFound(f'There is no such variable: "{variable}".')

        del self.variables[_variable]
    remove_var = remove_variable

    def process(self, string: str):

        result = None
        for variable, value in self.variables.items():
            if not result:
                result = str(string)

            _variable = f'{self.prefix}{variable}{self.suffix}'
            result = result.replace(_variable, value)
        
        return result