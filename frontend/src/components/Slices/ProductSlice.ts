import { createSlice, createAsyncThunk, PayloadAction } from "@reduxjs/toolkit";
import axios from "axios";

const baseURL = "http://45.12.237.111:8000/api/v1";
interface ProductType {
    title: string;
    price: number;
    description: string;
}

interface ProductState {
    list: ProductType[];
    loading: boolean;
    error: string | null;
}

const initialState: ProductState = {
    list: [],
    loading: false,
    error: null,
};

export const getCardData = createAsyncThunk<ProductType[], void, { rejectValue: string }>(
    'card/getCardData',
    async (_, thunkAPI) => {
        try {
            const response = await axios.get(`${baseURL}/get_card`);
            return response.data;
        } catch (error: any) {
            return thunkAPI.rejectWithValue(error.response?.data?.message || error.message);
        }
    }
);

// Создаем slice
const productSlice = createSlice({
    name: 'card',
    initialState,
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(getCardData.pending, (state) => {
                state.loading = true;
                state.error = null;
            })
            .addCase(getCardData.fulfilled, (state, action: PayloadAction<ProductType[]>) => {
                state.loading = false;
                state.list = Array.isArray(action.payload) ? action.payload : [];
            })
            .addCase(getCardData.rejected, (state, action) => {
                state.loading = false;
                state.error = action.payload ?? null;
            });
    }
});

export default productSlice.reducer;
