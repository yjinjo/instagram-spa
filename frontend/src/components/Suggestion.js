import React from "react";
import { Avatar, Button } from "antd";
import { UserOutlined } from "@ant-design/icons";
import "./Suggestion.scss";

function Suggestion({ suggestionUser }) {
  const { username, name, avatar_url } = suggestionUser;

  return (
    <div className="suggestion">
      <div className="avatar">
        <Avatar
          size="small"
          icon={
            <img
              src={"http://localhost:8000" + avatar_url}
              alt={`${username}'s avatar`}
            />
          }
        />
        {/*<UserOutlined />*/}
      </div>
      <div className="username">{name.length === 0 ? username : name}</div>
      <div className="action">
        <Button size="small">Follow</Button>
      </div>
    </div>
  );
}

export default Suggestion;
