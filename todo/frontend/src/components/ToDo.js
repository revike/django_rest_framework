import React from "react"
import {Link} from "react-router-dom";


const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>
                <Link to={`/project/${todo.project}`}>{todo.project}</Link>
            </td>
            <td>
                <Link to={`/todo/${todo.id}`}>{todo.text}</Link>
            </td>
            <td>
                {todo.date_creation}
            </td>
            <td>
                {todo.date_update}
            </td>
            <td>
                <Link to={`/user/${todo.user}`}>{todo.user}</Link>
            </td>
        </tr>
    )
}


const TodoList = ({todos}) => {
    return (
        <table>
            <th>
                Project
            </th>
            <th>
                Text
            </th>
            <th>
                Date Creation
            </th>
            <th>
                Date Update
            </th>
            <th>
                User
            </th>
            {todos.map((todo) => <TodoItem todo={todo}/>)}
        </table>
    )
}


export default TodoList;
