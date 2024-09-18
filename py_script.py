import json

def load_config(file_path='config.json'):
    with open(file_path, 'r') as file:
        return json.load(file)

def route_decision(brand, customer_id, config):
    brands = config['brands']
    customer_profiles = config['customer_profiles']
    switch = customer_profiles['switch']
    customers = customer_profiles['customers']

    # First, check if the brand is enabled
    if brands.get(brand, 'N') == 'Y':
        # If brand is enabled, check the switch
        if switch == 'A':
            # If switch is 'A', go straight to Route 2
            return "Route 2 selected"
        elif switch == 'Y':
            # If switch is 'Y', check if customer ID is in the list and enabled
            if customers.get(customer_id, 'N') == 'Y':
                return "Route 2 selected"
    
    # Default to Route 1 for all other cases
    return "Route 1 selected"

def main():
    config = load_config()
    
    while True:
        brand = input("Enter brand (RBS, NWB, UBN) or 'q' to quit: ").upper()
        if brand == 'Q':
            break
        if brand not in ['RBS', 'NWB', 'UBN']:
            print("Invalid brand. Please enter RBS, NWB, or UBN.")
            continue
        
        customer_id = input("Enter customer ID: ")
        
        result = route_decision(brand, customer_id, config)
        print(result)

if __name__ == "__main__":
    main()