import React from "react"
import {Link} from "react-router-dom";


const ProjectItem = ({project, deleteProject}) => {
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
            <td>
                <button onClick={() => deleteProject(project.id)}>
                    Delete
                </button>
            </td>

        </tr>
    )
}


const ProjectsList = ({projects, deleteProject}) => {
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
            <th>

            </th>
            {projects.map((project) => <ProjectItem project={project}
                                                    deleteProject={deleteProject}/>)}
        </table>
    )
}


export default ProjectsList;
