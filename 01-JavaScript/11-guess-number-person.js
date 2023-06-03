const prompt = require("prompt-sync")({ sigint: true });
/* We are guessing which number the computer is thinking of. */

console.log("I am thinking of a number between 0 and 5.");

const randomNumber = Math.floor(Math.random() * 6);

let guessNumber = parseInt(prompt("Take a guess: "));

let guessCount = 1;

if (guessNumber !== randomNumber) {
    while (guessNumber !== randomNumber) {
        guessNumber = parseInt(prompt("Nope! Take a new guess: "));
        guessCount += 1;
    }
    console.log(`You got it! It was number: ${randomNumber}. It has taken you ${guessCount} guesses.`);

} else {
    console.log("You got it from the first attempt!");
}


