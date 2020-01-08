import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
const path = require('path');
import 'bootstrap/dist/css/bootstrap.min.css';
import { JobContextProvider } from "./contexts/JobContext";
import { CandidatesContextProvider } from "./contexts/CandidatesContext";
import "./index.css";

ReactDOM.render(
    <CandidatesContextProvider>
        <JobContextProvider>
            <App />
        </JobContextProvider>
    </CandidatesContextProvider>, document.getElementById('app'));
