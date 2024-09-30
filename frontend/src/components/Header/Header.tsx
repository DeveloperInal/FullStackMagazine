import React from "react";

interface HeaderProps {
    logo_url: string;
    shop_name: string;
    page_name: string;
}

const Header: React.FC<HeaderProps> = ({ logo_url, shop_name, page_name }) => {
    return (
        <header className="flex justify-between items-center p-6 bg-customBlack text-white relative">
            <div className="flex items-center absolute left-6">
                <img
                    src={logo_url}
                    alt={shop_name}
                    className="w-12 h-12 rounded-full bg-white mr-3"
                />
                <span className="text-xl font-bold">{shop_name}</span>
            </div>

            <div className="absolute items-center">
                <div className="text-2xl bg-[#7a7267] text-white py-2 px-16 rounded-3xl">
                    {page_name}
                </div>
            </div>
            <div className="absolute w-full bottom-0 h-0.5 bg-gray-300 top-16" />
        </header>
    );
};

export default Header;
