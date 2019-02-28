#developed by sravani
# Log-Analysis-Project
An internal reporting tool that uses information of large database of a web server and draw business conclusions from that information. (Project from Full Stack Web Development Nanodegree)

# Introduction
This is a python module that uses information of large database of a web server and draw business conclusions from that information. The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. The database includes three tables:

The authors table includes information about the authors of articles.
The articles table includes the articles themselves.
The log table includes one entry for each time a user has accessed the site.
The project drives following conclusions:
what are the Most trendenious three articles of all time.
who are Most trendinious articles of all time.
Days on which more than 1% of requests lead to errors.
