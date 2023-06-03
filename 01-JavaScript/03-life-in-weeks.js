const prompt = require("prompt-sync")({ sigint: true });

const yourAge = prompt("What is your age? ");

function timeLeft(age) {

    const currentAge = parseInt(age);

    const timeLeft = 90 - currentAge;

    const months = timeLeft * 12;
    const weeks = timeLeft * 52;
    const days = timeLeft * 365;

    console.log("You have " + days + " days, or " + weeks + " weeks, or " + months + " months left until age 90.");
}

timeLeft(yourAge);