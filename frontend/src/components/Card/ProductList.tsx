import { useEffect } from 'react';
import ProductCard from '../Card/ProductCard.tsx';
import { useAppDispatch, useAppSelector } from "../../hooks/reduxHooks.ts";
import { getCardData } from "../Slices/ProductSlice.ts";

export default function ProductList() {
    const dispatch = useAppDispatch();
    const { list: products, loading, error } = useAppSelector((state) => state.card);

    useEffect(() => {
        dispatch(getCardData());
    }, [dispatch]);

    if (loading) {
        return <p>Loading...</p>;
    }

    if (error) {
        return <p>Error: {error}</p>;
    }

    return (
        <div className="flex justify-center items-center mx-auto">
            {products.map((product, index) => (
                <ProductCard
                    key={index}
                    card_title={product.title}
                    description={product.description}
                    price={product.price}
                />
            ))}
        </div>
    );
};
