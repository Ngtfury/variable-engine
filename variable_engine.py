class VariableEngine:

    def __init__(self, prefix=None, suffix=None):
        self.variables = {}
        self.prefix = prefix if prefix else ''
        self.suffix = suffix if suffix else self.prefix

    def add_variable(self, variable: str, value: str):
        if not isinstance(variable, str):
            raise TypeError(f'Expected str instance, got {type(variable).__name__} in variable.')
        if not isinstance(value, str):
            raise TypeError(f'Expected str instance, got {type(value).__name__} in value.')

        self.variables[variable] = value
    add_var = add_variable

    def clear_variables(self):
        del self.variables
        self.variables = {}
    clear_vars = clear_variables

    def remove_variable(self, variable):
        if not isinstance(variable, str):
            raise TypeError(f'Expected str instance, got {type(variable).__name__} in variable.')

        if not variable in self.variables:
            raise NameError(f'There is no such variable: "{variable}".')

        del self.variables[variable]
    remove_var = remove_variable

    def process(self, string: str):
        if not isinstance(string, str):
            raise TypeError(f'Expected str instance, got {type(string).__name__} in string.')

        result = None
        for variable, value in self.variables.items():
            if not result:
                result = string

            _variable = f'{self.prefix}{variable}{self.suffix}'
            result = result.replace(_variable, value)
        
        return result