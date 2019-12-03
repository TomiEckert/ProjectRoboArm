// we don't initialize the brain here
// and it's much faster
const rb = require('./roboBrain.js');

// static function, also superfast
const ai = rb.importModel('test');

var result = ai({x: -0.2, y: 0.3});
rb.formatResult(result);
var result = ai({x: -0.6, y: -0.9});
rb.formatResult(result);
var result = ai({x: 0.9, y: -0.1});
rb.formatResult(result);
var result = ai({x: -0.1, y: 0.5});
rb.formatResult(result);
var result = ai({x: 0.4, y: 0.8});
rb.formatResult(result);
var result = ai({x: -0.6, y: -0.6});
rb.formatResult(result);
var result = ai({x: 0.3, y: -0.2});
rb.formatResult(result);
var result = ai({x: -0.7, y: 0.3});
rb.formatResult(result);