import React from "react";

interface NetWorkInfo {
    title: string;
    url: string;
    icons?: React.ReactElement;
}

const ButtonNetWork: React.FC<NetWorkInfo> = ({ title, url, icons }) => {
    return (
        <div>
            <a
                href={url} rel="noopener noreferrer" className="bg-[#7a7267] text-white font-bold py-2 px-20 rounded-full inline-flex items-center">
                {icons}{title}
            </a>
        </div>
    );
}

export default ButtonNetWork;
