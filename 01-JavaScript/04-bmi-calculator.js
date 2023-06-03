const prompt = require("prompt-sync")({ sigint: true });

const yourWeight = prompt("What is your weight? (e.g.: 65) ");
const yourHeight = prompt("What is your height? (e.g.:1.8) ");

function bmiCalculator(weight, height) {

    const givenWeight = parseInt(weight);
    const givenHeight = parseFloat(height);

    const bmi = Math.round(givenWeight / givenHeight ** 2);

    const yourBMI = "Your BMI is ";

    if (bmi < 18.5) {
        console.log(yourBMI + bmi + ", so you are underweight.");
    }
    if (bmi > 18.5 && bmi < 24.9) {
        console.log(yourBMI + bmi + ", so you have a normal weight.");
    }
    if (bmi > 24.9) {
        console.log(yourBMI + bmi + ", so you are overweight.");
    }

}

bmiCalculator(yourWeight, yourHeight);