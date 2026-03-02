// your code goes here
// WARNING
// THIS IS FOR EDUCATIONAL PURPOSES ONLY
// I AM NOT RESPONSIBLE FOR HOW YOU USE THIS
// ver 1.2 (JavaScript port)
// normal file
// im warning you, dont delete random shit

const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// -----------------------------
// ASCII BANNER
// -----------------------------
console.log(`
     _                                          _    _ 
  __| | ___ _ __ ___   ___   ___ _ __ __ _  ___| | _| |
 / _\` |/ _ \\ '_ \` _ \\ / _ \\ / __| '__/ _\` |/ __| |/ / |
| (_| |  __/ | | | | | (_) | (__| | | (_| | (__|   <|_|
 \\__,_|\\___|_| |_| |_|\\___/ \\___|_|  \\__,_|\\___|_|\\_(_)
`);

// -----------------------------
// CONFIG
// -----------------------------
const CHARACTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
const MIN_LENGTH = 1;
const MAX_LENGTH = 10;
const PROGRESS_INTERVAL = 10000000;

let amtnotit = 0;
let actualPassword = '';
let actualArray = [];

// -----------------------------
// 0. Choose password source
// -----------------------------
console.log("Choose password source:\n1 - Use pass.txt\n2 - Type password manually");

rl.question("Enter 1 or 2: ", (choice) => {
    if (choice === "1") {
        try {
            const data = fs.readFileSync('pass.txt', 'utf8');
            actualPassword = data.split('\n')[0].trim();
            actualArray = actualPassword.split('');
            startBruteforce();
        } catch (err) {
            console.log("ERROR: You chose pass.txt but it DOES NOT EXIST.\nLoad the file or choose option 2 next time.");
            rl.close();
            process.exit(1);
        }
    } else if (choice === "2") {
        rl.question("Type the password to brute-force: ", (password) => {
            actualPassword = password.trim();
            actualArray = actualPassword.split('');
            startBruteforce();
        });
    } else {
        console.log("Invalid choice. Exiting.");
        rl.close();
        process.exit(1);
    }
});

// -----------------------------
// Generator function to mimic itertools.product
// -----------------------------
function* product(chars, repeat) {
    const indices = new Array(repeat).fill(0);
    const charsArray = chars.split('');
    const total = Math.pow(charsArray.length, repeat);
    
    for (let i = 0; i < total; i++) {
        const result = new Array(repeat);
        let temp = i;
        
        for (let pos = repeat - 1; pos >= 0; pos--) {
            result[pos] = charsArray[temp % charsArray.length];
            temp = Math.floor(temp / charsArray.length);
        }
        
        yield result;
        
        if (i % PROGRESS_INTERVAL === 0 && i > 0) {
            console.log(`Generated ${i} combinations for length ${repeat}...`);
        }
    }
}

// -----------------------------
// Main brute-force function
// -----------------------------
function startBruteforce() {
    console.log("Starting by trying common passes...");

    // -----------------------------
    // 1. Check common passwords first
    // -----------------------------
    try {
        const commonsData = fs.readFileSync('commons.txt', 'utf8');
        const commonPasswords = commonsData.split('\n').map(line => line.trim());
        
        for (const guess of commonPasswords) {
            amtnotit++;
            
            if (guess === actualPassword) {
                console.log(`Got it from commons! Password is: ${guess}\nTook ${amtnotit} tries!`);
                rl.close();
                return;
            }
            
            if (amtnotit % PROGRESS_INTERVAL === 0) {
                console.log(`Tried ${amtnotit} guesses so far...`);
            }
        }
    } catch (err) {
        console.log("commons.txt not found, skipping common password check.");
    }

    // -----------------------------
    // 2. Brute-force
    // -----------------------------
    console.log("Wasn't in common passes we had...\nStarting brute forcing...");

    let found = false;

    for (let length = MIN_LENGTH; length <= MAX_LENGTH; length++) {
        const generator = product(CHARACTERS, length);
        
        for (const guessArray of generator) {
            amtnotit++;
            
            // Compare arrays
            if (arraysEqual(guessArray, actualArray)) {
                console.log(`Got it! Password is: ${guessArray.join('')}\nTook ${amtnotit} tries!`);
                found = true;
                break;
            }
            
            if (amtnotit % PROGRESS_INTERVAL === 0) {
                console.log(`Tried ${amtnotit} guesses so far...`);
            }
        }
        
        if (found) break;
    }

    if (!found) {
        console.log("\nPassword was not found in the brute-force search space.\nMaybe it's too long, contains numbers, symbols, or uses unsupported characters.\nPerhaps read the instructions next time?");
    }

    rl.close();
}

// -----------------------------
// Helper function to compare arrays
// -----------------------------
function arraysEqual(arr1, arr2) {
    if (arr1.length !== arr2.length) return false;
    for (let i = 0; i < arr1.length; i++) {
        if (arr1[i] !== arr2[i]) return false;
    }
    return true;
}

// Reminder:
// You can remove amtnotit and the progress check entirely for slightly better speed,
// but you won't see progress updates.