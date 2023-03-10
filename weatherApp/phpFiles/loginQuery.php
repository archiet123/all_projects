<?php
//starting the session
session_start();
//including the database connection
require_once 'connection.php';

$_SESSION['hello'] = "hello there";
// Setting variables

$username = $_POST['username'];
$password = $_POST['password'];

if ($username == "" or $password == "") {
    $_SESSION['empty'] = "One or more of the fields are empty.";
    //redirecting to the index.php 
    header('location: /login.php');
    exit();
}
//gets password and hashes it ready to be compared.    

//Select query for getting already hashed passwords in database and comparing them to a newly hashed password
$query = "SELECT * FROM `userDetails` WHERE `Username` = :username OR `Email` = :email";
$stmt = $conn->prepare($query);
$stmt->bindParam(':username', $username);
$stmt->bindParam(':email', $username);
$stmt->execute();
$row = $stmt->fetch();

if (password_verify($password, ($row[4]))) {
    $_SESSION["user"] = $username;
    $user = $_SESSION['user'];
    $userMessage = "Welcome back $user, you have been signed in";
    $_SESSION["userMessage"] = $userMessage;
    $_SESSION["user_id"] = ($row[0]);
    header('location: ../index.php');

    exit();
} else {
    $_SESSION['error'] = "Invalid username or password";
    echo "data did not match";
    header('location: ../login.php');
    exit();
}
