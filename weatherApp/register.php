<!DOCTYPE html>
<html lang="en">

<?php

session_start();

?>

<head>
    <link href="styles.css" rel="stylesheet">
    <title>Weather App</title>
    <link rel="stylesheet" href="https://kit.fontawesome.com/56ec8ed5e8.css" crossorigin="anonymous">
    <script src="https://kit.fontawesome.com/56ec8ed5e8.js" crossorigin="anonymous"></script>
    <script src="/app.js" crossorigin="anonymous"></script>
</head>

<body>
    <section class="navigation wide">
        <div class="navContainer">
            <nav class="navBar">
                <div class="leftNav">
                    <a class="navButton" href="index.php">Home</a>
                    <a class="navButton" href="healthAdvice.php">Health Advice</a>
                    <a class="navButton" href="polutionLevels.php">Polution levels</a>
                    <a class="navButton" href="more.php">More</a>
                    <a class="navButton" href="things.php">Things</a>
                </div>
                <div class="rightNav">
                    <a class="navButton" id="active" href="register.php">Register</a>
                    <a class="navButton" href="login.php">Login</a>
                </div>
            </nav>
        </div>
    </section>

    <div class="slim-nav">
        <div>
            <i id="nav-icon" class="fa-regular fa-bars"></i>
        </div>
    </div>
    <section id="slim-nav" class="navigation hidden slim blackBackground">
        <div class="slim-menu">
            <a class="navButton" href="index.php">Home</a>
            <a class="navButton" href="healthAdvice.php">Health Advice</a>
            <a class="navButton" href="polutionLevels.php">Polution levels</a>
            <a class="navButton" href="more.php">More</a>
            <a class="navButton" href="things.php">Things</a>
            <a class="navButton" id="active" href="register.php">Register</a>
            <a class="navButton" href="/desgin/login.php">Login</a>
        </div>
    </section>

    <section class="registrationContainer">

        <div class="logoWrapper">
            <img class="logo" src="/assests/companyIcon.jpg" alt="company icon" width="100px">
        </div>
        <div class="headingWrapper">
            <h1 class="heading">Register an account!</h1>
        </div>

        <form method="POST" class="registrationForm" action="/phpFiles/registrationQuery.php">

            <div class="inputWrapper">
                <input class="email inputBox" type="text" name="email" placeholder="Email">
            </div>
            <div class="divider"></div>

            <div class="inputWrapper">
                <input class="number inputBox" type="text" name="number" placeholder="Phone">
            </div>
            <div class="divider"></div>

            <div class="inputWrapper">
                <input class="username inputBox" type="text" name="username" placeholder="Username">
            </div>
            <div class="divider"></div>

            <div class="inputWrapper">
                <input class="password inputBox" type="password" name="password" placeholder="Password ">
            </div>
            <div class="divider"></div>

            <div class="inputWrapper">
                <input class="password inputBox" type="password" name="password2" placeholder="Confirm Password ">
            </div>
            <div class="divider"></div>

            <div class="forgotPasswordwrapper">
                <a class="forgotPassword" href="newPassword.php">Forgot password?</a>
            </div>


            <div class="submitButton">
                <button class="Submit" type="submit">Register</button>
            </div>
        </form>

        <?php
        //checking if the session 'error' is set. Erro session is the message if the 'Username' and 'Password' is not valid.
        if (isset($_SESSION['empty'])) {
        ?>
            <!-- Display Login Error message -->
            <div class="dangerAlert"><?php echo $_SESSION['empty'] ?></div>
        <?php
            //Unsetting the 'error' session after displaying the message. 
            unset($_SESSION['empty']);
        }
        ?>

        <?php

        if (isset($_SESSION['pass_error'])) {
        ?>

            <div class="dangerAlert"><?php echo $_SESSION['pass_error'] ?></div>
        <?php

            unset($_SESSION['pass_error']);
        }
        ?>

        <?php

        if (isset($_SESSION['success'])) {
        ?>

            <div class="accountCreated"><?php echo $_SESSION['success'] ?></div>
        <?php

            unset($_SESSION['success']);
        }
        ?>
    </section>


</body>

</html>