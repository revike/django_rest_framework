import React from 'react'
import {useParams} from 'react-router-dom'


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.name}</td>
            <td>{project.link}</td>
            <td>{project.users}</td>
        </tr>
    )
}


const ProjectPageList = ({projects}) => {

    let { id } = useParams();
    let filtered_projects = projects.filter((project) => project.id == id)
    return (
        <table>
            <tr>
                <th>Project</th>
                <th>Link</th>
                <th>Users</th>
            </tr>
            {filtered_projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectPageList;
