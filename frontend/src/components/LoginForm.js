import React, { useEffect, useRef, useState } from "react";
import { Redirect } from "react-router-dom";

const checkUrl = "http://localhost:3001";

export const LoginForm = ({ username, setUsername, password, setPassword }) => {
  const [submitted, setSubmitted] = useState(false);

  const userValue = useRef("");

  useEffect(() => {
    userValue.current.focus();
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const check = await fetch(checkUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
      },
      body:
        "username=" +
        username +
        "&password=" +
        password +
        "&grant_type=password",
    });

    if (check.status === 200) {
      setSubmitted(true);
      setUsername(username);
    }
  };

  if (submitted) {
    return <Redirect to="/users" />;
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="username">Username: </label>
      <br />
      <input
        type="text"
        onChange={(e) => setUsername(e.target.value)}
        ref={userValue}
      />
      <br />
      <label htmlFor="password">Password: </label>
      <br />
      <input type="password" onChange={(e) => setPassword(e.target.value)} />
      <br />
      <br />
      <input type="submit" value="Submit"></input>
    </form>
  );
};
