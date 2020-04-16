# Logs-analysis
<h1>Udacity Logs Analysis Project</h1>

<h2><b>Project OverView</b></h2>
<br>

<h2><b>Requirements</b></h2>
<li><a href="https://www.python.org/download/releases/3.0/" rel="nofollow">Python 3</a> The code in logs_analysis runs on Python 3.7.4 </li>
<li><a href="https://www.postgresql.org/about/" rel="nofollow">PostGreSQL</a> PostGreSQL is used for SQL queries</li>
<li><a href="https://www.vagrantup.com/" rel="nofollow">Vagrant</a> A virtual environment builder and manager </li>
<li><a href="https://www.virtualbox.org/" rel="nofollow">VirtualBox</a> Open source virtualization software</li>

<h2><b>How to run the Project</b></h2>
<ol>
  <li>To get started, download a virtual machine. In my case I used Vagrant. You can download Vagrant and VirtualBox to install and manage your virtual machine. Use vagrant up to bring the virtual machine online and vagrant ssh to login.</li>

<li>Download the data here <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip" rel="nofollow">here</a>. Unzip the file in order to extract newsdata.sql. Place this file inside the Vagrant folder.</li>

<li>Load the database using psql -d news -f newsdata.sql.</li>

<li>Connect to the database using psql -d news -f news/newsdata.sql.</li>

<li>Now execute the Python file - python logs_analysis.py.</li>

</ol>

