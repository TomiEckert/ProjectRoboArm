class Argv {
    constructor () {
        const ArgumentParser = require('argparse').ArgumentParser;

        const parser = new ArgumentParser({
            version: '1.0.0',
            addHelp: true,
            description: 'This is a simple wrapper for brain.js.'
        });

        var subparser = parser.addSubparsers(
            {
                title: "Methods",
                dest: "Method",
            }
        );
        
        var train = subparser.addParser('train', { addHelp: true, description: 'Trains the selected model.' })
        var load = train.addMutuallyExclusiveGroup({required: true});
        load.addArgument(
            ['-n', '--name'],
            {
                help: 'Load an existing MODEL.',
                metavar: 'NAME'
            }
        );
        load.addArgument(
            ['-c', '--create'],
            {
                help: 'Create NEW model',
                metavar: 'NAME'
            }
        );
        train.addArgument(
            ['-l', '--layers'],
            {
                help: 'Sets the LAYERS for model creation. Format: "[3, 2]"',
                defaultValue: [3]
            }
        );
        train.addArgument(
            'DATA',
            {
                help: 'Path to the training DATA.'
            }
        );
        train.addArgument(
            ['-i', '--iterations'],
            {
                help: 'Number of INTERATIONS. Default: 250000',
                defaultValue: 250000
            }
        );
        train.addArgument(
            ['-t', '--timelimit'],
            {
                help: 'TIMELIMIT for training in milliseconds. Default: 300000',
                defaultValue: 300000
            }
        );
        train.addArgument(
            ['-e', '--error'],
            {
                help: "ERROR threshold. Default: 0.001",
                defaultValue: 0.001
            }
        );

        var run = subparser.addParser('run', { addHelp: true, description: 'Runs the model on the specified data.' });
        run.addArgument(
            'MODEL',
            {
                help: "Name of the MODEL."
            }
        );
        run.addArgument(
            ['-e', '--exported'],
            {
                nargs: 0,
                help: 'Searches for an exported version of the MODEL.'
            }
        );
        run.addArgument(
            'DATA',
            {
                help: "Path to the DATA file, or raw json encoded DATA."
            }
        );
        run.addArgument(
            ['-f', '--formatted'],
            {
                nargs: 0,
                help: "Formats the output to human-readable format."
            }
        );


        this.args = parser.parseArgs();
        return this.args;
    }
}

module.exports = Argv;