import React, { useState } from 'react';
import { Redirect } from 'react-router-dom';
import { signUp } from '../../../services/auth';
import { useModalAndAuthContext } from '../../../context/ModalAndAuth';

function SignUpFormPage() {
  const { authenticated, setAuthenticated } = useModalAndAuthContext();
  const [errors, setErrors] = useState([]);
  const [username, setUsername] = useState('');
  const [city, setCity] = useState('');
  const [stateAbbr, setStateAbbr] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const user = await signUp(username, email, city, stateAbbr, password);
      if (!user.errors) {
        setAuthenticated(true);
        } else {
          setErrors(user.errors);
      }
    }
    // else{
    //   setErrors(errors.password = "Password fields must match")
    // }
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };
  
  const updateEmail = (e) => {
    setEmail(e.target.value);
  };
  
  const updateCity = (e) => {
    setCity(e.target.value);
  };
  
  const updateStateAbbr = (e) => {
    setStateAbbr(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (authenticated) {
    return <Redirect to='/' />;
  }

  return (
    <form onSubmit={onSignUp}>
      <div>
        {errors.map((error) => (
          <div>{error}</div>
        ))}
      </div>
      <div>
        <label>User Name</label>
        <input
          type='text'
          name='username'
          onChange={updateUsername}
          value={username}
        ></input>
      </div>
      <div>
        <label>Email</label>
        <input
          type='text'
          name='email'
          onChange={updateEmail}
          value={email}
        ></input>
      </div>
      <div>
        <label>City</label>
        <input
          type='text'
          name='city'
          onChange={updateCity}
          value={city}
        ></input>
      </div>
      <div>
        <label>State Abbreviation</label>
        <input
          type='text'
          name='stateAbbr'
          onChange={updateStateAbbr}
          value={stateAbbr}
        ></input>
      </div>
      <div>
        <label>Password</label>
        <input
          type='password'
          name='password'
          onChange={updatePassword}
          value={password}
        ></input>
      </div>
      <div>
        <label>Repeat Password</label>
        <input
          type='password'
          name='repeat_password'
          onChange={updateRepeatPassword}
          value={repeatPassword}
          required={true}
        ></input>
      </div>
      <button type='submit'>Sign Up</button>
    </form>
  );
}

export default SignUpFormPage;
