import React from 'react';
// import logo from './logo.svg';
import './App.css';
import axios from "axios";
import UserList from "./components/Users";
import Footer from "./components/Footer";
import Header from "./components/Header";
import ProjectsList from "./components/Project";
import TodoList from "./components/ToDo";
import {BrowserRouter, Route, Redirect, Switch} from 'react-router-dom';
import UserPageList from "./components/UserPage";
import ProjectPageList from "./components/ProjectPage";
import ToDoPageList from "./components/ToDoPage";


const notFount404 = ({location}) => {
    return (
        <div>
            Error 404: {location.pathname}
        </div>
    )
}


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
            <div class='content'>
                <BrowserRouter>
                    <Header/>
                    <Switch>
                        <Route exact path='/'
                               component={() => <UserList
                                   users={this.state.users}/>}/>
                        <Route exact path='/projects'
                               component={() => <ProjectsList
                                   projects={this.state.projects}/>}/>
                        <Route exact path='/todos'
                               component={() => <TodoList
                                   todos={this.state.todos}/>}/>

                        <Route exact path='/user/:id'> <UserPageList
                            users={this.state.users}/> </Route>
                        <Route exact path='/project/:id'> <ProjectPageList
                            projects={this.state.projects}/> </Route>
                        <Route exact path='/todo/:id'> <ToDoPageList
                            todos={this.state.todos}/> </Route>

                        <Redirect from='/users' to='/'/>
                        <Route component={notFount404}/>
                    </Switch>
                    <Footer/>
                </BrowserRouter>
            </div>
        )
    }
}


export default App;
