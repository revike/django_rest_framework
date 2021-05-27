import React from "react"
import {Link} from "react-router-dom";


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                <Link to={`/project/${project.id}`}>{project.name}</Link>
            </td>

            <td>
                {project.link}
            </td>

            <td>
                {project.users}
            </td>

        </tr>
    )
}


const ProjectsList = ({projects}) => {
    return (
        <table>
            <th>
                Name
            </th>
            <th>
                Link
            </th>
            <th>
                Users
            </th>
            {projects.map((project) => <ProjectItem project={project} /> )}
        </table>
    )
}


export default ProjectsList;
