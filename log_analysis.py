from datetime import datetime
import psycopg2

# Connect to database
conn = psycopg2.connect('dbname=news')
cur = conn.cursor()

# Find top three articles and print results
cur.execute('''
select articles.title, count(*) as num
from articles, log
where log.path = '/article/' || articles.slug
group by articles.title
order by num desc
limit 3;
''')
result = cur.fetchall()
print('What are the most popular three articles of all time?')

for i in range(len(result)):
    print('\t"' + result[i][0] + '" — ' + str(result[i][1]) + ' views')

# Find top authors and print results
cur.execute('''
select authors.name, count(*) as num
from articles, log, authors
where log.path = '/article/' || articles.slug
and authors.id = articles.author
group by authors.id
order by num desc
''')
result = cur.fetchall()
print('Who are the most popular article authors of all time?')

for i in range(len(result)):
    print('\t"' + result[i][0] + '" — ' + str(result[i][1]) + ' views')

# Fetch dates where http error exceeds 1% and print results
cur.execute('''
select data.date, (data.error::float / data.total::float) * 100 as rate from
    (select total.date as date, error.num as error, total.num as total from
        (select time::date as date, count(*) as num from log group by date)
        as total,
        (select time::date as date, count(*) as num from log
        where status !~ '200 OK' group by date) as error
where error.date = total.date
group by total.date, error.num, total.num
order by error.num desc) as data
where (data.error::float / data.total::float) * 100 > 1;
''')
result = cur.fetchall()
print('On which days did more than 1% of requests lead to errors?')

for i in range(len(result)):
    print('\t"' +
          datetime.strptime(str(result[i][0]), '%Y-%m-%d')
          .strftime('%B %d, %Y') +
          '" — ' + str("{:0.1f}".format(result[i][1])) + '% errors')

conn.commit()
cur.close()
conn.close()
