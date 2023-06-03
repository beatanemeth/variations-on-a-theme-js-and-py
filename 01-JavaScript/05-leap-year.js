const prompt = require("prompt-sync")({ sigint: true });

const yourYear = prompt("Write a year and check if it is leap or not (e.g. 2010): ");

function isLeapYear(year) {
    const yearNum = parseInt(year);

    if (yearNum % 4 === 0) {
        if (yearNum % 100 === 0) {
            if (yearNum % 400 === 0) {
                return "Leap year.";
            } else {
                return "Not leap year.";
            }
        } else {
            return "Leap year.";
        }
    } else {
        return "Not leap year.";
    }
}

const leapOrNot = isLeapYear(yourYear);
console.log(leapOrNot);