export type userProductType = {
    tg_id: number;
    card_title: string;
    by_product_date: string;
}

export type userProductState = {
    list: userProductType[];
    loading: boolean;
    error: string | null;
}
