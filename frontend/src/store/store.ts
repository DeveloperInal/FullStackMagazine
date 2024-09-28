import { configureStore } from '@reduxjs/toolkit';
import ProductReducer from '../components/Slices/ProductSlice.ts';
import UserByProductReducer from "../components/Slices/UserByProductSlice.ts";

export const store = configureStore({
    reducer: {
        card: ProductReducer,
        user: UserByProductReducer
    },
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;