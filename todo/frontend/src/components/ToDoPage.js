import React from 'react'
import {useParams} from 'react-router-dom'


const ToDoItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.project}</td>
            <td>{todo.text}</td>
            <td>{todo.user}</td>
        </tr>
    )
}


const ToDoPageList = ({todos}) => {

    let { id } = useParams();
    let filtered_todos = todos.filter((todo) => todo.id == id)
    return (
        <table>
            <tr>
                <th>Project</th>
                <th>Text</th>
                <th>User</th>
            </tr>
            {filtered_todos.map((todo) => <ToDoItem todo={todo} />)}
        </table>
    )
}

export default ToDoPageList;
