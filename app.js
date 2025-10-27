const express = require("express");
const app = express();
const path = require("path");
const mongoose = require("mongoose");
const userModel = require("./models/user");
const jwt = require("jsonwebtoken");
const cookieParser = require("cookie-parser");
require("./config/mongoose-connection");
const bcrypt = require("bcrypt");
const port = 3000;

require("dotenv").config();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public")));
app.use(cookieParser());
app.set("view engine", "ejs");

app.get("/", isLoggedin, (req, res) => {
  res.render("index", { msg: req.query.msg, page: req.query.page });
});

app.get("/dashboard", (req, res) => {
  res.render("dashboard");
});

app.post("/signup", async (req, res) => {
  const { username, email, password, confirmpass } = req.body;
  let user = await userModel.findOne({ email });
  if (user) {
    return res.redirect(`/?msg= account already exists&page=signup`);
  } else if (confirmpass !== password) {
    return res.redirect(
      `/?msg=confirm password didnot match the password&page=signup`
    );
  } else {
    bcrypt.genSalt(10, (err, salt) => {
      bcrypt.hash(password, salt, async (err, hash) => {
        let createdUser = await userModel.create({
          username,
          email,
          password: hash,
        });

        let token = jwt.sign(
          { email: email, userId: createdUser._id },
          process.env.JWT_SECRET
        );
        res.cookie("token", token);

        res.redirect("/dashboard");
      });
    });
  }
});

app.post("/login", async (req, res) => {
  const { email, password } = req.body;

  let user = await userModel.findOne({ email: email });
  if (!user)
    return res.redirect(
      `/?msg=this account is not registered please signup first`
    );
  else {
    bcrypt.compare(password, user.password, (err, result) => {
      if (result) {
        let token = jwt.sign(
          { email: email, userid: user._id },
          process.env.JWT_SECRET
        );
        res.cookie("token", token);
        res.redirect("/dashboard");
      } else {
        return res.redirect(`/?msg=email or password is incorrect`);
      }
    });
  }
});

app.get("/logout", (req, res) => {
  res.clearCookie("token");
  res.redirect("/");
});

app.listen(port, () => {
  console.log(`Server is running on port http://localhost:${port}`);
});

function isLoggedin(req, res, next) {
  let tok = req.cookies.token;

  if (!tok) return res.redirect("/");
  else {
    let data = jwt.verify(tok, process.env.JWT_SECRET);
    req.user = data;
    return res.redirect("/dashboard");
    next();
  }
}
