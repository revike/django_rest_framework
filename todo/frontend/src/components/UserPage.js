import React from 'react'
import {useParams} from 'react-router-dom'


const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.id}</td>
            <td>{user.user_name}</td>
            <td>{user.email}</td>
        </tr>
    )
}


const UserPageList = ({users}) => {

    let { id } = useParams();
    let filtered_users = users.filter((user) => user.id == id)
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>E-MAIL</th>
            </tr>
            {filtered_users.map((user) => <UserItem user={user} />)}
        </table>
    )
}

export default UserPageList;
