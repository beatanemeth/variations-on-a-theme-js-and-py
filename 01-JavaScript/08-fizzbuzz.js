const prompt = require("prompt-sync")({ sigint: true });

const output = [];

function fizzBuzz() {

    for (count = 1; count <= 5; count++) {
        const myNumber = prompt("Write a hole number: ");
        output.push(myNumber);
    }

    console.log("Your numbers: " + output.join(", "));

    const myNumArray = [];
    output.forEach(item => {
        let myOutput = "";
        if (item % 3 == 0) { myOutput += "Fizz"; }
        if (item % 5 == 0) { myOutput += "Buzz"; }
        if (myOutput == "") { myOutput = item; }

        myNumArray.push(myOutput);
    })

    console.log("\nNumbers replaced with Fizz/Buzz: " + myNumArray.join(", "));

};

fizzBuzz();