<?php

//starting the session
session_start();

//including the database connection
require_once 'connection.php';

// Setting variables

$email = $_POST['email'];
$number = $_POST['number'];
$username = $_POST['username'];
$password = $_POST['password'];
$passoword2 = $_POST['password2'];

function checkUsernames($email, $username, $conn)
{
    $query = "SELECT * FROM `userDetails` WHERE `Username` = :username OR `Email` = :email";

    $stmt = $conn->prepare($query);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':username', $username);
    $row = $stmt->fetch();

    $value = $row;
    if ($value == '') {
        return false;
    } else {
        return true;
    }
}

function checkNumber($number, $conn)
{
    $query = "SELECT * FROM `userDetails` WHERE `mobile` = :number";

    $stmt = $conn->prepare($query);
    $stmt->bindParam(':number', $number);
    $row = $stmt->fetch();

    $value = $row;
    if ($value == '') {
        return false;
    } else {
        return true;
    }
}


if ($email == "" or $number == "" or $username == "" or $password == "" or $passoword2 == "") {
    $_SESSION['empty'] = "One or more of the fields are empty.";
    //redirecting to the index.php 
    header('location: /register.php');
    exit();
} elseif (strlen($number) != 11) {
    $_SESSION['invalid'] = "You have not entered a valid mobile number.";
    header('location: /register.php');
    exit();
} elseif (checkUsernames($email, $username, $conn) == True) {
    $_SESSION['userTaken'] = "This username or email are already in use.";
    header('location: /register.php');
    exit();
} elseif (checkNumber($number, $conn) == True) {
    $_SESSION['numberTaken'] = "This username or email are already in use.";
    header('location: /register.php');
} elseif ($password != $passoword2) {
    $_SESSION['pass_error'] = "Passwords do not match";
    header('location: /register.php');
} else {
    $pass = password_hash($password, PASSWORD_DEFAULT);

    // Insertion Query

    $query = "INSERT INTO `userDetails` (email, mobile, userName, passWord) VALUES(:email, :number, :username, :pass)";
    $stmt = $conn->prepare($query);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':number', $number);
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':pass', $pass);


    // Check if the execution of query is success
    if ($stmt->execute()) {
        //setting a 'success' session to save our insertion success message.
        $_SESSION['success'] = "Successfully created an account";
        //redirecting to the index.php 
        header('location: /register.php');
    } else {
        echo "not working";
        header('location: /register.php');
    }
}
