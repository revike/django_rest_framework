import React from 'react';
// import logo from './logo.svg';
import './App.css';
import UserList from "./Users";
import axios from "axios";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/v1/users/')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => console.log(error))
    }


    // render() {
    //     return (
    //         <div><UserList users={this.state.users}/></div>
    //     )
    // }

    render() {
        return (
            <div class='wrapper'>
                <div class='header'>
                    Header
                </div>
                <div class='content'>
                    <UserList users={this.state.users}/>
                </div>
                <div class='footer'>
                    Footer
                </div>
            </div>
        )
    }
}


export default App;
