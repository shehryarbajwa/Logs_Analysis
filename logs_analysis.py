#!/usr/bin/env python3
"""Logs analysis Udacity Project Full Stack Nano-degree"""
import sys
import psycopg2


DBNAME = "news"


"""Connect to the database and execute the query"""

# Connect to the database named news
# Open cursor for use with query
# Execute the query
# Store the results of the query using fetchall
# Close database connection
# Return the result


def execute_query(query):

    try:
        connection = psycopg2.connect(database=DBNAME)
        c = connection.cursor()
        c.execute(query)
        results = c.fetchall()
        connection.close()
        print(results)
        return results
    except psycopg2.Error as e:
        print(e)
        sys.exit(1)


question_1 = "What are the most popular three articles of all time?"

query_1 = """
select title, count(*) as views from articles inner join
log on concat('/article/', articles.slug) = log.path
where log.status like '%200%'
group by articles.title order by views desc limit 3;
"""

question_2 = "What are the most popular article authors of all time?"
query_2 = """
select authors.name, count(*) as views from articles
inner join authors on articles.author = authors.id
inner join log on concat('/article/', articles.slug) = log.path
where log.status like '%200%'
group by authors.name order by views desc;
"""

question_3 = "On which days did more than 1% of requests lead to errors?"
query_3 = """
select * from (
    select a.day,
    round(cast((100*b.count) as numeric) / cast(a.count as numeric), 2)
    as errorpercentage from
    (select date(time) as day, count(*) as count from log group by day) as a
    inner join
    (select date(time) as day, count(*) as count from log where
    log.status like '%404%' group by day) as b
    on a.day = b.day)
    as p where errorpercentage > 1.0;
"""

"""Execute each query"""
q1 = execute_query(query_1)
q2 = execute_query(query_2)
q3 = execute_query(query_3)

print(
    "\n"
)


def print_results(q_list):
    for i in range(len(q_list)):
        title = q_list[i][0]
        res = q_list[i][1]
        print("\t" + "%s - %d" % (title, res) + " views")
    print("\n")


print(question_1)


print_results(q1)


print(question_2)


print_results(q2)


print(question_3)


def print_q3(query):
    for key, value in query:
        print("\t{} - {} %".format(key, value))


print("\n")


print_q3(q3)
