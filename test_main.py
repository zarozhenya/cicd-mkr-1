import pytest
from main import sort_by_population, sort_by_area


@pytest.mark.parametrize(
    'data, descending_order, result',
    [
        ([['Ukraine', 602000, 38000000], ['Poland', 312696, 37500000], ['USA', 9834000, 331900000], ['Germany', 357588, 83200000], ['Japan', 377973, 125700000]],
        True,
        [['USA', 9834000, 331900000], ['Japan', 377973, 125700000], ['Germany', 357588, 83200000], ['Ukraine', 602000, 38000000], ['Poland', 312696, 37500000]]
         ),
([['Ukraine', 602000, 38000000], ['Poland', 312696, 37500000], ['USA', 9834000, 331900000], ['Germany', 357588, 83200000], ['Japan', 377973, 125700000]],
        False,
        [['Poland', 312696, 37500000], ['Ukraine', 602000, 38000000], ['Germany', 357588, 83200000], ['Japan', 377973, 125700000], ['USA', 9834000, 331900000]]
         )
    ]
)
def test_sort_by_population(data, descending_order, result):
    assert sort_by_population(data, descending_order) == result


@pytest.mark.parametrize(
    'data, descending_order, result',
    [
        ([['Ukraine', 602000, 38000000], ['Poland', 312696, 37500000], ['USA', 9834000, 331900000], ['Germany', 357588, 83200000], ['Japan', 377973, 125700000]],
        True,
        [['USA', 9834000, 331900000], ['Ukraine', 602000, 38000000], ['Japan', 377973, 125700000], ['Germany', 357588, 83200000], ['Poland', 312696, 37500000]]
         ),
([['Ukraine', 602000, 38000000], ['Poland', 312696, 37500000], ['USA', 9834000, 331900000], ['Germany', 357588, 83200000], ['Japan', 377973, 125700000]],
        False,
        [['Poland', 312696, 37500000], ['Germany', 357588, 83200000], ['Japan', 377973, 125700000], ['Ukraine', 602000, 38000000], ['USA', 9834000, 331900000]]
         )
    ]
)
def test_sort_by_area(data, descending_order, result):
    assert sort_by_area(data, descending_order) == result