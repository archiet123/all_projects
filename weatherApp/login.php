<!DOCTYPE html>
<html lang="en">
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
                    <a class="navButton" href="register.php">Register</a>
                    <a class="navButton" id="active" href="login.php">Login</a>
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
            <a class="navButton" id="active" href="index.php">Home</a>
            <a class="navButton" href="healthAdvice.php">Health Advice</a>
            <a class="navButton" href="polutionLevels.php">Polution levels</a>
            <a class="navButton" href="more.php">More</a>
            <a class="navButton" href="things.php">Things</a>
            <a class="navButton" href="register.php">Register</a>
            <a class="navButton" href="login.php">Login</a>
        </div>
    </section>

    <section class="loginContainer">

        <div class="logoWrapper">
            <img class="logo" src="/assests/companyIcon.jpg" alt="company icon" width="100px">
        </div>
        <div class="headingWrapper">
            <h1 class="heading">Log in</h1>
        </div>

        <form method="POST" class="loginForm" action="login.php">
        <div class="inputWrapper">
            <input class="username inputBox" type="text" placeholder="Email or username">
        </div>
        <div class="divider"></div>
        <div class="inputWrapper">
            <input class="password inputBox" type="password" placeholder="Password ">
        </div>
        <div class="divider"></div>
        
    </section>
</body>
</html>