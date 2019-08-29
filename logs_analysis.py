"""
Logs analysis Udacity Project Full Stack Nano-degree
"""
#!/usr/bin/env python3
import sys
import psycopg2

DBNAME="news"

def execute_query(query):

    try:
        #Connect to the database named news
        connection = psycopg2.connect(database=DBNAME)
        #Open cursor for use with query
        c = connection.cursor()
        #Execute the query
        c.execute(query)
        #Store the results of the query using fetchall
        results = c.fetchall()
        #Close database connection
        connection.close()
        #Return the result
        print(results)
        return results
    except psycopg2.Error as e:
        print(e)
        sys.exit(1)

question_1 = "What are the most popular three articles of all time?"
query_1 =  """
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

if __name__ == '__main__':
    execute_query(query_2)