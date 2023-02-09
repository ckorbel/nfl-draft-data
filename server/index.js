require("dotenv").config();
const express = require("express");
const cors = require("cors");
const app = express();
const pool = require("./db");

//route
app.use(cors());
app.use(express.json());

// Fetch all player basically the whole DB
app.get("/players", async (req, res) => {
  try {
    const players = await pool.query(
      "SELECT * FROM draftedplayers ORDER BY draft_year DESC"
    );
    console.log({ players });
    return res.json(players.rows);
  } catch (err) {
    console.error(err.message);
  }
});

app.get("/teams", async (req, res) => {
  try {
    const { team } = req.query;
    const players = await pool.query(
      "SELECT * FROM draftedplayers" +
        "WHERE original_team = $1" +
        "ORDER BY draft_year DESC",
      [team]
    );
    return res.json(players.rows);
  } catch (err) {
    console.error(err.message);
  }
});

const PORT = process.env.PORT || 4000;

app.listen(PORT, () => {
  console.log(`server started on port ${PORT}`);
});
