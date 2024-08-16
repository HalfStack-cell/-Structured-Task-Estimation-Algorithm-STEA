def calculate_total_time(components, time_scaling_factors):
    """
    Calculate the total time required for the project based on the components and their complexities.
    
    Parameters:
    components (dict): A dictionary where keys are component names and values are complexity levels.
    time_scaling_factors (dict): A dictionary where keys are component names and values are time-scaling factors.

    Returns:
    float: The total time required for the project.
    """
    total_time = sum(time_scaling_factors[comp] * components[comp] for comp in components)
    return total_time

def main():
    print("Welcome to the Project Time Estimator based on STEA!")
    
    # Number of components
    n = int(input("Enter the number of components in your project: "))
    
    components = {}
    time_scaling_factors = {}
    
    # Input components and their complexities
    for i in range(n):
        comp_name = input(f"Enter the name of component {i+1}: ")
        comp_complexity = float(input(f"Enter the complexity level of {comp_name}: "))
        comp_scaling = float(input(f"Enter the time-scaling factor for {comp_name}: "))
        
        components[comp_name] = comp_complexity
        time_scaling_factors[comp_name] = comp_scaling
    
    # Calculate total time required
    total_time = calculate_total_time(components, time_scaling_factors)
    
    print("\n--- Project Time Estimation ---")
    print(f"Total Time Required: {total_time:.2f} weeks")
    
    # Optionally, print detailed breakdown
    print("\nDetailed Breakdown:")
    for comp in components:
        time = time_scaling_factors[comp] * components[comp]
        print(f"Time for {comp}: {time:.2f} weeks")
    
if __name__ == "__main__":
    main()
