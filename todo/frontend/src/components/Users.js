import React from "react";
import {Link} from "react-router-dom";


const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                <Link to={`/user/${user.id}`}>{user.user_name}</Link>
            </td>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}


const UserList = ({users}) => {
    return (
        <table>
            <th>
                User name
            </th>
            <th>
                First name
            </th>
            <th>
                Last name
            </th>
            <th>
                E-mail
            </th>
            {users.map((user) => <UserItem user={user} />)}
        </table>
    )
}


export default UserList;
