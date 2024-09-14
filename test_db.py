import sqlite_lib as sl
import pytest


@pytest.fixture
def before_after_operations_db():
    # BEFORE
    sl.connect('CustomerBehavior.db');

    yield;  # test_get_years

    # AFTER
    sl.close();


def test_gold_membership_count(before_after_operations_db):
    # Act
    result: list[tuple] = sl.run_query_select('''
                         SELECT count(*) 
                         FROM customers
                         where LOWER("Membership Type") = 'gold';
    ''');

    # Assert
    assert result == [(117,)];


def test_silver_membership_count(before_after_operations_db):
    # Act
    result: list[tuple] = sl.run_query_select('''
                         SELECT count(*) 
                         FROM customers
                         where LOWER("Membership Type") = 'silver';
    ''');

    # Assert
    assert result == [(117,)];


def test_bronze_membership_count(before_after_operations_db):
    # Act
    result: list[tuple] = sl.run_query_select('''
                         SELECT count(*) 
                         FROM customers
                         where LOWER("Membership Type") = 'bronze';
    ''');

    # Assert
    assert result == [(116,)];

