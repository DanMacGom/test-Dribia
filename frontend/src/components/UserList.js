import { useData } from "../hooks/useData";

export const UserList = () => {
  const userData = useData();

  return (
    <ul>
      {userData.map((user, idx) => (
        <li key={idx}>
          {user.username}, {user.creation_date}
        </li>
      ))}
    </ul>
  );
};
