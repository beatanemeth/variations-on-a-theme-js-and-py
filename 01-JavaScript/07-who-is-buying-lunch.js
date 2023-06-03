const prompt = require("prompt-sync")({ sigint: true });

const yourInput = prompt("Enter names separated by space: ");

const names = yourInput.split(" ");
console.log(names.length);

function whosPaying(names) {

    const random = Math.floor(Math.random() * names.length);

    const randomName = names[random];

    console.log(randomName + " is going to buy lunch today!")
}

whosPaying(names);