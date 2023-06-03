let count = 5;
let bottle;
let bottleDown;

while (count > 0) {

    if (count === 1) {
        bottle = bottleDown = "bottle";
    } else if (count === 2) {
        bottle = "bottles";
        bottleDown = "bottle";
    } else {
        bottle = bottleDown = "bottles";
    }

    console.log(`${count} ${bottle} of beer on the wall, ${count} ${bottle} of beer.\n Take one down and pass it around, ${count - 1} ${bottleDown} of beer on the wall.\n`)

    count--;
}