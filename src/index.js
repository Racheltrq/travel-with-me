import React from 'react';
import ReactDOM from 'react-dom/client';
import { AmplifyProvider } from '@aws-amplify/ui-react'
import { studioTheme } from './ui-components'
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { HeroLayout1 } from './ui-components';
import {
  BrowserRouter,
  Route,
  Routes
  //Switch,
  //Link
} from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <AmplifyProvider theme={studioTheme}>
    <BrowserRouter>
      <div>
        <Routes>
          <Route exact path="/" element={<HeroLayout1 />}/>
          <Route path="/feed" element={<App />}/>
        </Routes>
      </div>
    </BrowserRouter>
    </AmplifyProvider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
