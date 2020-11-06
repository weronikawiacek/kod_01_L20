# -*- coding: utf-8 -*-
from point import Point


def test_should_check_constructor_without_z():
    # given
    point_a = Point('A', 1, 1)

    # when
    # then
    assert point_a.name == 'A'
    assert point_a.x == 1
    assert point_a.y == 1
    assert point_a.z == 0


def test_should_check_constructor_with_z():
    # given
    point_a = Point('A', 1, 1, 1)

    # when
    # then
    assert point_a.name == 'A'
    assert point_a.x == 1
    assert point_a.y == 1
    assert point_a.z == 1


def test_should_check_print_method():
    # given
    point_a = Point('A', 1, 1, 1)

    # when
    # then
    assert point_a.__str__() == 'Point(nr="A", x=1, y=1, z=1)'


def test_should_check_lenght():
    # given
    begin_point = Point('P1245', 0, 0)
    end_point = Point('P12', 3, 4)

    # when
    # then
    assert begin_point.lenght(begin_point) == 0
    assert begin_point.lenght(end_point) == 5
    assert end_point.lenght(begin_point) == 5
