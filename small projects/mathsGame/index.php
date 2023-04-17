<!DOCTYPE html>
<html lang="en">

<head>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
</head>

<body>
    <section class="title">
        <div class="PageTitle">
            <h1 class="titleText">Multiplication Game</h1>
        </div>
        <div class="subheading">
            <h2 class="displayText">Practice your multiplication knowledge</h2>
        </div>
    </section>

    <section class="mainContent">
        <div class="mathsQuestion">
            <div class="textContainer">
                <h1 id="numb1">1</h1>
            </div>
            <h1 class="displayText">X</h1>

            <div class="textContainer">
                <h1 id="numb2">3</h1>
            </div>
            <h1 class="displayText">=</h1>

            <input id="userAnswer" class="inputFormat" type="text">

        </div>
        <div id="answer-state"></div>
        <div class="countStreak">
            <div class="displayText streak">Streak: 
                <div id="userStreak"></div>
            </div>
        </div>
        
    </section>

    <script>
        let result = 0;
        var streakCounter = 0;

        function generateRandom(maxLimit = 12) {
            let rand = Math.random() * maxLimit;

            rand = Math.floor(rand);
            
            return Math.max(1, rand);
        }

        function placeNumbers() {
            let num1 = generateRandom()
            let num2 = generateRandom()
            document.getElementById("numb1").innerHTML = num1
            document.getElementById("numb2").innerHTML = num2

            result = num1 * num2;
        }


        placeNumbers()

        var userAnswer = document.getElementById("userAnswer")

        userAnswer.addEventListener("keydown", (e) => {
            console.log("sdkaig")
            if (e.key === "Enter") {
                if (result == userAnswer.value) {
                    removeExistingElement()        
                    createAnswerElement("Correct")
                    streakCounter = streakCounter +1                           
                } else {
                    removeExistingElement()
                    createAnswerElement("Incorrect")
                    streakCounter = 0               
                }
                placeNumbers()
                displayStreak()
                userAnswer.value = ""
            }


        });

        function displayStreak(){
           document.getElementById("userStreak").innerHTML = streakCounter
        }

        function createAnswerElement(text) {
          
            // Create element:
            const para = document.createElement("p");
            para.id = "tempValue";
            para.innerText = text;

            // Append to answer-state element:
            var answerState = document.getElementById("answer-state")

            answerState.appendChild(para);
            
        }

        function removeExistingElement(){
            const remove = document.getElementById("tempValue");
            console.log(typeof remove)
            if (remove) {
                // alert("remove")
                console.log("removed")
                remove.remove();
            } else {
            // alert("Element does not exist");
            }
        }
    </script>

</body>

</html>