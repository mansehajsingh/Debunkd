document.getElementById("results").style.display = "none"; // we don't want the results item to open right away
document.getElementById("conclusion-tag").style.display = "none"; // nor do we want this
document.getElementById("article-error-tag").style.display = "none";

 // sends article text to server for evaluation
function sendArticle() {

    document.getElementById("article-error-tag").style.display = "none";

    let articleText = document.getElementById("articletext").value;

    if(articleText && articleText.split(" ").length >= 50) {

        $.ajax({
            type: "POST",
            contentType: 'application/json',
            url: "/debunk",
            data: JSON.stringify({
                'messageType': '1',
                'articleText': articleText
            }),
            success: function(result) {

                let response = JSON.parse(result);
                
                // we want to make the elements visible
                document.getElementById("results").style.display = "flex";
                document.getElementById("conclusion-tag").style.display = "block";

                let fakeProbability = Math.round(parseFloat(response['fakeProba']));
                let realProbability = Math.round(parseFloat(response['realProba']));
                let conclusion = response['conclusion'];

                document.getElementById("fake-tag").innerHTML = `Fake (${fakeProbability}% Probability)`;
                document.getElementById("real-tag").innerHTML = `Real (${realProbability}% Probability)`;
                document.getElementById("conclusion-inner").innerHTML = conclusion;

                switch(response['state']){ // setting the color of the conclusion-inner tag
                    case 1:
                        document.getElementById("conclusion-inner").style.color = "#FFBC0A";
                        break;
                    case 2:
                        document.getElementById("conclusion-inner").style.color = "#E83151";
                        break;
                    case 3:
                        document.getElementById("conclusion-inner").style.color = "#8AC926";
                        break;
                }

                document.getElementById("real-bar").style.width = `${realProbability}%`

            }
        });

    } else if(articleText && articleText.split(" ").length < 50) { // if article length is under 50 words
        document.getElementById("article-error-tag").innerHTML = "Please enter at least 50 words.";
        document.getElementById("article-error-tag").style.display = "block";
    } else { // if article text is left empty
        document.getElementById("article-error-tag").innerHTML = "You have left the article text empty.";
        document.getElementById("article-error-tag").style.display = "block";
    }

}

// clears the text area
function clearText() {
    document.getElementById("articletext").value = "";
}