from main import (
    aggregate_data,
    filter_data,
    is_numeric,
    parse_condition,
    read_csv,
)
import pytest


@pytest.fixture
def sample_csv(tmp_path):
    csv_data = """name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
poco x5 pro,xiaomi,299,4.4"""
    file_path = tmp_path / 'test.csv'
    with open(file_path, 'w') as f:
        f.write(csv_data)
    return file_path


def test_read_csv(sample_csv):
    data = read_csv(sample_csv)
    assert len(data) == 4
    assert data[0]['name'] == 'iphone 15 pro'
    assert data[1]['brand'] == 'samsung'


def test_filter_data(sample_csv):
    data = read_csv(sample_csv)
    filtered = filter_data(data, 'price>1000')
    assert len(filtered) == 1
    assert filtered[0]['name'] == 'galaxy s23 ultra'

    filtered = filter_data(data, 'brand=xiaomi')
    assert len(filtered) == 2
    assert all(row['brand'] == 'xiaomi' for row in filtered)


def test_aggregate_data(sample_csv):
    data = read_csv(sample_csv)
    result = aggregate_data(data, 'price=avg')
    assert result[0]['avg'] == 674.0

    result = aggregate_data(data, 'price=min')
    assert result[0]['min'] == 199.0

    result = aggregate_data(data, 'price=max')
    assert result[0]['max'] == 1199.0


def test_parse_condition():
    assert parse_condition('price>1000') == ('price', '>', '1000')
    assert parse_condition('brand=xiaomi') == ('brand', '=', 'xiaomi')
    assert parse_condition('rating<5') == ('rating', '<', '5')


def test_is_numeric():
    assert is_numeric('100') is True
    assert is_numeric('4.5') is True
    assert is_numeric('abc') is False
