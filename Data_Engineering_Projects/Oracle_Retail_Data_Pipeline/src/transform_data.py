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


def build_order_summary_dataset(order_details_df):
    # order_summary_df = order_details_df[
    #         ['order_id', 
    #          'customer_id',
    #          'order_date',
    #          'order_year',
    #          'order_month',
    #          'order_year_month',
    #          'status',
    #          'order_total']
    #     ].drop_duplicates().reset_index(drop=True)
    order_summary_df = order_details_df.groupby('order_id', as_index=False).agg(
                                                    order_id=('order_id', 'first'),
                                                    customer_id=('customer_id', 'first'),
                                                    order_date=('order_date', 'first'),
                                                    order_year=('order_year', 'first'),
                                                    order_month=('order_month', 'first'),
                                                    order_year_month=('order_year_month', 'first'),
                                                    status=('status', 'first'),
                                                    order_total=('order_total', 'first')
                                                )

    return order_summary_df

def build_customer_summary_dataset(order_summary_df):
    customer_summary_df = order_summary_df.groupby('customer_id', as_index=False).agg(
                                order_count=('order_id', 'count'),
                                total_spent=('order_total','sum'),
                                avg_order_value=('order_total', 'mean')
                            )
    customer_summary_df['avg_order_value'] = customer_summary_df['avg_order_value'].round(2)
    
    return customer_summary_df