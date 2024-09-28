import { postUserByCardData } from "../Slices/UserByProductSlice.ts";
import React, {useState} from "react";
import { useAppDispatch } from "../../hooks/reduxHooks.ts";

interface ModalWinProps {
    onClose: () => void;
    card_title: string;
    tg_user: string;
}

const ModalWin: React.FC<ModalWinProps> = ({ tg_user, onClose, card_title }) => {
    const [inputValue, setInputValue] = useState(tg_user);
    const dispatch = useAppDispatch();

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setInputValue(e.target.value);
    };

    const handlePayClick = () => {
        const by_product_date = new Date().toISOString();
        dispatch(postUserByCardData({
            tg_id: Number(inputValue),
            card_title,
            by_product_date
        }));

        onClose();
    };

    return (
        <div className="fixed inset-0 bg-gray-900 bg-opacity-50 flex justify-center items-center">
            <div className="bg-white p-6 rounded-lg shadow-lg max-w-md w-full">
                <h2 className="text-2xl font-bold mb-4">Введите tg_user</h2>
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