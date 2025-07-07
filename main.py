import argparse
import csv
from typing import Any, Dict, List

from tabulate import tabulate


def read_csv(file_path: str):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


def filter_data(data: List[Dict[str, Any]], condition: str):
    if not condition:
        return data

    column, operator, value = parse_condition(condition)

    filtered_rows = []
    for row in data:
        row_value = row[column]
        if operator == '=':
            if str(row_value) == value:
                filtered_rows.append(row)
        elif operator == '>':
            if is_numeric(row_value) and float(row_value) > float(value):
                filtered_rows.append(row)
        elif operator == '<':
            if is_numeric(row_value) and float(row_value) < float(value):
                filtered_rows.append(row)

    return filtered_rows


def parse_condition(condition: str):
    operators = ['>', '<', '=']
    for op in operators:
        if op in condition:
            parts = condition.split(op)
            if len(parts) == 2:
                return parts[0], op, parts[1]
    raise ValueError(f'Invalid condition format: {condition}')


def is_numeric(value: str):
    try:
        float(value)
        return True
    except ValueError:
        return False


def aggregate_data(data: List[Dict[str, Any]], aggregate: str):
    if not aggregate:
        return None

    column, operation = aggregate.split('=')

    numeric_values = []
    for row in data:
        value = row[column]
        if is_numeric(value):
            numeric_values.append(float(value))

    if not numeric_values:
        return None

    if operation == 'avg':
        result = sum(numeric_values) / len(numeric_values)
    elif operation == 'min':
        result = min(numeric_values)
    elif operation == 'max':
        result = max(numeric_values)
    else:
        raise ValueError(f'Unknown aggregation operation: {operation}')

    return [{'column': column, operation: result}]


def sort_data(data: List[Dict[str, Any]], order_by: str):
    if not order_by:
        return data

    column, order = order_by.split('=')

    if order not in ['desc', 'asc', '']:
        raise ValueError(f'Unknown order value: {order}')

    def sort_key(row):
        value = row[column]
        return float(value) if is_numeric(value) else value

    reverse = order == 'desc'
    return sorted(data, key=sort_key, reverse=reverse)


def main():
    parser = argparse.ArgumentParser(
        description='Process CSV file with filtering and aggregation.'
    )
    parser.add_argument(
        'file_path',
        type=str,
        help='Path to the CSV file',
        default='.csv',
    )
    parser.add_argument(
        '--where',
        type=str,
        help='Filter condition (e.g., "price>1000")',
        default='',
    )
    parser.add_argument(
        '--aggregate',
        type=str,
        help='Aggregation condition (e.g., "price=avg")',
        default='',
    )
    parser.add_argument(
        '--order-by',
        type=str,
        help='Sorting condition (e.g., "price=asc" or "name=desc")',
        default='',
    )

    args = parser.parse_args()

    data = read_csv(args.file_path)

    if args.where:
        data = filter_data(data, args.where)

    if args.order_by:
        data = sort_data(data, args.order_by)

    if args.aggregate:
        data = aggregate_data(data, args.aggregate)
        if not data:
            print('No numeric data to aggregate.')

    print(tabulate(data, headers='keys', tablefmt='grid'))


if __name__ == '__main__':
    main()
