class MiniInterpreter
    def __init__(self)
        self.variables = {}

    def evaluate_expression(self, expr str)
        # Replace variables with their values
        for var in self.variables
            expr = expr.replace(var, str(self.variables[var]))
        try
            return eval(expr)
        except Exception as e
            return fError evaluating expression {e}

    def handle_let(self, statement str)
        # Remove 'let' and split into var and expression
        assignment = statement[4].strip()
        var, value_expr = assignment.split(=, 1)
        var = var.strip()
        value_expr = value_expr.strip()
        value = self.evaluate_expression(value_expr)
        self.variables[var] = value
        print(value)

    def handle_if(self, statement str)
        # Parse the if statement
        condition, true_expr, false_expr = self.parse_if_statement(statement)
        if self.evaluate_expression(condition)
            result = self.evaluate_expression(true_expr)
        else
            result = self.evaluate_expression(false_expr)
        print(result)

    def parse_if_statement(self, statement str)
        # Extract condition, true expression, and false expression
        parts = statement[3].strip().split(then)
        if len(parts) != 2
            raise SyntaxError(Invalid if syntax.)
        condition = parts[0].strip()
        true_false_parts = parts[1].strip().split(else)
        if len(true_false_parts) != 2
            raise SyntaxError(Invalid if syntax.)
        true_expr = true_false_parts[0].strip()
        false_expr = true_false_parts[1].strip()
        return condition, true_expr, false_expr

    def run(self, lines list)
        for line in lines
            line = line.strip()
            if line.startswith(let)
                self.handle_let(line)
            elif line.startswith(if)
                self.handle_if(line)
            elif line
                print(self.evaluate_expression(line))


if __name__ == __main__
    # Sample Input
    commands = [
        let x = 5,
        let y = x + 3,
        if x  3 then x else y
    ]

    interpreter = MiniInterpreter()
    interpreter.run(commands)
