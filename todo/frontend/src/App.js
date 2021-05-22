import React from 'react';
// import logo from './logo.svg';
import './App.css';
import axios from "axios";
import UserList from "./components/Users";
import Footer from "./components/Footer";
import Header from "./components/Header";
import ProjectsList from "./components/Project";
import TodoList from "./components/ToDo";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'todos': []
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

        axios.get('http://127.0.0.1:8000/api/v1/projects/').then(response => {
            const projects = response.data
            this.setState(
                {
                    'projects': projects
                }
            )
        }).catch(errors => console.log(errors))

        axios.get('http://127.0.0.1:8000/api/v1/todo/').then(response => {
            const todos = response.data
            this.setState(
                {
                    'todos': todos
                }
            )
        }).catch(errors => console.log(errors))
    }

    render() {
        return (
            <div class='wrapper'>
                <Header/>
                <div class='content'>
                    <UserList users={this.state.users}/>
                    <ProjectsList projects={this.state.projects}/>
                    <TodoList todos={this.state.todos}/>
                </div>
                <Footer/>
            </div>
        )
    }
}


export default App;
