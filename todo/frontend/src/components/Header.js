import React from "react";
import {Link} from "react-router-dom";


const Header = () => {
    return (
        <div className='header'>
            <nav>
                <ul>
                    <li>
                        <Link to='/'> Users </Link>
                    </li>
                    <li>
                        <Link to='/todos'> ToDo </Link>
                    </li>
                    <li>
                        <Link to='/projects'> Projects </Link>
                    </li>
                </ul>
            </nav>
        </div>
    )
}


export default Header;
