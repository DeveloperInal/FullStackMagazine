import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import axios from "axios";

const baseURL = "http://localhost:8000/api/v1";

interface userProductType {
    tg_id: number;
    card_title: string;
    by_product_date: string;
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

export const postUserByCardData = createAsyncThunk<
    userProductType[],
    { tg_id: number; card_title: string; by_product_date: string },
    { rejectValue: string }
>(
    'user/postUserByCardData',
    async (data, thunkAPI) => {
        try {
            const response = await axios.post(`${baseURL}/set_by_user_card`, data, {
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
                state.list = action.payload;
            })
            .addCase(postUserByCardData.rejected, (state, action) => {
                state.loading = false;
                state.error = action.payload || 'Произошла ошибка';
            });
    }
});

export default userSlice.reducer;
