import React, { useState } from 'react';
import ModalWin from "../ModalWin/ModalWin.tsx";

interface ProductCardProps {
    card_title: string;
    price: number;
    imageUrl: string; // Add imageUrl prop
}

const ProductCard: React.FC<ProductCardProps> = ({ card_title, price, imageUrl }) => {
    const [isModalOpen, setModalOpen] = useState(false);
    const [isAnimating, setIsAnimating] = useState(false);

    const handleCardClick = () => {
        setIsAnimating(true);
        setTimeout(() => {
            setModalOpen(true);
            setIsAnimating(false);
        }, 300);
    };

    const handleCloseModal = () => {
        setModalOpen(false);
    };

    return (
        <>
            <div
                className={`w-80 h-56 px-3 py-8 rounded-2xl gap-0.5 overflow-hidden shadow-lg m-2 bg-[#6E675B] cursor-pointer transition-transform duration-300 ${isAnimating ? 'transform scale-105' : ''}`}
                onClick={handleCardClick}
            >
                <img
                    src={imageUrl}
                    alt={card_title}
                    className="object-cover rounded-t-2xl" // Image styling
                />
                <div className="px-6 py-4">
                    <div className="font-bold mb-2 text-white text-4xl relative top-3">{card_title}</div>
                </div>
                <div className="px-6 pt-4 pb-2 text-start">
                    <div className="ml-0 w-28 p-3 bg-[#9E927E] rounded-2xl relative top-0.5">
                        <span className="text-white font-bold text-3xl">{price}₽</span>
                    </div>
                </div>
            </div>

            {isModalOpen && (
                <ModalWin tg_user="" onClose={handleCloseModal} card_title={card_title} price={price} promocode="" />
            )}
        </>
    );
};

export default ProductCard;

