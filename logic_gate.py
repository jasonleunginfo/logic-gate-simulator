def simulate_gate(gate: str, input_a: bool, input_b: bool = None) -> bool:
    """
    Simulates basic logic gates: AND, OR, NOT, XOR.
    """
    gate = gate.upper()
    
    if gate == "AND":
        return input_a and input_b
    elif gate == "OR":
        return input_a or input_b
    elif gate == "NOT":
        return not input_a
    elif gate == "XOR":
        return input_a != input_b
    else:
        raise ValueError(f"Gate '{gate}' not supported.")

if __name__ == "__main__":
    # Examples
    print("--- Logic Gate Simulator ---")
    print(f"AND (True, False): {simulate_gate('AND', True, False)}")
    print(f"OR (True, False):  {simulate_gate('OR', True, False)}")
    print(f"NOT (True):        {simulate_gate('NOT', True)}")
    print(f"XOR (True, True):  {simulate_gate('XOR', True, True)}")
