const prompt = require("prompt-sync")({ sigint: true });

/* The computer is guessing which number we are thinking of. */

const myNumber = prompt("I am thinking of a number between 0 and 5. It is number: ");

let gotIt = false;

let numberOfGuesses = 1;

while (gotIt == false) {
    let randomGuessNumber = Math.floor(Math.random() * 6);
    console.log(`Computer guess: ${randomGuessNumber}`);

    if (randomGuessNumber == myNumber) {
        gotIt = true;
        console.log(`Got it! It was a ${randomGuessNumber}. It has taken me ${numberOfGuesses} guesses.`)

    } else {
        numberOfGuesses += 1;
    }
}
