import pytest
from main import sort_by_population, sort_by_area, pretty_print_the_data


@pytest.mark.parametrize(
    'data, descending_order, result',
    [
        ([
             ['Ukraine', 602000, 38000000],
             ['Poland', 312696, 37500000],
             ['USA', 9834000, 331900000],
             ['Germany', 357588, 83200000],
             ['Japan', 377973, 125700000]
         ],
         True,
         [
             ['USA', 9834000, 331900000],
             ['Japan', 377973, 125700000],
             ['Germany', 357588, 83200000],
             ['Ukraine', 602000, 38000000],
             ['Poland', 312696, 37500000]
         ]),
        ([
             ['Ukraine', 602000, 38000000],
             ['Poland', 312696, 37500000],
             ['USA', 9834000, 331900000],
             ['Germany', 357588, 83200000],
             ['Japan', 377973, 125700000]
         ],
         False,
         [
             ['Poland', 312696, 37500000],
             ['Ukraine', 602000, 38000000],
             ['Germany', 357588, 83200000],
             ['Japan', 377973, 125700000],
             ['USA', 9834000, 331900000]
         ])
    ]
)
def test_sort_by_population(data, descending_order, result):
    assert sort_by_population(data, descending_order) == result


@pytest.mark.parametrize(
    'data, descending_order, result',
    [
        ([
             ['Ukraine', 602000, 38000000],
             ['Poland', 312696, 37500000],
             ['USA', 9834000, 331900000],
             ['Germany', 357588, 83200000],
             ['Japan', 377973, 125700000]
         ],
         True,
         [
             ['USA', 9834000, 331900000],
             ['Ukraine', 602000, 38000000],
             ['Japan', 377973, 125700000],
             ['Germany', 357588, 83200000],
             ['Poland', 312696, 37500000]
         ]),
        ([
             ['Ukraine', 602000, 38000000],
             ['Poland', 312696, 37500000],
             ['USA', 9834000, 331900000],
             ['Germany', 357588, 83200000],
             ['Japan', 377973, 125700000]
         ],
         False,
         [
             ['Poland', 312696, 37500000],
             ['Germany', 357588, 83200000],
             ['Japan', 377973, 125700000],
             ['Ukraine', 602000, 38000000],
             ['USA', 9834000, 331900000]
         ])
    ]
)
def test_sort_by_area(data, descending_order, result):
    assert sort_by_area(data, descending_order) == result


@pytest.fixture
def input_value():
    return [
        ['USA', 9834000, 331900000],
        ['Ukraine', 602000, 38000000],
        ['Japan', 377973, 125700000],
        ['Germany', 357588, 83200000],
        ['Poland', 312696, 37500000]
    ]


def test_pretty_print_the_data(input_value):
    assert pretty_print_the_data(input_value) == [
        '\nCountry 1\nName: USA\nArea: 9834000\nPopulation: 331900000\n',
        '\nCountry 2\nName: Ukraine\nArea: 602000\nPopulation: 38000000\n',
        '\nCountry 3\nName: Japan\nArea: 377973\nPopulation: 125700000\n',
        '\nCountry 4\nName: Germany\nArea: 357588\nPopulation: 83200000\n',
        '\nCountry 5\nName: Poland\nArea: 312696\nPopulation: 37500000\n',
    ]
