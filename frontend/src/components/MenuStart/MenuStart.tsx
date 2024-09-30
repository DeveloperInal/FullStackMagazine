import ProductList from "../Card/ProductList";
import Header from "../Header/Header.tsx";
import ButtonNetWork from "../ButtonNetWork/ButtonNetWork";
import { FaTelegram } from "react-icons/fa";

const MenuStart = () => {
    return (
        <div className="text-center text-white text-2xl bg-customBlack min-h-screen px-4 py-4">
            <Header logo_url="./magazin_diadyshki.jpg" shop_name='Магазин дядюшки' page_name='Home' />

            <div className="mt-8">
                <h1 className="text-6xl font-bold mb-4 h-20">Добро Пожаловать</h1>
                <h2 className="text-4xl mb-4 h-16">Наши Контакты</h2>
                <div className="flex flex-col md:flex-row items-center justify-center space-y-2 md:space-y-0 md:space-x-4">
                    <ButtonNetWork title="Бот" url="https://t.me/tysbo_prog" icons={<FaTelegram />} />
                    <ButtonNetWork title="Канал" url="https://t.me/tysbo_prog" icons={<FaTelegram />} />
                </div>
            </div>

            <div className="mt-8">
                <h2 className="text-4xl font-bold mb-4 h-10">Топ Предложений</h2>
                <ProductList />
            </div>
        </div>
    );
};

export default MenuStart;
