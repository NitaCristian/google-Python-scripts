#!/usr/bin/env python3

import json
import locale
import sys
import emails
import reports
import os


def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def format_car(car):
    """Given a car dictionary, returns a nicely formatted name."""
    return "{} {} ({})".format(
        car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
    """Analyzes the data, looking for maximums.

    Returns a list of lines that summarize the information.
    """
    max_revenue = {"revenue": 0}
    best_model = {}
    best_sales = 0
    years = {}

    for item in data:
        # Calculate the revenue generated by this model (price * total_sales)
        # We need to convert the price from "$1234.56" to 1234.56
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price
        if item_revenue > max_revenue["revenue"]:
            item["revenue"] = item_revenue
            max_revenue = item

        if item["total_sales"] > best_sales:
            best_sales = item["total_sales"]
            best_model = item

        index = item["car"]["car_year"]
        years[index] = years.get(index, 0) + item["total_sales"]

    best_year = sorted(years, key=years.get, reverse=True)[0]

    summary = [
        "The {} generated the most revenue: ${}".format(
            format_car(max_revenue["car"]), max_revenue["revenue"]),
        "The {} had the most sales: {}".format(
            format_car(best_model["car"]), best_sales),
        "The most popular year was {} with {} sales.".format(
            best_year, years[best_year])
    ]

    return summary


def cars_dict_to_table(car_data):
    """Turns the data in car_data into a list of lists."""
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in car_data:
        table_data.append([item["id"], format_car(
            item["car"]), item["price"], item["total_sales"]])
    return table_data


def main(argv):
    """Process the JSON data and generate a full report out of it."""
    data = load_data("../car_sales.json")
    summary = process_data(data)
    print(summary)
    reports.generate("/tmp/cars.pdf", "A Complete Inventory of My Fruit",
                     "<br/>".join(summary), cars_dict_to_table(data))
    emails.send(emails.generate("automation@example.com", "{}@example.com".format(
        os.environ.get('USER')), "Sales summary for last month", "\n".join(summary), "/tmp/cars.pdf"))


if __name__ == "__main__":
    main(sys.argv)
