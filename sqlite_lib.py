import sqlite3;

conn: any = None
cursor: any = None


def connect(file_name: str) -> any:
    global conn, cursor
    conn = sqlite3.connect(file_name)
    conn.row_factory = sqlite3.Row # allow to use column names
    cursor = conn.cursor()  # Create cursor


def run_query_select(query: str) -> list[tuple]:
    cursor.execute(query)
    columns = cursor.fetchall()
    result = [tuple(row) for row in columns]
    return result


def run_query_update(query: str) -> None:
    cursor.execute(query)
    cursor.connection.commit()


def membership_count(member_type: str) -> list[tuple]:
    member_cnt: list[tuple] = run_query_select(f'''
                                       SELECT count(*) 
                                       FROM customers
                                       where LOWER("Membership Type") = '{member_type}';          
                                   ''');

    return member_cnt;


def close():
    cursor.close();