// Prompt: Analyze the code, find weaknesses or gaps (security, structure, readability), then rewrite an improved version.
const express = require("express");
const helmet = require("helmet");

const app = express();

// Add security headers
app.use(helmet());

/**
 * Root endpoint.
 * Responds with a greeting.
 */
app.get("/", (req, res) => {
  res.send("Hello World!");
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, (err) => {
  if (err) {
    console.error("Server failed to start:", err);
    process.exit(1);
  }
  console.log(`Example app listening on port ${PORT}!`);
});
