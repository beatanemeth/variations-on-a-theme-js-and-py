const prompt = require("prompt-sync")({ sigint: true });

const word = prompt("Enter any word, all in lowercase: ");
const firstChar = word.slice(0, 1)
const firstUpper = firstChar.toUpperCase();
const restChar = word.slice(1, word.length);
console.log("\nLook, I can turn your word's first character into uppercase: \n" + firstUpper + restChar);