<!DOCTYPE html>
<html lang="en">
<head>
    <link href="styles.css" rel="stylesheet">
    <title>Weather App</title>
</head>
<body>
    <section class="navigation">
        <div class="navContainer">
            <nav class="navBar">
                <div class="leftNav">
                    <a class="navButton" id="active" href="index.php">Home</a>
                    <a class="navButton" href="healthAdvice.php">Health Advice</a>
                    <a class="navButton" href="airConditions.php">Air Conditions</a>
                    <a class="navButton" href="more.php">More</a>
                    <a class="navButton" href="things.php">Things</a>
                </div>                
                <div class="rightNav">                
                    <a class="navButton" href="register.php">Register</a>
                    <a class="navButton" href="login.php">Login</a>                
                </div>
            </nav>
        </div>
    </section>
    <section class="main">
        <div class="backGround">
            <img src="/assests/weatherBackground.png" width="100%" alt="Raining">
            <div class="searchbarContainer">
                <p1 class="heading">Enter your area!</p1>
                <input class="input" type="text" placeholder="Find your area">
            </div>
        </div>
    </section>
</body>
</html>