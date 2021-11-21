// Requirements...
require("dotenv").config();
const { PythonShell } = require("python-shell");

console.log("run content_generator");
PythonShell.run(
  "./content_generator",
  { pythonOptions: ["-u", "-m"], env: process.env },
  function (err) {
    if (err) throw err;
    console.log("content_generator complete");
  }
);
