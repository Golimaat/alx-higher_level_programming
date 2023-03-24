
devjokar
/
alx-higher_level_programming
Public
Code
Issues
Pull requests
Actions
More
alx-higher_level_programming/0x0F-python-object_relational_mapping/2-my_filter_states.py /

Josi Karachi Chmod all task files
 0 contributors
Executable File  21 lines (18 sloc)  525 Bytes
#!/usr/bin/python3
"""
Lists all values in the states tables of a database where name
matches the argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * \
    FROM states \
    WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS = '{}';".format(sys.argv[4]))
    states = cur.fetchall()

    for state in states:
        print(state)
