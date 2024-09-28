import React from "react";

interface NetWorkInfo {
    title: string;
    url: string;
    icons?: React.ReactElement;
}

const ButtonNetWork: React.FC<NetWorkInfo> = ({ title, url, icons }) => {
    const handleClick = () => {
        window.location.href = url; // Переход по указанному URL
    };

    return (
        <div>
            <button
                className='relative py-2 px-8 text-black text-base font-bold nded-full overflow-hidden bg-green-700 rounded-full transition-all duration-400 ease-in-out shadow-md hover:scale-105 hover:text-white hover:shadow-lg active:scale-90 before:absolute before:top-0 before:-left-full before:w-full before:h-full before:bg-gradient-to-r before:from-blue-500 before:to-blue-300 before:transition-all before:duration-500 before:ease-in-out before:z-[-1] before:rounded-full hover:before:left-0'
                onClick={handleClick}>
                {icons}{title}
            </button>
        </div>
    );
}

export default ButtonNetWork;
