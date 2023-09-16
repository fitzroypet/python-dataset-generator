# python-dataset-generator
A python script to generate dataset and store in JSON format
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
