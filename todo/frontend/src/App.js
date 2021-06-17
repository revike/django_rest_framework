import React from 'react';
// import logo from './logo.svg';
import './App.css';
import axios from "axios";
import UserList from "./components/Users";
import Footer from "./components/Footer";
import Header from "./components/Header";
import ProjectsList from "./components/Project";
import TodoList from "./components/ToDo";
import {BrowserRouter, Route, Redirect, Switch, Link} from 'react-router-dom';
import UserPageList from "./components/UserPage";
import ProjectPageList from "./components/ProjectPage";
import ToDoPageList from "./components/ToDoPage";
import LoginForm from "./components/Auth";
import ProjectForm from "./components/ProjectForm";


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
            'todos': [],
            'token': ''
        }
    }

    create_header() {
        if (!this.is_auth()) return {};
        return {
            'Authorization': 'Token ' + this.state.token
        }
    }

    load_data() {
        let headers = this.create_header();
        axios.get('http://127.0.0.1:8000/api/v1/users/', {headers})
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => {
                this.setState(
                    {
                        'users': []
                    }
                )
            })

        axios.get('http://127.0.0.1:8000/api/v1/projects/', {headers})
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(errors => console.log(errors))

        axios.get('http://127.0.0.1:8000/api/v1/todo/', {headers})
            .then(response => {
                const todos = response.data
                this.setState(
                    {
                        'todos': todos
                    }
                )
            }).catch(errors => console.log(errors))
    }

    restore_token() {
        let token = localStorage.getItem('token');
        this.setState(
            {
                'token': token
            }, this.load_data
        );
    }

    componentDidMount() {
        this.restore_token();
    }

    is_auth() {
        return !!(this.state.token);
    }

    logout() {
        localStorage.removeItem('token')
        this.setState(
            {
                'token': ''
            }, this.load_data
        );
    }

    get_token(login, password) {
        axios.post(
            'http://127.0.0.1:8000/api-token-auth/',
            {"username": login, "password": password}
        )
            .then(response => {
                this.setState(
                    {
                        'token': response.data.token
                    }, this.load_data
                );
            })
            .catch(error => alert(error));
    }

    delete_project(id) {
        let headers = this.create_header();
        axios
            .delete(`http://127.0.0.1:8000/api/v1/projects/${id}/`, {headers})
            .then(response => {
                this.setState(
                    {
                        'projects': this.state.projects.filter((project) => project.id !== id)
                    }
                )
            })
            .catch(error => {
                console.log(error)
            })
    }

    create_project(name, users) {
        axios
            .post(
                `http://127.0.0.1:8000/api/v1/projects/`,
                {'name': name, 'users': users}
            )
            .then(response => {
                this.load_data();
            })
            .catch(error => alert(error))
    }

    render() {
        return (
            <div class='content'>
                <BrowserRouter>
                    <Header/>

                    <div className='auth'>
                        {
                            this.is_auth() ?
                                <button
                                    onClick={() => this.logout()}>
                                    Logout</button> :
                                <Link to='/login'>Login</Link>
                        }
                    </div>

                    <Switch>
                        <Route exact path='/'
                               component={() => <UserList
                                   users={this.state.users}/>}/>
                        <Route exact path='/projects'
                               component={() => <ProjectsList
                                   projects={this.state.projects}
                                   deleteProject={(id) => this.delete_project(id)}/>}/>
                        <Route exact path='/todos'
                               component={() => <TodoList
                                   todos={this.state.todos}/>}/>
                        <Route exact path='/login'
                               component={() => <LoginForm
                                   get_token={(username, password) => this.get_token(username, password)}/>}/>

                        <Route exact path='/projects/create'
                               component={() => <ProjectForm
                                   create_project={(name, users) => this.create_project(name, users)}
                                   users={this.state.users}/>}/>

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
