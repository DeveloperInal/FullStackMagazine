import { useEffect } from 'react';
import ProductCard from '../Card/ProductCard';
import { useAppDispatch, useAppSelector } from "../../hooks/reduxHooks";
import { getCardData } from "../Slices/ProductSlice";

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
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 justify-items-center gap-2">
                {products.map((product, index) => (
                    <ProductCard
                        key={index}
                        card_title={product.title}
                        price={product.price}
                        imageUrl={product.image_url}
                    />
                ))}
            </div>
    );
}
