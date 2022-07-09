require("dotenv").config();
const express = require("express");
const cors = require("cors");
const app = express();
const pool = require("./db");

//route
app.use(cors());
app.use(express.json());

app.get("/players", async (req, res) => {
  try {
    const { position } = req.query;
    const players = await pool.query(
      "SELECT * FROM draftedplayers WHERE position = $1" +
        "ORDER BY value_for_draft_team DESC",
      [position]
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
