import { UserList } from "./components/UserList";
import { LoginForm } from "./components/LoginForm";

import { useState } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";

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
        </Route>
      </Switch>
    </BrowserRouter>
  );
};

export default App;
