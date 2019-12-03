class RoboBrain {

    constructor(generateNet, config) {
        console.log('Initializing framework...');
        this.brain = require("brain.js");
        if(typeof config === "undefined") {
            this.netConfig = {
                hiddenLayers: [2]
            }
        } else {
            this.netConfig = config;
        }

        this.trainConf = {
            iterations: 250000,
            errorThresh: 0.0005,
            learningRate: 0.2,
            momentum: 0.1,
            timeout: 300000,
        }

        if (generateNet != true) {
            return;
        }

        this.generate();
    }

    initialize() {
        this.net = new this.brain.NeuralNetwork(this.netConfig);
    }

    generate(config) {
        if(typeof config === "undefined") {
            config = this.netConfig;
        }
        process.stdout.write("Generating net [");
        process.stdout.write(config['hiddenLayers'].toString());
        console.log("]... ");
        this.net = new this.brain.NeuralNetwork(config);
    }

    train(data, config) {
        if(typeof config === "undefined") {
            config = this.trainConf;
        }
        process.stdout.write("Training net... ");
        var start = Date.now();
        const stats = this.net.train(data, config);
        var end = Date.now();
        var time = end - start;
        console.log("done: " + time + "ms");
        var acc = stats['error'] * 100000;
        console.log(" >  Accuracy: " + (100 - (Math.round(acc) / 1000)) + "%");
        console.log(" >  Iterations: " + stats['iterations'] + '\n');
        return stats;
    }

    trainQuick(data) {
        var config = {
            iterations: 10000,
            errorThresh: 0.05,
            learningRate: 0.3,
            momentum: 0.1,
            timeout: 10000,
        };
        return this.train(data, config);
    }

    formatResult(result) {
        console.log("Results:");
        Object.keys(result).forEach(function (key, index) {
            var out = result[key];
            var value = Math.round(out * 10000) / 10000;
            console.log(" >  " + key + ": " + value);
        });
        console.log();
    }

    static formatResult(result) {
        console.log("Results:");
        Object.keys(result).forEach(function (key, index) {
            var out = result[key];
            var value = Math.round(out * 10000) / 10000;
            console.log(" >  " + key + ": " + value);
        });
        console.log();
    }

    run(data) {
        var result = this.net.run(data);
        return result;
    }

    test(data, accuracy) {
        console.log("Testing...");
        if (accuracy == "undefined") { accuracy = 0.5; }

        var good = 0;
        var bad = 0;

        for (let i = 0; i < data.length; i++) {
            var result = this.net.run(data[i]['input']);
            var pass = true;
            Object.keys(result).forEach(function (key, index) {
                var out = result[key];
                var expected = data[i]['output'][key];

                if (typeof expected === "undefined") { expected = 0; }

                if (Math.abs(out - expected) > accuracy) {
                    pass = false;
                }
            });
            if (pass) {
                console.log(" >  " + (i + 1) + ". passed");
                good++;
            } else {
                console.log(" >  " + (i + 1) + ". failed");
                bad++;
            }
        }
        console.log(" ==>  passed: " + good);
        console.log(" ==>  failed: " + bad + '\n');
    }

    saveModel(name) {
        const fs = require('fs');
        const json = JSON.stringify(this.net.toJSON());
        fs.writeFileSync("./models/" + name + ".json", json);
    }

    exportModel(name) {
        const fs = require('fs');
        const func = this.net.toFunction();
        fs.writeFileSync("./models/" + name + ".js", func.toString() + '\nmodule.exports = anonymous;');
    }

    static importModel(name) {
        const anonymous = require('./models/' + name + '.js');
        return anonymous;
    }

    loadModel(name) {
        const fs = require('fs');
        var json = fs.readFileSync("./models/" + name + ".json");
        this.net.fromJSON(JSON.parse(json));
    }
}
module.exports = RoboBrain;