const prompt = require("prompt-sync")({ sigint: true });

const guestList = ["Angela", "Jack", "Pam", "James", "Lara", "Jason"];
const guestName = prompt("What is your name? ");
if (guestList.includes(guestName)) {
    console.log("Welcome!");
} else {
    console.log("You are not invited.")
}
