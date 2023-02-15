import React from "react";
import PostNewForm from "../components/PostNewForm";
import "../components/PostNew.scss";
import { Card } from "antd";

function PostNew() {
  return (
    <div className="PostNew">
      <Card title="새 포스팅 쓰기">
        <PostNewForm />
      </Card>
    </div>
  );
}

export default PostNew;
