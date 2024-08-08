def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    balance = 0
    
    for char in parens:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        
        # If balance goes negative, we have more closing than opening
        if balance < 0:
            return False
    
    # If balance is 0, parentheses are balanced
    return balance == 0