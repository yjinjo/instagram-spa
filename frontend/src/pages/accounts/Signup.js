import React, { useEffect, useState } from "react";
import Axios from "axios";
import { Alert } from "antd";
import { useHistory } from "react-router-dom/cjs/react-router-dom";

function Signup() {
  const history = useHistory();
  const [inputs, setInputs] = useState({ username: "", password: "" });
  const [loading, setLoading] = useState(false);
  const [errors, setErrors] = useState({});
  const [formDisabled, setFormDisabled] = useState(true);
  // const [username, setUsername] = useState("");
  // const [password, setPassword] = useState("");

  const onSubmit = (e) => {
    e.preventDefault();

    setLoading(true);
    setErrors({});

    Axios.post("http://localhost:8000/accounts/signup/", inputs)
      .then((response) => {
        console.log("response: ", response);
        history.push("/accounts/login");
      })
      .catch((error) => {
        console.log("error: ", error);
        if (error.response) {
          setErrors({
            username: (error.response.data.username || []).join(" "),
            password: (error.response.data.password || []).join(" "),
          });
        }
      })
      .finally(() => {
        setLoading(false);
      });
  };

  useEffect(() => {
    const isEnabled = Object.values(inputs).every((s) => s.length > 0);
    setFormDisabled(!isEnabled);
  }, [inputs]);

  const onChange = (e) => {
    const { name, value } = e.target;
    setInputs((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  return (
    <div>
      <form onSubmit={onSubmit}>
        <div>
          <input type="text" name="username" onChange={onChange} />
          {errors.username && <Alert type="error" message={errors.username} />}
        </div>
        <div>
          <input type="password" name="password" onChange={onChange} />
          {errors.password && <Alert type="error" message={errors.password} />}
        </div>
        <input
          type="submit"
          value="회원가입"
          disabled={loading || formDisabled}
        />
      </form>
    </div>
  );
}

export default Signup;
