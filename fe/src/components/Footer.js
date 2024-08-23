import React from "react";
import { SocialIcon } from 'react-social-icons'


export default function SiteFooter() {
    return (
        <footer>
            <div className='container'>
                <SocialIcon url="https://www.flickr.com/photos/chrisfleisch" />
                <SocialIcon url="https://www.linkedin.com/in/chris-fleisch" />
                <SocialIcon url="https://github.com/chrisfleisch" />
            </div>
        </footer>
    );
}
