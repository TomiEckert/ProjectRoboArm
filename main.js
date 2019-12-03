const RoboBrain = require('./roboBrain.js');
const Argv = require('./argv.js');
const fs = require('fs');

parseArray = function (text) {
    try {
        return JSON.parse(text);
    } catch (error) {
        console.error(error);
    }
}
isPath = function (path) {
    if (fs.existsSync(path)) {
        try {
            return JSON.parse(fs.readFileSync(path));
        } catch (error) {
            return false;
        }
    }
    return false;
}
isValidJSON = function (json) {
    try {
        return JSON.parse(json);
    } catch (error) {
        return false;
    }
}

const args = new Argv();

switch (args['Method']) {
    case 'run':
        var rb = "";
        var ai = "";
        if(args['exported'] === null) {
            try {
                rb = new RoboBrain(true);
                rb.loadModel(args['MODEL']);
                ai = null;
            } catch (error) {
                console.error("MODEL not found");
                return false;
            }
        } else {
            ai = RoboBrain.importModel(args['MODEL']);
        }
        var data = isPath(args['DATA']);
        if (data === false) {
            data = isValidJSON(args['DATA']);
            if (data === false) {
                console.error("DATA is not a path nor raw input");
                return false;
            }
        }
        if (args['formatted'] !== null) {
            if(ai !== null) {
                RoboBrain.formatResult(ai(data));
            } else {
                RoboBrain.formatResult(rb.run(data));
            }
        } else {
            if(ai !== null) {
                console.log(ai(data));
            } else {
                console.log(rb.run(data));
            }
        }

        break;

    case 'train':
        var rb = new RoboBrain(false);
        rb.initialize();
        var fileName = "";
        if (args['name'] !== null) {
            try {
                rb.loadModel(args['name']);
                fileName = args['name'];
            } catch (error) {
                console.error("MODEL not found");
                return false;
            }
        } else {
            var name = args['create'];
            var config = {
                hiddenLayers: parseArray(args['layers'])
            }
            rb.generate(config);
            fileName = args['create'];
        }
        var data = isPath(args['DATA']);
        if (data === false) {
            data = isValidJSON(args['DATA']);
            if (data === false) {
                console.error("DATA is not a path nor raw input");
                return false;
            }
        }
        config = {
            iterations: parseInt(args['iterations']),
            errorThresh: parseFloat(args['error']),
            timeout: parseInt(args['timelimit'])
        };
        rb.train(data, config);
        rb.saveModel(fileName);
        rb.exportModel(fileName);
        break;
}