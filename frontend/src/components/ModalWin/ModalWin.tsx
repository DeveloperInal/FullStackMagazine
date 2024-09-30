import { postUserByCardData } from "../Slices/UserByProductSlice";
import React, { useState } from "react";
import { useAppDispatch } from "../../hooks/reduxHooks";

interface ModalWinProps {
    onClose: () => void;
    card_title: string;
    price: number;
    tg_user: string;
    promocode: string;
}

const ModalWin: React.FC<ModalWinProps> = ({ tg_user, onClose, card_title, price, promocode }) => {
    const [inputValue, setInputValue] = useState(tg_user);
    const [isClosing, setIsClosing] = useState(false);
    const dispatch = useAppDispatch();

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setInputValue(e.target.value);
    };

    const handlePayClick = () => {
        console.log(dispatch(postUserByCardData({
            tg_id: Number(inputValue),
            card_title,
            price,
            promocode
        })));

        handleClose();
    };

    const handleClose = () => {
        setIsClosing(true);
        setTimeout(() => {
            onClose();
        }, 300);
    };

    const handleOutsideClick = (e: React.MouseEvent<HTMLDivElement, MouseEvent>) => {
        const modalContent = document.getElementById("modal-content");
        if (modalContent && !modalContent.contains(e.target as Node)) {
            handleClose();
        }
    };

    return (
        <div
            className={`fixed inset-0 bg-gray-900 bg-opacity-50 flex justify-center items-center transition-opacity duration-300 ${isClosing ? 'opacity-0' : 'opacity-100'}`}
            onClick={handleOutsideClick}  // Close when clicking outside modal
        >
            <div
                id="modal-content"
                className={`bg-white p-6 rounded-lg shadow-lg max-w-md w-full transform transition-transform duration-300 ${isClosing ? 'scale-90 opacity-0' : 'scale-100 opacity-100'}`}
            >
                <h2 className="text-2xl font-bold mb-4 text-black">Введите ваш Telegram ID</h2>
                <input
                    type="text"
                    value={inputValue}
                    onChange={handleChange}
                    className="w-full p-2 border border-gray-300 rounded mb-4"
                    placeholder="Введите ваш Telegram ID"
                />
                <div className="flex justify-end">
                    <button
                        onClick={handlePayClick}
                        className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition"
                    >
                        Оплатить
                    </button>
                </div>
            </div>
        </div>
    );
};

export default ModalWin;
