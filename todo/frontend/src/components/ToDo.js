import React from "react"


const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.date_creation}
            </td>
            <td>
                {todo.date_update}
            </td>
            <td>
                {todo.user}
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
