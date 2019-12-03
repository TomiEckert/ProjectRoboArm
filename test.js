// imports magic library
const RoboBrain = require('./roboBrain.js');
const fs = require('fs');

createDataSet = function () {
    console.log("Generating data...");

    // input and output can be either an array of ints between 0 and 1
    // or a map of ints between 0 and 1
    // example:
    /*
            // map
            const dataSet = [
                {input: { x: 0.1, y: 0.5 }, output: 0.6},
                {input: { x: 0.8, y: 0.4 }, output: 1.2}
            ];
    
            or
    
            // array
            const dataSet = [
                {input: [0.1, 0.5], output: 0.6},
                {input: [0.8, 0.4], output: 1.2}
            ];
    */

    // inputs for the dataset
    const inputs = [
        { x: 0, y: 0 },
        { x: 1, y: 0 },
        { x: 0, y: 1 },
        { x: 1, y: 1 },

        { x: 0.3, y: 0 },
        { x: 0, y: 0.5 },
        { x: 0.7, y: 0 },
        { x: 0, y: 0.1 },

        { x: -1, y: 0 },
        { x: -0.4, y: 0 },
        { x: 0, y: -1 },
        { x: 0, y: -0.3 },

        { x: -0.8, y: 0.3 },
        { x: -0.2, y: -0.5 },
        { x: 0.5, y: -0.4 },
        { x: 0.1, y: -0.8 },
    ];

    // expected outputs for the dataset
    const outputs = [
        { left: 0 },
        { right: 1 },
        { up: 1 },
        { right: 1, up: 1 },

        { right: 1 },
        { up: 1 },
        { right: 1 },
        { up: 1 },

        { left: 1 },
        { left: 1 },
        { down: 1 },
        { down: 1 },

        { left: 1, up: 1 },
        { down: 1, left: 1 },
        { right: 1, down: 1 },
        { down: 1, right: 1 },
    ];

    const trainingData = [];

    // merges the two datasets into one
    for (let i = 0; i < inputs.length; i++) {
        trainingData.push({
            input: inputs[i],
            output: outputs[i]
        });
    }

    var json = JSON.stringify(trainingData);
    fs.writeFileSync('dataSet.json', json);

    return trainingData;
}

// loads dataset
const trainingData = JSON.parse(fs.readFileSync('./dataSet.json'));

// initiates the brain (takes time), with [3, 2] hidden layers
const rb = new RoboBrain(true, { hiddenLayers: [3, 2] });

// starts training the AI
rb.train(trainingData);

// exports model for faster use
rb.exportModel('test');

// ================================================================

// runs the current AI on the coordinates: (-0.2 : 0.6)
var result = rb.run(
    {x: -0.2, y: 0.6}
);

// prints the output of the AI
rb.formatResult(result);

// tests the AI on the whole training dataset
rb.test([{
    input: { x: -0.2, y: 0.6 }, output: { left: 1, up: 1 }
}]);