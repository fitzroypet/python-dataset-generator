# Fictitious Service Provider Data Generator

This Python script generates fictitious service provider data and saves it to a JSON file. It's designed to create mock data for service providers offering services in the categories of Cleaning, Delivery, and Shopping.

## Features

- Generates fictitious service provider profiles with the following details:
  - Name
  - Location (randomly selected from New York, Los Angeles, Chicago, or Miami)
  - Services Offered (based on the selected category)
  - Ratings (a random rating between 1 and 5, rounded to 2 decimal places)
  - Number of Reviews (a random number between 0 and 100)

- Supports three main service categories:
  - Cleaning (with services like House Cleaning, Carpet Cleaning, and Window Cleaning)
  - Delivery (with services like Food Delivery, Package Delivery, and Grocery Delivery)
  - Shopping (with services like Personal Shopping, Grocery Shopping, and Clothing Shopping)

- Generates a specified number of fictitious service providers (adjustable via `num_providers`).

- Outputs the generated data in JSON format and saves it to a user-defined JSON file (`service_providers.json` by default).

## Usage

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   ```

2. Navigate to the repository directory:
   ```bash
   cd your-repo
   ```

3. Edit the script parameters if needed:
   - Adjust the `num_providers` variable to specify the number of fictitious service providers to generate.
   - Modify the `output_file` variable to set the output JSON file name.

4. Run the script:
   ```bash
   python your_script_name.py
   ```

5. The generated data will be saved to the specified JSON file.

## Example Output

The script will generate data similar to the following JSON format:

```json
[
    {
        "name": "Fictitious Cleaning Service",
        "location": "New York",
        "services_offered": ["House Cleaning", "Carpet Cleaning", "Window Cleaning"],
        "ratings": 4.12,
        "reviews": 73
    },
    {
        "name": "Fictitious Shopping Service",
        "location": "Los Angeles",
        "services_offered": ["Personal Shopping", "Grocery Shopping", "Clothing Shopping"],
        "ratings": 3.75,
        "reviews": 88
    },
    // ...
]
```

## License

This script is provided under the [MIT License](LICENSE).

Feel free to use, modify, and distribute it as needed for your projects.

Happy data generation!

```

Replace `"yourusername/your-repo.git"` with the actual GitHub repository URL where you plan to host your Python script. You can also customize the content further to include additional information or specific instructions relevant to your project.
