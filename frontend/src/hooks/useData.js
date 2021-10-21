import { useState, useEffect } from "react";

const userUrl = "/users";

export const useData = () => {
  const [userData, setUserData] = useState([]);

  const getData = async () => {
    const jsonData = await fetch(userUrl);
    const data = await jsonData.json();

    return setUserData(data);
  };

  useEffect(() => {
    getData();
  }, []);

  return userData;
};
