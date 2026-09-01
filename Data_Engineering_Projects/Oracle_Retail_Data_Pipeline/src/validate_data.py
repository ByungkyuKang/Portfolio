VALID_TABLES_DUP = {
    "customers":"customer_id",
    "products":"product_id",
    "orders":"order_id",
    "order_items":"order_item_id"
}

VALID_TABLES_CONST = (
    "products",
    "orders",
    "order_items"
)

VALID_FKS = (
    "customer_id",
    "order_id",
    "product_id"
)

def check_constraints( table_name, df ):
    table_name = table_name.lower()
            
    if table_name not in VALID_TABLES_CONST:
        raise ValueError(f"Invalid table name: {table_name}")
    
    if table_name == 'products':
        const_violation = len( df[ df['price']<0 ] )
        const_dic = {'price':const_violation}
    elif table_name == 'order_items':
        const_violation = len( df[ df['quantity']<=0 ] )
        const_dic = {'quantity':const_violation}
        
        const_violation = len( df[ df['unit_price']<0 ] )
        const_dic['unit_price'] = const_violation
    elif table_name == 'orders':
        const_violation = len( df[ ~df['status'].isin(['COMPLETED', 'SHIPPED', 'CANCELLED','PENDING']) ] )
        const_dic = {'status':const_violation}
    return const_dic


def check_pk_duplicates( table_name, df ):
    table_name = table_name.lower()
        
    if table_name not in VALID_TABLES_DUP:
        raise ValueError(f"Invalid table name: {table_name}")
    
    pk = VALID_TABLES_DUP[table_name]

    return df[pk].duplicated().sum() 


def check_fk_integrity( fk_name, base_df, reference_df ):
    fk_name = fk_name.lower()

    if fk_name not in VALID_FKS:
        raise ValueError(f"Invalid fk name: {fk_name}")

    invalidation = len(base_df[
            ~(base_df[fk_name].isin(reference_df[fk_name]))
    ])
    
    return invalidation

def calculate_total_violations( validation_results ):
    total_violations = 0
    for result in validation_results.values():
        total_violations += sum(result.values())
    return total_violations
