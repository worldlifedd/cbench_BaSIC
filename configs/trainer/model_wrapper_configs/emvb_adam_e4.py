config = dict(
    optimizer_type="Adam",
    optimizer_config=dict(
        base_lr=1e-4,
    ),
    multiopt_configs=[
        dict(
            optimizer_config=dict(
                optimizer_type="Adam",
                base_lr=1e-4,
            ),
        )
    ]
)