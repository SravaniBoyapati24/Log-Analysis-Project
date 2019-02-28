#!/usr/bin/env python
import psycopg2
# first top 3 articles execution


def trend_artifacts():
    conne1 = psycopg2.connect(
        dbname="news", user='vagrant', password='vagrant')
    concur = conne1.cursor()
    queryq1 = ''' SELECT title, views FROM logstipulation INNER JOIN articles ON
    articles.slug = logstipulation.slug ORDER BY views desc LIMIT 3; '''
    concur.execute(queryq1)
    resultr1 = concur.fetchall()
    print("\nI)**what are the mostly used trendeiness article name:\n")
    c = 1
    for r in resultr1:
        n = '[' + str(c) + ']-->'
        a = r[0]+'"'
        v = str(r[1])+" views are"+' '+'"'  
        print(n + v + a)
        c = c+1
        # print('"{0}"=>{1} views'.format(r[0], r[1]))


def trenines_penmans():
    conne2 = psycopg2.connect(
        dbname="news", user='vagrant', password='vagrant')
    concur = conne2.cursor()
    queryq2 = '''
    SELECT logedpenman.name AS author,sum(logstipulation.views) 
    AS views FROM logstipulation INNER JOIN logedpenman
    ON logedpenman.slug=logstipulation.slug
    GROUP BY logedpenman.name ORDER BY views desc limit 4;
    '''
    concur.execute(queryq2)
    resultr1 = concur.fetchall()
    print("\nII)**Who are the mostly trendines authors of all time: \n")
    c = 1
    for r in resultr1:
        n = '[' + str(c) + ']-->'
        t = r[0] + '"'
        v = str(r[1])+" views are"+' '+'"' 
        print(n + v + t)
        c = c+1
        # print('"{0}"=>{1} views'.format(r[0], r[1]))
# lead errors


def logerrorbankrupt():
    conne3 = psycopg2.connect(
        dbname="news", user='vagrant', password='vagrant')
    concur3 = conne3.cursor()
    queryq3 = '''
    SELECT errorlogflop.date ,(
    errorlogflop.count*100.00 / unsteinedtot.count) AS
    percentage FROM errorlogflop  INNER JOIN unsteinedtot
    ON errorlogflop .date = unsteinedtot.date
    AND (errorlogflop .count*100.00 / unsteinedtot.count) >1
    ORDER BY(errorlogflop.count*100.00 /unsteinedtot.count) desc;
    '''
    concur3.execute(queryq3)
    rst = concur3.fetchall()
    print(" \nDays on which more than 1% of requests lead to errors ? ")
    for r in rst:
        print('\n On' + str(r[0]) + '===>' + '%.1f' % r[1] + '% errors\n')
trend_artifacts()
trenines_penmans()
logerrorbankrupt()
