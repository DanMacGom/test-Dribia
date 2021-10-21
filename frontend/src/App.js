import { UserList } from "./components/UserList";
import { LoginForm } from "./components/LoginForm";

import { useState } from "react";
import { Link, BrowserRouter, Route, Switch } from "react-router-dom";
import { LoginButton } from "./components/LoginButton";

const App = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/">
          <LoginForm
            username={username}
            setUsername={setUsername}
            password={password}
            setPassword={setPassword}
          />
        </Route>
        <Route exact path="/users">
          <UserList />
          <Link to="/">
            <LoginButton />
          </Link>
        </Route>
      </Switch>
    </BrowserRouter>
  );
};

export default App;
