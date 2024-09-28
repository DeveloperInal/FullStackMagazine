import ProductList from "../Card/ProductList.tsx";
import ButtonNetWork from "../ButtonNetWork/ButtonNetWork.tsx";
import { FaTelegram } from "react-icons/fa";

const MenuStart = () => {
    return (
        <div className='text-center text-black text-2xl bg-[rgb(14,41,74)]'>
            <div>
                <h3>Добро пожаловать в наш магазин!</h3>
                <h3>Наши соц сети</h3>
                <div
                    className='flex flex-col items-center justify-center mx-auto space-y-3'> {/* Вертикальное расположение и отступы */}
                    <ButtonNetWork title='Бот' url='https://t.me/tysbo_prog' icons={<FaTelegram />}/>
                    <ButtonNetWork title='Канал' url='https://t.me/tysbo_prog' icons={<FaTelegram />}/>
                </div>
            </div>
            <ProductList/>
        </div>
    )
}

export default MenuStart;