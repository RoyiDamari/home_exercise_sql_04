import sqlite_lib as sl


def main():
    sl.connect('CustomerBehavior.db')
# Exercise 2
    cnt_customer: list[tuple] = sl.run_query_select('''
            SELECT count(*)
            FROM customers;
        ''');

    print(cnt_customer);

    avg_age: list[tuple] = sl.run_query_select('''
                SELECT avg(Age)
                FROM customers;
            ''');

    print(avg_age);

    cnt_gender: list[tuple] = sl.run_query_select('''
                    SELECT Gender, count(*)
                    FROM customers
                    group by Gender;
                ''');

    print(cnt_gender);

    avg_sales: list[tuple] = sl.run_query_select('''
                        SELECT Gender, avg("Items Purchased")
                        FROM customers
                        group by Gender;
                    ''');

    print(avg_sales);

    membership_type: list[tuple] = sl.run_query_select('''
                           SELECT count(DISTINCT "Membership Type")
                           FROM customers;
                       ''');

    print(membership_type);

    cnt_membership_type: list[tuple] = sl.run_query_select('''
                               SELECT "Membership Type", count(*) 
                               FROM customers
                               group by "Membership Type";
                           ''');

    print(cnt_membership_type);

    new_york_city_members: list[tuple] = sl.run_query_select('''
                                   SELECT count(*) 
                                   FROM customers
                                   where City = "New York";
                               ''');

    print(new_york_city_members);

    city_members: list[tuple] = sl.run_query_select('''
                                       SELECT City, count(*) cnt
                                       FROM customers
                                       group by City
                                       order by cnt desc;
                                   ''');

    print(city_members);

    total_spend: list[tuple] = sl.run_query_select('''
                                           SELECT Gender, sum("Total Spend") 
                                           FROM customers
                                           group by Gender;
                                       ''');

    print(total_spend);

    max_min_sales: list[tuple] = sl.run_query_select('''
                                              SELECT "Customer ID", "Items Purchased" ip 
                                              FROM customers
                                              where ip = (SELECT min("Items Purchased") 
                                                          FROM customers)
                                              or ip = (SELECT max("Items Purchased") 
                                                                      FROM customers)
                                              order by ip;          
                                          ''');

    print(max_min_sales);

    while True:
        # Validate the year input
        try:
            # Accept input from the user
            member_type: str = input("Enter your member type: ").lower();
            if any(char.isdigit() for char in member_type):
                raise ValueError("member type can't be a number");
            break;

        except ValueError as e:
            print(e);

    result: list[tuple] = sl.membership_count(member_type);

    print(result);

    sl.close();


if __name__ == "__main__":
    main();
