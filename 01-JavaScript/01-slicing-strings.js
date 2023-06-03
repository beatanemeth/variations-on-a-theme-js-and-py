const prompt = require("prompt-sync")({ sigint: true });

const myTweet = prompt("Compose your tweet (a longer one, more then 100 characters): ");

const myTweetLength = myTweet.length;

if (myTweetLength < 140) {
    console.log("You have written " + myTweetLength + " characters, you have " + (140 - myTweet.length) + " characters remaining.\n");

} else {
    console.log("You have written " + myTweetLength + " characters, you have exceeded the limit with " + Math.abs(140 - myTweet.length) + " characters.\n");
}

const myTweetSliced = myTweet.slice(0, 140);
console.log("Your sliced tweet (only 100 characters): \n" + myTweetSliced)