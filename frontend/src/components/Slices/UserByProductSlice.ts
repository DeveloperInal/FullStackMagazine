import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import axios from "axios";

const baseURL = "http://localhost:8000/api/v1";

interface userProductType {
    tg_id: number;
    card_title: string;
    price: number;
    by_product_date: string;
    promocode: string;  // Backend generates this
}

interface userProductState {
    list: userProductType[];
    loading: boolean;
    error: string | null;
}

const initialStateUser: userProductState = {
    list: [],
    loading: false,
    error: null,
};

// Async thunk to send purchase data to the backend
export const postUserByCardData = createAsyncThunk<
    userProductType[],
    { tg_id: number; card_title: string; price: number, promocode: string },
    { rejectValue: string }
>(
    'user/postUserByCardData',
    async (data, thunkAPI) => {
        try {
            const by_product_date = new Date().toISOString();  // Generate date for the purchase
            const response = await axios.post(`${baseURL}/set_by_user_card`,
                {
                    ...data,
                    by_product_date 
                }, {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                });
            return response.data;
        } catch (error: any) {
            return thunkAPI.rejectWithValue(error.response?.data?.message || error.message);
        }
    }
);

// User slice to handle the Redux state
const userSlice = createSlice({
    name: 'user',
    initialState: initialStateUser,
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(postUserByCardData.pending, (state) => {
                state.loading = true;
                state.error = null;
            })
            .addCase(postUserByCardData.fulfilled, (state, action) => {
                state.loading = false;
                state.list = [...state.list, ...action.payload];
            })
            .addCase(postUserByCardData.rejected, (state, action) => {
                state.loading = false;
                state.error = action.payload || 'Произошла ошибка';
            });
    }
});

export default userSlice.reducer;
