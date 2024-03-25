const Ajv = require("ajv");
const ajv = new Ajv({ allErrors: true });
require("ajv-formats")(ajv);

const schema = require("./schema.json"); // Adjust the path as necessary

// Example JSON data to validate
const data = require("./systems.json");

const validate = ajv.compile(schema);
const valid = validate(data);

if (!valid) {
  console.error(validate.errors);
  process.exit(1);
} else {
  console.log("JSON is valid.");
}
