#!/usr/bin/env node
'use strict';

var fs = require('fs');

var script = {
  config: {
    target: '',
    phases: {
      duration: 20,
      arrivalRate: 10
    }
  },
  scenarios: [{
    name: 'My recorded scenario',
    flow: [
    ]
  }]
};

var lines = fs.readFileSync(process.argv[2], 'utf8').split('\n');
lines.forEach(function(line) {
  var rs;
  if (line.length === 0) {
    return;
  }
  try {
    rs = JSON.parse(line);
  } catch(e) {
    console.error(e);
    return;
  }
  script.scenarios[0].flow.push(rs);
});

console.log(JSON.stringify(script, null, 2));
