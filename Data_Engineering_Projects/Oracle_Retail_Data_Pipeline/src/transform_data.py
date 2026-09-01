def build_order_detail_dataset( orders_df,
                                customers_df,
                                order_items_df,
                                products_df ):
    transformed_df = orders_df.merge(
        customers_df,
        on = 'customer_id',
        how = 'left'
    )

    transformed_df = transformed_df.merge(
        order_items_df,
        on = 'order_id',
        how = 'left'
    )

    transformed_df = transformed_df.merge(
        products_df,
        on = 'product_id',
        how = 'left'
    )

    transformed_df['line_total'] = (
        transformed_df['quantity'] * transformed_df['unit_price']
    )

    transformed_df['order_total'] = (
        transformed_df.groupby('order_id')['line_total'].transform('sum')
    )

    transformed_df['order_year'] = transformed_df['order_date'].dt.year
    transformed_df['order_month'] = transformed_df['order_date'].dt.month

    transformed_df['order_year_month'] = (
        transformed_df['order_date'].dt.strftime('%Y-%m')
    )

    return transformed_df