# Setting up RoboBrain

## Requirements

- [Node.js](https://nodejs.org/en/) (12.10 or lower)
- [NPM](https://www.npmjs.com/) (5.5.1 or higher)
- [Brain.js](https://brain.js.org/)
- [argparse](https://www.npmjs.com/package/argparse)

## Setup
---
1. You need [Node.js](https://nodejs.org/en/) (12.10 or lower)<sup>[1](#Notes)</sup>, you might need to download [NPM](https://www.npmjs.com/) (5.5.1 or higher) sperately, this is the Node.js package manager.

> _Note: You **need** to downgrade your Node.js installation if you are using the official Windows installer. [NVM](https://github.com/coreybutler/nvm-windows) will help with that._
---
2. Clone this branch into the folder where you want to put you neural network.
---
3. Now you need to download [Brain.js](https://brain.js.org/) and [argparse](https://www.npmjs.com/package/argparse).
    - Open cmd and type in: `cd <path>`. Replace `<path>` with the path to your folder.
    - Once you're inside the folder, type: `npm install brain.js` (might need to use `sudo` on linux).
    - Repeat the step above but with this command: `npm install argparse`.
---
4. Run the test with `node test.js`

## Basics

There are 2 types of models in the framework:
- **Normal** - can be trained, but it is slow to open.
- **Exported** - cannot be trained anymore, but super quick.

> _Notes: check out **test.js** and **load.js** to see how the code works._

## Notes
1. Node.js version above 12.10 have problems with the `require(module)` command.