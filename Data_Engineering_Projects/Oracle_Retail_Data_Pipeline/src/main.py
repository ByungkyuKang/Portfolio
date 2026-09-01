from extract_data import extract_table, print_df_info
from validate_data import check_pk_duplicates, check_constraints, check_fk_integrity, calculate_total_violations
from transform_data import build_order_detail_dataset

def main():
    customers_df = extract_table('customers')
    products_df = extract_table('products')
    orders_df = extract_table('orders')
    order_items_df = extract_table('order_items')

    print_df_info('customers', customers_df)
    print_df_info('products', products_df)
    print_df_info('orders', orders_df)
    print_df_info('order_items', order_items_df)

    PK_DUP_RELATIONSHIPS = [
        ('customers', customers_df),
        ('products', products_df),
        ('orders', orders_df),
        ('order_items', order_items_df)
    ]

    CHECK_CONST_RELATIONSHIPS = [
        ('products', products_df),
        ('orders', orders_df),
        ('order_items', order_items_df)
    ]

    FK_RELATIONSHIP = [
        ("customer_id", orders_df, "orders", customers_df, "customers"),
        ("order_id", order_items_df, "order_items", orders_df, "orders"),
        ("product_id", order_items_df, "order_items", products_df, "products")
    ]

    validation_results = {
            "pk_duplicates": {},
            "constraints": {},
            "fk_integrity": {}
        }
    
    print("\nPK Duplicates Check:")
    for table, df in PK_DUP_RELATIONSHIPS:
        cnt = check_pk_duplicates(table, df)
        validation_results["pk_duplicates"][table] = cnt
        print(f"\t{table} PK duplicates: {cnt}")

    print("\nConstraint Check:")
    for table, df in CHECK_CONST_RELATIONSHIPS:
        if table == "order_items":
            const_dic = check_constraints(table, df)
            
            for column, cnt_violation in const_dic.items():
                validation_results["constraints"][f"{table}.{column}"] = cnt_violation
                if column == 'quantity':
                    if cnt_violation != 0:
                        print(f"\t{cnt_violation} row(s) of {column.upper()} in {table.upper()} is(are) equal to or less than 0.")
                    else:
                        print(f"\tSatisfying Constraints ({column.upper()} of {table.upper()} has to be > 0).")
                else:
                    if cnt_violation != 0:
                        print(f"\t{cnt_violation} row(s) of {column.upper()} in {table.upper()} is(are) less than 0.")
                    else:
                        print(f"\tSatisfying Constraints ({column.upper()} of {table.upper()} has to be >= 0).")
        else:
            const_dic = check_constraints(table, df)
            for column, cnt_violation in const_dic.items():
                validation_results["constraints"][f"{table}.{column}"] = cnt_violation
                if column == 'status':
                    if cnt_violation != 0:
                        print(f"\t{cnt_violation} row(s) of {column.upper()} in {table.upper()} is(are) not COMPLETED, SHIPPED, CANCELLED, or PENDING")
                    else:
                        print(f"\tSatisfying Constraints ({column.upper()} of {table.upper()} has to be COMPLETED, SHIPPED, CANCELLED, or PENDING).")
                else:
                    if cnt_violation != 0:
                        print(f"\t{cnt_violation} row(s) of {column.upper()} in {table.upper()} is(are) less than 0.")
                    else:
                        print(f"\tSatisfying Constraints ({column.upper()} of {table.upper()} has to be >= 0).")

    print("\nFK Integrity Check:")
    for fk, base_df, base_table, ref_df, ref_table in FK_RELATIONSHIP:
        cnt_invalidation = check_fk_integrity(fk, base_df, ref_df)

        validation_results["fk_integrity"][f"{base_table}.{fk}"] = cnt_invalidation

        if cnt_invalidation == 0:
            print(f"\tFK integrity satisfied: {base_table}.{fk} references {ref_table}.{fk}.")
        else:
            print(
                f"\tFK integrity violation: "
                f"{cnt_invalidation} row(s) in "
                f"{base_table}.{fk} do not reference "
                f"{ref_table}.{fk}."
            )

    print()
    print("="*30)
    print("\tValidation Results")
    print("="*30)
    
    total_violations = calculate_total_violations( validation_results )
    print(f"Total Violations: {total_violations}")
    if total_violations == 0:
        print("Overall Validation: PASS")
    else:
        print("Overall Validation: FAIL")

    order_details_df = build_order_detail_dataset(
        orders_df, customers_df, order_items_df, products_df
    )

    print(f"\n{order_details_df.head()}")


if __name__ == "__main__":
    main()