# Logs-analysis
<h1>Udacity Logs Analysis Project</h1>

<h2><b>Project OverView</b></h2>
<br>
The project requires students to create and use SQL queries that would fetch results from a large database of a news website.The goal of the project is to build students' SQL skills. The requirements of the project require one query per question used to answer each question. The code in logs_analysis.py runs three queries to answer three different questions.

<h2><b>Requirements</b></h2>
<li><a href="https://www.python.org/download/releases/3.0/" rel="nofollow">Python 3</a> The code in logs_analysis runs on Python 3.7.4 </li>
<li><a href="https://www.postgresql.org/about/" rel="nofollow">PostGreSQL</a> PostGreSQL is used for SQL queries</li>
<li><a href="https://www.vagrantup.com/" rel="nofollow">Vagrant</a> A virtual environment builder and manager </li>
<li><a href="https://www.virtualbox.org/" rel="nofollow">VirtualBox</a> Open source virtualization software</li>

<h2><b>How to run the Project</b></h2>
<ol>
  <li>To get started, I recommend the user use a virtual machine to ensure they are using the same environment that this project was developed on, running on your computer. You can download Vagrant and VirtualBox to install and manage your virtual machine. Use vagrant up to bring the virtual machine online and vagrant ssh to login.</li>

<li>Download the data provided by Udacity here. Unzip the file in order to extract newsdata.sql. This file should be inside the Vagrant folder.</li>

<li>Load the database using psql -d news -f newsdata.sql.</li>

<li>Connect to the database using psql -d news -f news/newsdata.sql.</li>

<li>Now execute the Python file - python logs_analysis.py.</li>

</ol>
