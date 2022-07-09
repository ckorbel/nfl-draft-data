const Pool = require("pg").Pool;

const pool = new Pool({
  user: "postgres",
  password: process.env.PORT.DB_PASSWORD,
  host: "localhost",
  port: 5432,
  database: "draft-data",
});

module.exports = pool;
