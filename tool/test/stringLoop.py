import random

# Define the template string with placeholders
template = "This is iteration {}, and random value is {}"

# Number of iterations
num_iterations = 5

# Loop for a specified number of times
for i in range(num_iterations):
    # Generate random or changing values for variables
    iteration_number = i + 1  # 1-based index
    random_value = random.randint(1, 100)
    
    # Replace placeholders with variable values
    result_string = template.format(iteration_number, random_value)
    
    # Print or store the resulting string
    print(result_string)