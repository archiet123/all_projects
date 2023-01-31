<?php
$dir = 'sqlite:./db.sqlite';
$dbh  = new PDO($dir) or die("cannot open the database");
$query =  "SELECT * FROM Album";
foreach ($dbh->query($query) as $row)
{
    echo $row[0] . "<br />";
}
$dbh = null; //This is how you close a PDO connection