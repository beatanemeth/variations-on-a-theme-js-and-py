const prompt = require("prompt-sync")({ sigint: true });

let fibonacciNumbers = [];

function fibonacciGenerator() {
    const numItems = prompt("Enter a whole number and get the list of Fibonacci's numbers: ");

    if (numItems === 1) {
        fibonacciNumbers.push(0);

    } else if (numItems === 2) {
        fibonacciNumbers.push(0, 1);

    } else {
        fibonacciNumbers.push(0, 1);

        for (let count = 2; count < numItems; count++) {
            const lastItem = fibonacciNumbers[fibonacciNumbers.length - 1];
            const beforeLastItem = fibonacciNumbers[fibonacciNumbers.length - 2];
            const nextItem = lastItem + beforeLastItem;
            fibonacciNumbers.push(nextItem);
        }
    }

    console.log(fibonacciNumbers);
}

fibonacciGenerator();